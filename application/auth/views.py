from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm
from flask import flash


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/signup", methods=["GET", "POST"])
def auth_signup():
    if not current_user:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("auth/singupform.html", form=SignupForm())

    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/singupform.html", form=form)

    if not User.query.filter_by(username=form.username.data).count() == 0:
        return render_template("auth/singupform.html", form=form, error="Username not available")

    u = User(form.name.data)
    u.username = form.username.data
    u.password = form.password.data

    db.session().add(u)
    db.session().commit()
    flash('Account created')
    return redirect(url_for("index"))
