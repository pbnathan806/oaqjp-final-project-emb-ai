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

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    print(formatted_response)

    emotionPredictions = formatted_response ['emotionPredictions']

    anger_score =  emotionPredictions['anger']
    print(anger_score)
    disgust_score = emotionPredictions['disgust']
    print(disgust_score)
    fear_score = emotionPredictions['fear']
    print(fear_score)
    joy_score = emotionPredictions['joy']
    print(joy_score)
    sadness_score = emotionPredictions['sadness']
    print(sadness_score)
    print('------------------')

    return response.text  # Return the response text from the API