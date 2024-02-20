import os
from flask import (
    Flask, render_template, request, flash, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

MONGO = PyMongo(app)

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/our_fleet")
def our_fleet():
    return render_template("our_fleet.html")


@app.route("/sell_car")
def sell_car():
    return render_template("sell_car.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash (
            "Thank you for contacting us! We have received your enquiry.".format(
                request.form.get("name")))
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    """
    On 404 error redirects the user to the 404 page
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(err):
    """
    On 500 error redirects the user to the 500 page
    """
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
