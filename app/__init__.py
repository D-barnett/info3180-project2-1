from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:uwimona123@localhost/project3db"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vcgzpvuhvmkslv:87b481518ec083d5ba8a7a914bcf40bdf04d7cfd13fc0f02ea7bd36c3b6a772f@ec2-54-225-119-223.compute-1.amazonaws.com:5432/d2u252a3ffcdh"

db = SQLAlchemy(app)
db.create_all()

from app import views,models
