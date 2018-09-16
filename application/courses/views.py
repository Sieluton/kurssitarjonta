from application import app, db
from flask import redirect, render_template, request, url_for
from application.courses.models import Course

@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
def courses_form():
    return render_template("courses/new.html")
  
@app.route("/courses/<course_id>/edit/", methods=["POST"])
def courses_edit_form(course_id):
    return render_template("courses/edit.html", course = Course.query.get(course_id))

@app.route("/courses/", methods=["POST"])
def courses_create():
    c = Course(request.form.get("name"), request.form.get("description"))

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
def courses_edit():
    c = Course(request.form.get("name"), request.form.get("description"))

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_index"))