from flask import render_template, redirect, url_for

from Level2.flask_reminder.flask_app import app
from Level2.flask_reminder.flask_app.models import Student, Lecture, Professor
from Level2.flask_reminder.flask_app.forms import LecturesForm, StudentForm, TeacherForm
from Level2.flask_reminder.flask_app import db


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/students')
def students_route():
    try:
        students = Student.query.all()
    except:
        students = []
    return render_template('students.html', students=students)


@app.route('/teachers')
def teachers_route():
    try:
        professor = Professor.query.all()
    except:
        professor = []
    return render_template('teachers.html', professors=professor)


@app.route('/lectures')
def lectures_route():
    try:
        lectures = Lecture.query.all()
    except:
        lectures = []
    lectures_with_professors = []
    lectures_students = []
    for lecture in lectures:
        for student in lecture.students:
            lecture_student_dict = {'student_name': student.name, 'student_surname': student.surname}
            lectures_students.append(lecture_student_dict)
        prof = Professor.query.get(lecture.professor_id)
        new_dict = {'id': prof.id, 'lecture_name': lecture.name, 'students': lectures_students, 'prof_name': prof.name,
                    'prof_surname': prof.surname, 'prof_exp': prof.experience}
        lectures_with_professors.append(new_dict)

    return render_template('lectures.html', lectures=lectures_with_professors)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student_route():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data,
                          surname=form.surname.data)
        student.lectures = []
        for lecture in form.lectures.data:
            selected_lecture = Lecture.query.get(lecture.id)
            student.lectures.append(selected_lecture)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students_route'))
    return render_template('add_student.html', form=form)


@app.route('/add_lecture', methods=['GET', 'POST'])
def add_lectures_route():
    form = LecturesForm()
    if form.validate_on_submit():
        lecture = Lecture(name=form.name.data, professor_id=form.professor.data.id)
        lecture.students = []
        for student in form.students.data:
            selected_student = Student.query.get(student.id)
            lecture.students.append(selected_student)
        db.session.add(lecture)
        db.session.commit()
        return redirect(url_for('lectures_route'))
    return render_template('add_lecture.html', form=form)


@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    form = TeacherForm()
    if form.validate_on_submit():
        professor = Professor(name=form.name.data,
                              surname=form.surname.data,
                              experience=form.experience.data)
        professor.lectures = []
        for lecture in form.lectures.data:
            selected_lecture = Lecture.query.get(lecture.id)
            professor.lectures.append(selected_lecture)
        db.session.add(professor)
        db.session.commit()
        return redirect(url_for('add_teacher'))
    return render_template('add_teacher.html', form=form)


@app.route('/update_professor/<int:id>', methods=['GET', 'POST'])
def update_professor(id):
    updated_professor = Professor.query.get(id)
    form = TeacherForm()
    if form.validate_on_submit():
        updated_professor.name = form.name.data
        updated_professor.surname = form.surname.data
        updated_professor.experience = form.experience.data
        updated_professor.lectures = []
        for lecture in form.lectures.data:
            new_lecture = Lecture.query.get(lecture.id)
            updated_professor.lectures.append(new_lecture)
        db.session.commit()
        return redirect((url_for('teachers_route')))
    return render_template('update_professor.html', form=form, professor=updated_professor)


@app.route('/delete_professor/<int:id>', methods=['GET', 'POST'])
def delete_professor(id):
    deleted_professor = Professor.query.get(id)
    db.session.delete(deleted_professor)
    db.session.commit()
    return redirect(url_for('teachers_route'))


@app.route('/update_student/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    updated_student = Student.query.get(id)
    form = StudentForm()
    if form.validate_on_submit():
        updated_student.name = form.name.data
        updated_student.surname = form.surname.data
        db.session.commit()
        return redirect((url_for('students_route')))
    return render_template('update_student.html', form=form, student=updated_student)


@app.route('/delete_student/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
    deleted_student = Student.query.get(id)
    db.session.delete(deleted_student)
    db.session.commit()
    return redirect(url_for('students_route'))


@app.route('/update_lecture/<int:id>', methods=['GET', 'POST'])
def update_lecture(id):
    updated_lecture = Lecture.query.get(id)
    form = LecturesForm()
    if form.validate_on_submit():
        updated_lecture.name = form.name.data
        updated_lecture.professor_id = form.professor.data.id
        for student in form.students.data:
            selected_student = Student.query.get(student.id)
            updated_lecture.students.append(selected_student)
        db.session.commit()
        return redirect((url_for('lectures_route')))
    return render_template('update_lecture.html', form=form, lectures=updated_lecture)
