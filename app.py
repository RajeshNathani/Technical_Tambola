from flask import Flask, render_template, request
import random
from numpy import fromiter
import pandas as pd
import ast

app = Flask(__name__, static_folder='public')
data = pd.read_csv('data_new.csv')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/game", methods=['GET', 'POST'])
def game():
    if request.method == "POST":
        name = request.form['Name']
        password = request.form['pass']
        rows = 3
        su = data['Username'].str.contains(name).sum(
        ) and data['Password'].str.contains(password).sum()
        if su >= 1:
            first = data[data['Username'] == "raj1234"]['first'].tolist()
            second = data[data['Username'] == name]['second'].tolist()
            third = data[data['Username'] == name]['third'].tolist()
            print(first)
            row1 = ast.literal_eval(str(first[0]))
            row2 = ast.literal_eval(str(second[0]))
            row3 = ast.literal_eval(str(third[0]))
            return render_template("game.html", rows=rows, first=row1, second=row2, third=row3)
        else:
            return "Invalid credentials"

    else:
        return "You are not authorized to access content"


if __name__ == '__main__':
    app.run(debug=True)
