from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# User model for the admin login
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Class model to store class details
class ClassInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(150), nullable=False)
    section = db.Column(db.String(150), nullable=False)

    # One-to-many relationship with students
    students = db.relationship('Student', backref='class_info', lazy=True)

# Subject model with total marks
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(150), unique=True, nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)

    # Many-to-many relationship with students through StudentSubject
    students = db.relationship('StudentSubject', backref='subject', lazy=True)

# Student model with relationship to ClassInfo
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    roll_id = db.Column(db.String(150), unique=True, nullable=False)
    class_name = db.Column(db.String(150), db.ForeignKey('class_info.class_name'), nullable=False)

    # Many-to-many relationship with subjects through StudentSubject
    subjects = db.relationship('StudentSubject', backref='student', lazy=True)

    # Method to get results
    def get_results(self):
        return {subject.subject.name: {'total': subject.subject.total_marks, 'obtained': subject.obtained_marks} for subject in self.subjects}

# Helper model to track the marks a student has obtained in each subject
class StudentSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    obtained_marks = db.Column(db.Integer, nullable=False)
