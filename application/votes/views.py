from application import app, db
from flask import redirect, render_template, request, url_for
from application.votes.models import Candidate

@app.route("/votes", methods=["GET"])
def votes_index():
	return render_template("votes/list.html", votes = Candidate.query.all())

@app.route("/votes/new/")
def votes_form():
	return render_template("votes/new.html")

@app.route("/votes/<candidate_id>/", methods=["POST"])
def votes_set_party(candidate_id):

	p = Candidate.query.get(candidate_id)
	p.party = request.form.get("party")
	db.session().commit()

	return redirect(url_for("votes_index"))

@app.route("/votes/", methods=["POST"])
def votes_create():
	c = Candidate(request.form.get("name"))

	db.session().add(c)
	db.session().commit()

	return redirect(url_for("votes_index"))
