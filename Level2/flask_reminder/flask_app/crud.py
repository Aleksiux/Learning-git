from Level2.flask_reminder.flask_app import db, app
from Level2.flask_reminder.flask_app.models import Student, Lecture, Professor



# app.app_context().push()
# db.create_all()
# student1 = Students('Jonas', 'Jonaitis')
# student2 = Students('Petras', 'Petraitis')
# student3 = Students('Auste', 'Austaityte')
# student4 = Students('Igne', 'Ignaityte')
# db.session.add_all([student1, student2, student3, student4])
# db.session.commit()
# professor1 = Professors('George', 'Washington', experience= 12, lectures_id=None)
# professor2 = Professors('Valdas', 'Adamkus', experience=25, lectures_id=None)
# professor3 = Professors('Antanas','Smetona', experience=100, lectures_id=None)
# professor4 = Professors('Jonas','Kubilius', experience=2, lectures_id=None)
# professor5 = Professors('Algis', 'Algiauskas',experience= 3, lectures_id=None)
# db.session.add_all([professor1, professor2, professor3, professor4, professor5])
# db.session.commit()
# lecture1 = Lectures('Introduction to Modal Logic')
# lecture2 = Lectures('Molecular Biology')
# lecture3 = Lectures('History of Lithuania')
# lecture4=Lectures('Epidemiology')
# db.session.add_all([lecture1, lecture2, lecture3, lecture4])
# db.session.commit()

#
# query_students = Student.query.all()
# query_teachers = Professor.query.all()
# query_lectures = Lecture.query.all()