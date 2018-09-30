from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from application.courses.models import Course
from application.courses.forms import CourseForm


@app.route("/courses/", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses=Course.query.all())


@app.route("/courses/new/")
#@login_required
def courses_form():
    return render_template("courses/new.html", form=CourseForm())


@app.route("/courses/<course_id>/edit/")
#@login_required
def courses_edit_form(course_id):
    return render_template("courses/edit.html", form=CourseForm(course_id),
                           course=Course.query.get(course_id))


@app.route("/courses/", methods=["POST"])
#@login_required
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form=form)

    c = Course(form.name.data, form.description.data)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))


@app.route("/courses/<course_id>/edit/", methods=["POST"])
#@login_required
def courses_edit(course_id):
    c = Course.query.get(course_id)
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/edit.html", form=form)

    c.name = form.name.data
    c.description = form.description.data

    db.session().commit()

    return redirect(url_for("courses_index"))


@app.route("/reservation/<course_id>", methods=["POST"])
@login_required
def courses_reservation(course_id):
    c = Course.query.get(course_id)
    u = current_user
    c.accounts.append(u)
    db.session.add(c)
    db.session.commit()
    flash('Reservation made')
    return redirect(url_for("courses_index"))
