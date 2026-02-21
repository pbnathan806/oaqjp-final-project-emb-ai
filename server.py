"""A brief summary of the module's purpose.

This module provides functions for running a specific server, handling client
connections, processing requests, and managing data flow.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """ Renders the main index page of the application."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    """ Retrieves the text to analyze from the request arguments."""
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is not None:
        # Extract the score for different emotions from the response
        joy_score = response['joy']
        anger_score = response['anger']
        disgust_score = response['disgust']
        sadness_score = response['sadness']
        fear_score = response['fear']
        dominant_emotion = response['dominant_emotion']
        # Return a formatted string with the emotional scores and dominant emotion
        result = (
            f"For the given statement, the system response is 'anger': {anger_score}, "
            f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
            f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
)
        return result
    return "Invalid text! Please try again."


if __name__ == "__main__":
    app.run(debug= True,host="0.0.0.0", port=5000)
