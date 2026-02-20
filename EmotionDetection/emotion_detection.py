import requests, json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header) 

    print ("Response code ----------------- {}".format(response.status_code)) 

    emotion = {}

    if response.status_code == 200:
    
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
    
        # Extracting the emotion predictions list from the formatted response dictionary
        emotionPredictions = formatted_response ['emotionPredictions']

        # Extracting the emotion dictionary from the emotion predictions list
        emotion = (emotionPredictions [0])['emotion']

        # Based on the score, adding the dominant emotion to the emotion dictionary  
        emotion ['dominant_emotion'] = max(emotion, key=emotion.get)
    
    elif response.status_code == 400:

        emotion['anger'] = None
        emotion['disgust'] = None
        emotion['joy'] = None
        emotion['sadness'] = None
        emotion['fear'] = None
        emotion['dominant_emotion'] = None
    
    # Returning a dictionary containing emotion detection results
    
    return emotion  # Return the response text from the API