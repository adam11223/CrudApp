from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teachers, Subjects


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY = 'YOUR_SECRET_KEY',
            WTF_CSRF_ENEBLED=False
        )

        return app

    def setUp(self):
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

    
    def tearDown(self):
        db.drop_all()


class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for("home"))
        assert "Adam Rashid" in response.data.decode()


class TestCreate(TestBase):
    def test_add_teacher(self):
        
        with self.client:
            response = self.client.post(
                url_for("add_teacher"),
                data={"teacher_name": "Steven Smith",  "teach_this" :'subjects'},
                follow_redirects=True
            )
            assert "Steven Smith" in response.data.decode()



          
class testRead_subject(TestBase):
    def test_subjects(self):
        response = self.client.get(url_for("sub"))
        assert "Maths" in response.data.decode()


class TestUpdate(TestBase):
    def test_update_teacher(self):
        response = self.client.post(
            url_for("update_sub", id=1),
            data=dict(subjects=Subjects(sub_name= 'Maths')),
            follow_redirects=True
            )
        assert "Maths" in response.data.decode()


class TestDel(TestBase):
    def test_delete(self):
        response = self.client.post(
            url_for("del_teacher", id=1),
            follow_redirects=True
            )
        assert "Adam Rashid" not in response.data.decode()
        self.assertEqual(response.status_code, 200)
