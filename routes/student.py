from flask import Blueprint, render_template, request, redirect, url_for, session
from models.student_model import StudentModel

student_bp = Blueprint("student", __name__)


@student_bp.route("/add-student", methods=["GET", "POST"])
def add_student():

    if "admin" not in session:
        return redirect(url_for("auth.login"))

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

    return render_template("students/add_student.html")


@student_bp.route("/students")
def students():

    if "admin" not in session:
        return redirect(url_for("auth.login"))

    keyword = request.args.get("search")

    if keyword:
        student_list = StudentModel.search_students(keyword)
    else:
        student_list = StudentModel.get_all_students()

    return render_template(
        "students/students.html",
        students=student_list,
        keyword=keyword
    )


@student_bp.route("/edit-student/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    if "admin" not in session:
        return redirect(url_for("auth.login"))

    student = StudentModel.get_student_by_id(id)

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
            "address": request.form["address"]
        }

        StudentModel.update_student(id, student_data)

        return redirect(url_for("student.students"))

    return render_template(
        "students/edit_student.html",
        student=student
    )


@student_bp.route("/delete-student/<int:id>")
def delete_student(id):

    if "admin" not in session:
        return redirect(url_for("auth.login"))

    StudentModel.delete_student(id)

    return redirect(url_for("student.students"))