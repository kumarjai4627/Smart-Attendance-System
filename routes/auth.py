from flask import Blueprint, render_template, request, redirect, url_for, session
from models.admin_model import AdminModel

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        admin = AdminModel.login(username, password)

        if admin:

            session["admin"] = admin[1]

            return redirect(url_for("dashboard"))

        else:

            return render_template(
                "auth/login.html",
                error="Invalid Username or Password"
            )

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect(url_for("auth.login"))