from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv


app = Flask(__name__) #app can use Flask functions now

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = str(os.getenv('secret_key'))

db = SQLAlchemy(app)

from . import routes


#in order to ensure your database password is secure in terminal
#export DATABASE_URI=mysql+pymysql://root:*your password goes here*@*your sql instance public ip*:3306/*name of the database you're using*
#enter it everytime you close vscode