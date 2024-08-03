
import json
import requests


def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)  
    formatted_response = json.loads(response.text)
    emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    emotion_scores = {}
    if response.status_code == 200:
        
        emotion_scores = {emotion: formatted_response['emotionPredictions'][0]['emotion'][emotion] for emotion in emotions}
        v = list(emotion_scores.values())
        dominant_emotion = emotions[v.index(max(v))]
    
        emotion_scores['dominant_emotion'] = dominant_emotion

    elif response.status_code == 400:
        
        emotion_scores = {emotion: None for emotion in emotions}
       
        emotion_scores['dominant_emotion'] = None


    return emotion_scores