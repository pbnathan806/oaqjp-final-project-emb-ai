from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the score for different emotions from the response
    joy_score = response['joy']
    anger_score = response['anger']
    disgust_score = response['disgust']
    sadness_score = response['sadness']
    fear_score = response['fear']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the emotional scores and dominant emotion
    

    return "For the given statement, the system response is 'anger': {} , 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger_score,disgust_score,fear_score,joy_score,sadness_score,dominant_emotion)


if __name__ == "__main__":
    app.run(debug= True,host="0.0.0.0", port=5000)