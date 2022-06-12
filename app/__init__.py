from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html", title="index", url=os.getenv("URL"))

@app.route("/about_maleluca")
def about_maleluca():
    return render_template("about_ai.html", title="about_maleluca", url=os.getenv("URL"))
