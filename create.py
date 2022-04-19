from application import db
from application.models import Teachers, Subjects, Add_Teacher, Select_Subject

db.drop_all()
db.create_all()
maths = Subjects(sub_name = 'Maths')
english = Subjects(sub_name = 'English')
science = Subjects(sub_name = 'Science')

db.session.add(maths)
db.session.add(english)
db.session.add(science)

adam = Teachers(teacher_name = 'Adam Rashid', subjects = Subjects(sub_name='Maths'))
molly = Teachers(teacher_name = 'Molly Smith', subjects = Subjects(sub_name='English'))
earl = Teachers(teacher_name = 'Earl Gray', subjects = Subjects(sub_name='Science'))

db.session.add(adam)
db.session.add(molly)
db.session.add(earl)

db.session.commit()