from flask import Flask, redirect, url_for, render_template, request
from sqlalchemy.orm import session
from . import app, db
from .models import Teachers, Subjects, Add_Teacher, Select_Subject
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


@app.route("/") 
@app.route('/home', methods=['GET', 'POST', 'PUT'])
def home():
    form = Add_Teacher()
    teacher_list = Teachers.query.all()  
    subs = Subjects.query.all()

    return render_template('home.html', tl=teacher_list, form=form)

@app.route('/create_teacher', methods=['GET', 'POST', 'PUT', 'DELETE'])
def add_teacher():
    form = Add_Teacher()
    if request.method == 'POST': 
        subs = Subjects.query.all()
        form.teach_this.choices = [(sub.sub_id, sub.sub_name) for sub in subs]

        new_teacher = Teachers(teacher_name=form.teacher_name.data, subject_id=form.teach_this.data)
                            
        db.session.add(new_teacher)
        db.session.commit()

        return redirect(url_for('home'))
    
    else:   
        subs = Subjects.query.all()
        form.teach_this.choices = [(sub.sub_id, sub.sub_name) for sub in subs]

        return render_template('add.html', form=form)

    


@app.route('/subject')
def sub():
    subs = Subjects.query.limit(5).all()
    list2 = []
    for sub in subs:
        list2.append([sub.sub_name])

    return render_template('subs.html', subs=list2)



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_sub(id):
    form = Add_Teacher()
    tu = Teachers.query.get(id)
    subs = Subjects.query.all()
    form.teach_this.choices = [(sub.sub_id, sub.sub_name) for sub in subs]
    if request.method == 'POST':
        tu.subject_id= form.teach_this.data
        db.session.commit()
        return redirect(url_for('home'))
                            

    else:   
        return render_template('update.html', form=form)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def del_teacher(id):
    td = Teachers.query.get(id)
    db.session.delete(td)
    db.session.commit()
    return redirect(url_for('home'))