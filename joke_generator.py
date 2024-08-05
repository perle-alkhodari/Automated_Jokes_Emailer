import os
from dotenv import load_dotenv
import requests

load_dotenv()


class JokeGenerator:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        self.endpoint = "https://api.api-ninjas.com/v1/jokes"
        self.headers = {
            "X-Api-Key": api_key
        }

    def get_joke(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        data = response.json()
        joke = data[0]["joke"]
        return joke
