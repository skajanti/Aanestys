from application import app, db
from flask import render_template, request
from application.votes.models import Candidate

@app.route("/votes/new/")
def votes_form():
	return render_template("votes/new.html")

@app.route("/votes/", methods=["POST"])
def votes_create():
	v = Candidate(request.form.get("name"))

	db.session().add(v)
	db.session().commit()

	return "hello world!"
