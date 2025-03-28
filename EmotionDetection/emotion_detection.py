import requests
import sys 
import json 

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse): 
    inputJson = { "raw_document": { "text": text_to_analyse } }    
    response = requests.post(
        url=URL, 
        headers=Headers, 
        json=inputJson  # Corrected from 'GET' to 'POST'
    )

    if response.status_code == 200:
        # return response.text
        response_data = response.json()
        # text = response_data["emotionPredictions"][0]["emotionMentions"][0]['span']['text']
        emotion = response_data["emotionPredictions"][0]["emotionMentions"][0]['emotion']
        emotion["dominant_emotion"] = ""

        for key, value in emotion.items():  
            if isinstance(value, float) and (len(emotion["dominant_emotion"]) == 0  or value > emotion[emotion['dominant_emotion']]):
                emotion["dominant_emotion"] = key
                # print(emotion['dominant_emotion'])
        outputString = json.dumps(emotion, indent = 4)
        print(outputString)
        return emotion
    else:
        return f"Error: {response.status_code}"


def main(): 
    if len(sys.argv) < 2: 
        print("Usage: emotion_detection.py '<string>'" )
        return
    text_to_analyse = sys.argv[1]
    emotion_detector(text_to_analyse)

if __name__ == "__main__":
    main() 