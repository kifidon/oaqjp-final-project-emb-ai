# server.py
"""
Flask server for emotion detection.
Provides a web-based UI and an API for detecting emotions from text.
"""


from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Route to serve the index.html
@app.route('/')
def index():
    """
    Serves the main HTML page.
    
    Returns:
        HTML page rendered from index.html.
    """
    return render_template('index.html')

# API endpoint for emotion detection
@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    API endpoint to detect emotions from text.

    Returns:
        JSON response containing emotion scores and a message.
    """
    if request.method == 'GET':
        text = request.args.get("textToAnalyze")
        emotion_scores = emotion_detector(text)
        if emotion_scores["dominant_emotion"] is None:
            return jsonify({
                "message": "Invalid text! Please try again!",
            }), 400
        emotion_message = (
            f"For the given statement, the system response is "
            f"'anger': {emotion_scores['anger']}, "
            f"'disgust': {emotion_scores['disgust']}, "
            f"'fear': {emotion_scores['fear']}, "
            f"'joy': {emotion_scores['joy']}, "
            f"'sadness': {emotion_scores['sadness']}. "
            f"The dominant emotion is {emotion_scores['dominant_emotion']}."
        )

        return jsonify({"message": emotion_message, "emotion_scores": emotion_scores}), 200
    return jsonify({"message": "Method not allowed", "emotion_scores": emotion_scores}), 400


# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
