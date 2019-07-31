from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('personal_website.html')
    
