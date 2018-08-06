from flask import Flask, render_template, redirect, request, url_for, jsonify
import firebase_admin
from firebase_admin import credentials, auth, firestore
import os
import boto3

application = Flask(__name__)

secret = os.getenv("TCF_ACCOUNTS_SECRET")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

if not os.path.isfile("key.json"):
    session = boto3.session.Session(
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key
    )
    session.resource("s3").Bucket("tcf-accounts-key").download_file(
        "key.json", "key.json"
    )

cred = credentials.Certificate("key.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

@application.route("/")
def index():
    return redirect("/hackathon")


@application.route("/hackathon")
def hackathon():
    return render_template("hackathon.html")


@application.route("/login")
def login():
    return render_template("login.html")


@application.route("/login/new")
def login_new():
    token = request.args.get("token")
    if not token:
        redirect(url_for("login"))


@application.route("/join")
def join():
    return render_template("join.html")


@application.route("/set-claims", methods=["POST"])
def set_claims():
    try:
        token = request.form["token"]
    except KeyError as e:
        return jsonify(
                    {"statusCode": 406, "message": "KeyError Exception" + str(e)}
                )
    except Exception as e:
        pass
    else:
        try:
            decoded_token: dict = auth.verify_id_token(token)
        except Exception as e:
            return jsonify({"statusCode": 505, "message": "Exception" + str(e)})
        else:
            try:
                uid = decoded_token["uid"]
            except KeyError as e:
                return jsonify(
                    {"statusCode": 406, "message": "KeyError Exception" + str(e)}
                )            
            except Exception as e:
                return jsonify({"statusCode": 505, "message": "Exception" + str(e)})
            else:
                try:
                    doc_data: dict = db.collection("accounts").document(uid).get().to_dict()
                except TypeError as e:
                    return jsonify(
                        {"statusCode": 406, "message": "TypeError Exception" + str(e)}
                    )
                except Exception as e:
                    return jsonify({"statusCode": 505, "message": "Exception" + str(e)})pass
                else:
                    try:
                        permissions: dict = doc_data["permissions"]
                    except TypeError as e:
                        return jsonify(
                            {"statusCode": 406, "message": "TypeError Exception" + str(e)}
                        )
                    except KeyError as e:
                        return jsonify(
                            {"statusCode": 406, "message": "KeyError Exception" + str(e)}
                        )
                    except Exception as e:
                        return jsonify({"statusCode": 505, "message": "Exception" + str(e)})
                    else:
                        try:
                            auth.set_custom_user_claims(uid, permissions)
                        except Exception as e:
                            return jsonify({"statusCode": 505, "message": "Exception" + str(e)})
                        else:
                            return jsonify({"statusCode": 202, "message": "operation successful"})

if __name__ == "__main__":
    application.run()


