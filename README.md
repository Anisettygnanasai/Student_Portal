# 🎓 Student Portal System
A simple and effective student portal built with Flask and MongoDB. This web application provides separate interfaces for students and administrators. Students can log in to view their academic results, while the admin can manage all student records through a secure dashboard.

✨ Features
👨‍🎓 Student Panel
Secure Login: Students log in using their unique Roll Number and password.

Dashboard: After logging in, students can view their personal details.

View Results: Displays semester-wise results and the total CGPA.

🔐 Admin Panel
Secure Login: A separate, credential-based login for the administrator.

Student Management Dashboard: View a list of all students currently in the database.

Full CRUD Functionality:

Create: Add new students to the database through a web form.

Read: View all student details.

Update: Edit the information of any existing student.

Delete: Remove a student's record permanently.

🚀 Tech Stack
Backend: Python, Flask

Database: MongoDB

Frontend: HTML, CSS

Dependencies: Flask-PyMongo, python-dotenv

🔧 Setup and Installation
Follow these steps to get the project running on your local machine.

1. Clone the Repository
Bash

git clone https://github.com/your-username/student-portal.git
cd student-portal
2. Create a Virtual Environment
It's recommended to create a virtual environment to manage project dependencies.

Bash

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install all the required packages from requirements.txt.

Bash

pip install -r requirements.txt
4. Set Up MongoDB
Make sure you have a MongoDB instance running on your machine or have access to a cloud instance (like MongoDB Atlas).

5. Configure Environment Variables
Create a file named .env in the root directory of the project and add the following lines. This file stores your database connection string and a secret key for the application session.

Code snippet

MONGO_URI=mongodb://localhost:27017/collegeDB
SECRET_KEY=your_super_secret_key_goes_here
Note: Replace collegeDB with your desired database name. You can change the secret key to any random string.

6. Run the Application
Start the Flask development server.

Bash

python app.py
The application will be running at http://127.0.0.1:5000. 🎉

🧑‍💻 How to Use
Admin Access: Navigate to /admin/login. The default credentials are:

Username: admin

Password: admin123

Student Access: An admin must first add a student via the admin dashboard. Once added, the student can log in at /student/login using the Roll Number and Password set by the admin.

📂 Project Structure
student-portal/
├── app.py                  # Main Flask application logic
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── images/
│       ├── bg.jpg          # Background image
│       └── logo.png        # College logo
└── templates/
    ├── index.html          # Homepage
    ├── login.html          # Student login page
    ├── admin_login.html    # Admin login page
    ├── student_dashboard.html # Student's personal dashboard
    ├── admin_dashboard.html  # Admin dashboard with student list
    ├── add_student.html    # Form to add a new student
    └── edit_student.html   # Form to edit a student's details
