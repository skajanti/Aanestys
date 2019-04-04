from application import db
from sqlalchemy.sql import text

class Candidate(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144))
	party = db.Column(db.String(32))

	votes = db.relationship("Vote", backref='candidate', lazy=True)

	def __init__(self, name):
		self.name = name

		
	@staticmethod
	def count_votes(done=0):
		stmt = text("SELECT count(Vote.id) FROM Vote LEFT JOIN Candidate ON Vote.candidate_id = Candidate.id GROUP BY Candidate.id").params(done=done)
		
		res = db.engine.execute(stmt)
		
		response = []
		
		for row in res:
			response.append({"count(id)":row[0]})
		
		return response

class Vote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"), nullable=False)
	voter_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
	year = db.Column(db.Integer)

	def __init__(self, candidate_id, voter_id):
		self.year = 0
		self.candidate_id = candidate_id
		self.voter_id = voter_id
