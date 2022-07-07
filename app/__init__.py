import datetime
from flask import Flask, render_template, request
import os
from peewee import *
from playhouse.shortcuts import model_to_dict
# from melaluca import predict

app = Flask(__name__)

# # setting mysql db
my_db = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                    user=os.getenv("MYSQL_USER"),
                    password=os.getenv("MYSQL_PASSWORD"),
                    host=os.getenv("MYSQL_HOST"),
                    port=3306)

print(my_db)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = my_db

my_db.connect()
my_db.create_tables([TimelinePost])

@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
    }

@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

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
        img = request.files["candidate"]
        img.save(img.filename) # save the picture TODO: need to create folder for inputs
        # np_pred, lbl_pred = predict(img)
        return "Got it!"
            
    else:
        return render_template("maleluca_action.html", title="maleluca_in_action", url=os.getenv("URL"))