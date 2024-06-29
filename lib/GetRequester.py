import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
        pass

    def load_json(self):
        result = []
        responses = json.loads(self.get_response_body())
        
        for response in responses:
            result.append(response)
        return result
        pass

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()