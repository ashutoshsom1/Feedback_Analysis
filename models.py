from flask_sqlalchemy import SQLAlchemy

# Initialize db instance
db = SQLAlchemy()

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_support = db.Column(db.Integer, nullable=False)
    cleanliness = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    sentiment_score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Feedback {self.id}>"
