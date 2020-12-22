from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
Uncomment if using SQLAlchemy

db = SQLAlchemy(app)
from models import * 
"""

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)