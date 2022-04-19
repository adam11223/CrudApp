from enum import unique
from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class Teachers(db.Model):
    teacher_id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(25),nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.sub_id'))

class Subjects(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(20))
    teachers = db.relationship('Teachers', backref='subjects')

class Add_Teacher(FlaskForm):
    teacher_name =  StringField('Enter Your name')
    teach_this = SelectField('What subject do you teach?')
    submit = SubmitField('Add Teacher')
    submit2 = SubmitField('Update')

class Select_Subject(FlaskForm):
    subject = SelectField('Pick a subject', choices=[])
    submit = SubmitField('Add subject')

    