from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:uwimona123@localhost/project3db"

db = SQLAlchemy(app)
db.create_all()

from app import views,models