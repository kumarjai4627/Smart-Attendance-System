from flask import Blueprint, render_template, request, redirect, url_for
from models.student_model import StudentModel

student_bp = Blueprint("student", __name__)


@student_bp.route("/add-student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student_data = {
            "student_id": request.form["student_id"],
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "course": request.form["course"],
            "branch": request.form["branch"],
            "semester": request.form["semester"],
            "section": request.form["section"],
            "gender": request.form["gender"],
            "dob": request.form["dob"],
            "address": request.form["address"],
            "photo_sample": ""
        }

        StudentModel.add_student(student_data)

        return redirect(url_for("student.add_student"))

    return render_template("add_student.html")