from application import db
from sqlalchemy.sql import text


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"), nullable=False)
    voter_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    election_year = db.Column(db.Integer, db.ForeignKey("election.year"), nullable=False)

    def __init__(self, candidate_id, voter_id, year):
        self.election_year = year
        self.candidate_id = candidate_id
        self.voter_id = voter_id

    @staticmethod
    def has_voted(user_id, year):
        stmt = text("SELECT id FROM Vote WHERE voter_id = :user_id "
                    "AND election_year = :year").params(user_id = user_id, year = year)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({row[0]})

        if response is not None:
            return True
        else:
            return False
