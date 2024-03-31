from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='thisissecretkey'
db.init_app(app)


from market import routes