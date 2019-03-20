from application import app, db
from flask import redirect, render_template, request, url_for
from application.votes.models import Candidate

@app.route("/votes", methods=["GET"])
def votes_index():
	return render_template("votes/list.html", votes = Candidate.query.all())

@app.route("/votes/new/")
def votes_form():
	return render_template("votes/new.html")

@app.route("/votes/", methods=["POST"])
def votes_create():
	cn = Candidate(request.form.get("name"))
	cp = Candidate(request.form.get("party"))

	db.session().add(cn)
	db.session().add(cp)
	db.session().commit()

	return redirect(url_for("votes_index"))
