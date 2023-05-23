import json
import requests

def get_joke(event,context):
    joke_url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(joke_url)
    joke_data = response.json()
    joke = {
        "setup": joke_data['setup'],
        "punchline": joke_data['punchline']
        
    }
    return {
        'statusCode': 200,
        'body' : json.dumps(joke_data),
        'isBase64Encoded': False,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        
    }

