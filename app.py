from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Student, Subject, ClassInfo, StudentSubject
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Initialize the login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##########################################################
################ Routes and views ########################
##########################################################

# Route for the homepage (for students)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        roll_id = request.form['roll_id']
        class_name = request.form['class_name']
        
        student = Student.query.filter_by(roll_id=roll_id, class_name=class_name).first()
        
        if student:
            results = student.get_results()
            return render_template('results.html', student=student, results=results)
        else:
            error_message = "Student not found or incorrect class/roll number."
            return render_template('home.html', error_message=error_message)
    
    classes = ClassInfo.query.all()  # Get all available classes
    return render_template('home.html', classes=classes)

# Route to view results (already implemented above in the form submission)
@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        full_name = request.form['full_name']
        roll_id = request.form['roll_id']
        class_name = request.form['class_name']
        student = Student(full_name=full_name, roll_id=roll_id, class_name=class_name)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('manage_students'))
    return render_template('add_student.html')

@app.route('/manage_students')
@login_required
def manage_students():
    students = Student.query.all()
    return render_template('manage_students.html', students=students)

# Edit Student
@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        student.full_name = request.form['full_name']
        student.roll_id = request.form['roll_id']
        student.class_name = request.form['class_name']
        db.session.commit()
        return redirect(url_for('manage_students'))

    return render_template('edit_student.html', student=student)

# Delete Student
@app.route('/delete_student/<int:student_id>')
@login_required
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('manage_students'))

@app.route('/add_subject', methods=['GET', 'POST'])
@login_required
def add_subject():
    if request.method == 'POST':
        name = request.form['name']
        code = request.form['code']
        total_marks = int(request.form['total_marks'])
        subject = Subject(name=name, code=code, total_marks=total_marks)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_subject.html')

@app.route('/manage_subjects')
@login_required
def manage_subjects():
    subjects = Subject.query.all()
    return render_template('manage_subjects.html', subjects=subjects)

# Edit Subject
@app.route('/edit_subject/<int:subject_id>', methods=['GET', 'POST'])
@login_required
def edit_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)

    if request.method == 'POST':
        subject.name = request.form['name']
        subject.code = request.form['code']
        db.session.commit()
        return redirect(url_for('manage_subjects'))

    return render_template('edit_subject.html', subject=subject)

# Delete Subject
@app.route('/delete_subject/<int:subject_id>')
@login_required
def delete_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    db.session.delete(subject)
    db.session.commit()
    return redirect(url_for('manage_subjects'))

@app.route('/add_class', methods=['GET', 'POST'])
@login_required
def add_class():
    if request.method == 'POST':
        class_name = request.form['class_name']
        section = request.form['section']
        new_class = ClassInfo(class_name=class_name, section=section)
        db.session.add(new_class)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_class.html')

@app.route('/manage_classes')
@login_required
def manage_classes():
    classes = ClassInfo.query.all()
    return render_template('manage_classes.html', classes=classes)

@app.route('/edit_class/<int:class_id>', methods=['GET', 'POST'])
@login_required
def edit_class(class_id):
    class_info = ClassInfo.query.get_or_404(class_id)

    if request.method == 'POST':
        class_info.class_name = request.form['class_name']
        class_info.section = request.form['section']
        db.session.commit()
        return redirect(url_for('manage_classes'))

    return render_template('edit_class.html', class_info=class_info)

@app.route('/delete_class/<int:class_id>')
@login_required
def delete_class(class_id):
    class_info = ClassInfo.query.get_or_404(class_id)
    db.session.delete(class_info)
    db.session.commit()
    return redirect(url_for('manage_classes'))


@app.route('/assign_marks', methods=['GET', 'POST'])
@login_required
def assign_marks():
    if request.method == 'POST':
        student_id = request.form['student_id']
        subject_id = request.form['subject_id']
        obtained_marks = int(request.form['obtained_marks'])

        student = Student.query.get(student_id)
        subject = Subject.query.get(subject_id)

        if student and subject:
            # Assuming you have a StudentSubject table
            student_subject = StudentSubject(
                student_id=student.id,
                subject_id=subject.id,
                obtained_marks=obtained_marks
            )
            db.session.add(student_subject)
            db.session.commit()
            return redirect(url_for('dashboard'))
        return redirect(url_for('assign_marks'))

    students = Student.query.all()
    subjects = Subject.query.all()
    return render_template('assign_marks.html', students=students, subjects=subjects)

@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        if current_user.password == old_password:
            if new_password == confirm_password:
                current_user.password = new_password
                db.session.commit()
                return redirect(url_for('dashboard'))
    return render_template('change_password.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
