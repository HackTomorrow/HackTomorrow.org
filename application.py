from flask import Flask, render_template, redirect, request

tcf_accounts_secret = os.getenv("TCF_ACCOUNTS_SECRET")


# FIREBASE ADMIN SETUP

application = Flask(__name__)

@application.route("/")
def index():
    return redirect("/hackathon")


@application.route("/hackathon")
def hackathon():
    return render_template("hackathon.html")


@application.route("/login")
def login():
    token = request.args.get("token")
    if token:
        # sign in
        # add new permissions to database
        pass
    return render_template("login.html")


@application.route("/join")
def join():
    return render_template("join.html")


if __name__ == "__main__":
    application.run()


