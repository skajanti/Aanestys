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
		stmt = text("SELECT Candidate.name, count(Vote.id) FROM Vote LEFT JOIN Candidate ON Vote.candidate_id = Candidate.id GROUP BY Candidate.id").params(done=done)
		
		res = db.engine.execute(stmt)
		
		response = []
		
		for row in res:
			response.append({row[0], row[1]})
		
		return response
