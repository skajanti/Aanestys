from application import app, db, login_required
from application.election.models import Election
from application.election.forms import ElectionForm

from flask import redirect, render_template, request, url_for
from sqlalchemy import update
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators


@app.route("/election", methods=["GET", "POST"])
@login_required(role="ADMIN")
def open_election_form():
    return render_template("election/new_election.html", form=ElectionForm())


@app.route("/election/new", methods=["POST"])
@login_required(role="ADMIN")
def open_election():
    form = ElectionForm(request.form)

    e = Election(form.year.data, True)
    e.active = True

    if not form.validate():
        return render_template("election/new_election.html", form=form)

    if db.session().query(Election.year).filter_by(year=form.year.data).scalar() is None:
        db.session().add(e)
        db.session().commit()

    return redirect(url_for("index"))


@app.route("/election/close", methods=["GET"])
@login_required(role="ADMIN")
def close_election_form():
    return render_template("election/close_election.html")


@app.route("/election/close/", methods=["POST"])
@login_required(role="ADMIN")
def close_election():
    stmt = update(Election).where(Election.active == True).values(active=False)
    db.engine.execute(stmt)

    return redirect(url_for("index"))