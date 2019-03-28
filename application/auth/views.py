from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, #Account_CreateForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

# @app.route("/auth/create_account")
# def create_account():
#     # form = Account_CreateForm(request.form)

#     # l = User(form.username.data)
#     # l.name = form.username.data
#     # l.password = form.password.data

#     # db.session().add(l)
#     # db.session().commit()

#     name = request.form.get('name')
#     password = request.form.get('password')
#     usernameOhjelma herokussa = request.form.get('username')

    

#     new_user = User(username=username, password=password, name=name)

#     db.session.add(new_user)
#     db.session.commit()

#     return redirect(url_for("index"))