from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/about")
def about():
    return redirect('/')