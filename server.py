"""
Emotion Detector Application.

This module sets up a web application with two routes:
- /emotionDetector: Analyzes the emotion of the provided text and returns a response.
- /: Renders the index page of the application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Route to analyze emotion from the text provided in the request."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    final_string = "For the given statement, the system response is "
    for emotion in emotions:
        final_string += f"'{emotion}': {response[emotion]}, "
    final_string = final_string.rstrip(", ")
    final_string += f". The dominant emotion is <b>{response['dominant_emotion']}</b>."
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."
    return final_string



@app.route("/")
def render_index_page():
    """Route to render the index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
