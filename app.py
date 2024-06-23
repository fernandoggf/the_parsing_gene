
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def void():
    return render_template("void.html")

