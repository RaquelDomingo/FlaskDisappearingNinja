from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template('ninja.html', color='')

@app.route('/ninja/<color>')
def getColor(color):
    return render_template('ninja.html', color=color)


app.run(debug=True) 