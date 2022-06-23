from flask import Flask, render_template, request
import os
from peewee import *

app = Flask(__name__)

# setting mysql db
my_db = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                    user=os.getenv("MYSQL_USER"),
                    password=os.getenv("MYSQL_PASSWORD"),
                    host=os.getenv("MYSQL_HOST"),
                    port=3306)

print(my_db)

@app.route("/")
def base():
    """ Used: templates/base.html - static/styles/base.css """

    return render_template("base.html", title="index", url=os.getenv("URL"))


@app.route("/about_maleluca")
def about_maleluca():
    """ Used: templates/about_ai.html - static/styles/about_ai.css """

    return render_template("about_ai.html", title="about_maleluca", url=os.getenv("URL"))


@app.route("/maleluca_in_action", methods=["GET", "POST"])
def maleluca_in_action():
    """ Used: templates/maleluca_action.html - static/styles/maleluca_action.css """
    """
    TODO:
    ! ADD PICTURES AS PARAM
    ! ADD NN GIF
    ! CREATE BUTTONS AND INPUT
    ! GET WEIGHTS AND CONNECT NN
    """
    if request.method == "POST":
        f = request.files["candidate"]
        f.save(f.filename)
        return "Got it!"
            
    else:
        return render_template("maleluca_action.html", title="maleluca_in_action", url=os.getenv("URL"))