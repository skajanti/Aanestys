from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from passlib.hash import pbkdf2_sha256

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, Account_CreateForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    res = pbkdf2_sha256.verify(form.password.data, user.password)

    if not res:
        return render_template("auth/loginform.html", form = form,
                               error = "The entered Username or Password was incorrect.")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new")
def create_accountform():
    return render_template("auth/create_accountform.html", form=Account_CreateForm())

@app.route("/auth/create_account", methods = ["GET", "POST"])
def create_account():
    form = Account_CreateForm(request.form)

    role = "USER"
    if form.name.data == "admin":
        role = "ADMIN"

        hash1 = pbkdf2_sha256.hash(form.password.data)

    l = User(form.name.data, form.username.data, hash1, role)

    if not form.validate():
        return render_template("/auth/create_accountform.html", form = form, 
                               error = "Name, Username, and Password must be between 4 and 24 characters long.")

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("index"))