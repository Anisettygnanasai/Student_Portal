# app.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from bson.objectid import ObjectId # <-- Important: Add this import
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@app.route('/')
def home():
    return render_template('index.html')

# --- Student Routes (No changes needed here) ---
@app.route('/student/login', methods=["GET", "POST"])
def student_login():
    if request.method == "POST":
        rollno = request.form['rollno']
        password = request.form['password']
        student = mongo.db.students.find_one({"rollno": rollno, "password": password})
        if student:
            session['student'] = rollno
            return redirect(url_for('student_dashboard'))
        else:
            flash("Invalid Roll Number or Password")
    return render_template("login.html")

@app.route('/student/dashboard')
def student_dashboard():
    if 'student' not in session:
        return redirect(url_for('student_login'))
    student = mongo.db.students.find_one({"rollno": session['student']})
    return render_template("student_dashboard.html", student=student)

# --- Admin Routes (UPDATED) ---
@app.route('/admin/login', methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid credentials")
    return render_template("admin_login.html")

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    # Fetch all students from the database to display them
    all_students = mongo.db.students.find()
    return render_template("admin_dashboard.html", students=all_students)

# --- NEW Route to Add a Student ---
@app.route('/admin/add_student', methods=['GET', 'POST'])
def add_student():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    if request.method == 'POST':
        # Get data from the form
        rollno = request.form.get('rollno')
        name = request.form.get('name')
        password = request.form.get('password')
        # Simple parsing for results, assuming "sem1:8.5,sem2:9.0" format
        results_str = request.form.get('results')
        results = dict(item.split(":") for item in results_str.split(","))
        cgpa = request.form.get('cgpa')

        # Create student document
        student_data = {
            'rollno': rollno,
            'name': name,
            'password': password,
            'results': results,
            'cgpa': cgpa
        }
        mongo.db.students.insert_one(student_data)
        flash("Student added successfully!", "success")
        return redirect(url_for('admin_dashboard'))
    return render_template('add_student.html')

# --- NEW Route to Edit a Student ---
@app.route('/admin/edit_student/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    
    student = mongo.db.students.find_one({'_id': ObjectId(student_id)})
    
    if request.method == 'POST':
        # Get updated data from the form
        updated_data = {
            'rollno': request.form.get('rollno'),
            'name': request.form.get('name'),
            'password': request.form.get('password'),
            'results': dict(item.split(":") for item in request.form.get('results').split(",")),
            'cgpa': request.form.get('cgpa')
        }
        mongo.db.students.update_one(
            {'_id': ObjectId(student_id)},
            {'$set': updated_data}
        )
        flash("Student details updated successfully!", "success")
        return redirect(url_for('admin_dashboard'))
    
    # Convert results dict back to string for display in the form
    student['results_str'] = ",".join([f"{k}:{v}" for k, v in student['results'].items()])
    return render_template('edit_student.html', student=student)

# --- NEW Route to Delete a Student ---
@app.route('/admin/delete_student/<student_id>', methods=['POST'])
def delete_student(student_id):
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    mongo.db.students.delete_one({'_id': ObjectId(student_id)})
    flash("Student deleted successfully!", "danger")
    return redirect(url_for('admin_dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)