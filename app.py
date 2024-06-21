from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from utils.sentiment_anlaysis import analyze_sentiment
from utils.alerting import check_alerts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\ashutosh.somvanshi\Feedback_analysis\Feedback_Analysis\feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models after initializing db to avoid circular import issues
# 

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_support = db.Column(db.Integer, nullable=False)
    cleanliness = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    sentiment_score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Feedback {self.id}>"



# 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    customer_support = int(request.form['customerSupport'])
    cleanliness = int(request.form['cleanliness'])
    comments = request.form['comments']
    
    sentiment_score = analyze_sentiment(comments)
    feedback = Feedback(
        customer_support=customer_support,
        cleanliness=cleanliness,
        comments=comments,
        sentiment_score=sentiment_score,
        created_at=datetime.now()
    )
    
    db.session.add(feedback)
    db.session.commit()
    
    check_alerts(feedback)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        app.run(debug=True)
