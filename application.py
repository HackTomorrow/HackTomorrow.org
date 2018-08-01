from flask import Flask, render_template, redirect, url_for

application = Flask(__name__)

@application.route("/")
def index():
    return redirect("/hackathon")

@application.route("/hackathon")
def hackathon():
    return render_template("hackathon.html")

if __name__ == "__main__":
    application.run()


