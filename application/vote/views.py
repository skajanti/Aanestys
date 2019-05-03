from application import app, db, login_required
from application.candidate.models import Candidate
from application.vote.models import Vote
from application.election.models import Election

from flask import redirect, render_template, url_for
from flask_login import current_user


@app.route("/candidates/<candidate_id>/vote/", methods=["POST"])
@login_required(role="ANY")
def cast_vote(candidate_id):
    year = db.session().query(Election.year).filter(Election.active.is_(True))

    if not year:
        v = Vote(candidate_id, current_user.id, year)

        db.session().add(v)
        db.session().commit()

    return redirect(url_for("votes_index"))


@app.route("/votes_count", methods=["GET"])
def votes_count():
    y = db.session().query(Election.year).filter(Election.active.is_(True))

    if not y:
        year = int(str(db.session().query(Election.year).filter(Election.active.is_(True)).first())[1:][:4])

        return render_template("vote/vote_count.html", votes = Candidate.query.all(), vote_count=Candidate.count_votes(year))

    return redirect(url_for("index"))