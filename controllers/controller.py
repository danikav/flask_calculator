from flask import render_template
from app.modules.calculator import Calculator

from app import app

@app.route('/')
def home():
    return render_template(
        'index.html',
    )

@app.route('/add/<number_1>/<number_2>')
def add(number_1, number_2):
    return render_template(
        'add.html',
        number_1 = int(number_1),
        number_2 = int(number_2),
    )

@app.route('/subtract/<number_1>/<number_2>')
def subtract(number_1, number_2):
    return render_template(
        'subtract.html',
        number_1 = int(number_1),
        number_2 = int(number_2),
    )

@app.route('/multiply/<number_1>/<number_2>')
def multiply(number_1, number_2):
    return render_template(
        'multiply.html',
        number_1 = int(number_1),
        number_2 = int(number_2),
    )

@app.route('/divide/<number_1>/<number_2>')
def divide(number_1, number_2):
    return render_template(
        'divide.html',
        number_1 = int(number_1),
        number_2 = int(number_2),
    )