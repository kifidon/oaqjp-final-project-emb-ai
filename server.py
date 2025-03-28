# server.py

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Route to serve the index.html
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for emotion detection
@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    if request.method == 'GET':
    
        text = request.form['text']

        if not text or text.strip() == "":
            return jsonify({
                "message": "Invalid text! Please try again!",
                "emotion_scores": {
                    "anger": None,
                    "disgust": None,
                    "fear": None,
                    "joy": None,
                    "sadness": None,
                    "dominant_emotion": None
                }
            }), 400 

        emotion_scores = emotion_detector(text)

        if emotion_scores["dominant_emotion"] is None:
            return jsonify({
                "message": "Invalid text! Please try again!",
            }), 400  

        
        emotion_message = f"For the given statement, the system response is 'anger': {emotion_scores['anger']}, 'disgust': {emotion_scores['disgust']}, 'fear': {emotion_scores['fear']}, 'joy': {emotion_scores['joy']} and 'emotion_scores': {result['sadness']}. The dominant emotion is {emotion_scores['dominant_emotion']}."

        return jsonify({"message": emotion_message, "emotion_scores": emotion_scores}), 200


# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)