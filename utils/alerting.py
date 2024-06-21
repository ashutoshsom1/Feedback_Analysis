def check_alerts(feedback):
    if feedback.customer_support < 2 or feedback.cleanliness < 2:
        print(f"Alert: Low rating detected. Feedback ID: {feedback.id}")
    
    if feedback.sentiment_score < -0.5:
        print(f"Alert: Negative sentiment detected. Feedback ID: {feedback.id}")
