from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.courses.models import Course
from application.courses.forms import CourseForm


@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses=Course.query.all())


@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form=CourseForm())


@app.route("/courses/<course_id>/edit/", methods=["POST"])
@login_required
def courses_edit_form(course_id):
    return render_template("courses/edit.html", course=Course.query.get(course_id))


@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form=form)

    c = Course(form.name.data)
    c.description = form.description.data
    c.account_id = current_user

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))


@app.route("/courses/", methods=["POST"])
@login_required
def courses_edit():
    c = Course(request.form.get("name"), request.form.get("description"))

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_index"))