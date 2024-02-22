#import os and dotenv to get api key from .env
import os
from dotenv import load_dotenv

#import requests to make api request
import requests

#create class to return all data
class GetData :
    def __init__ (self) :

        #load all enverimont variables from .env
        load_dotenv()

        #get APIKEY from .env file
        self.API_KEY = os.getenv("API_KEY")


    def getJson (self) :
        #get api data
        apiData = requests.get(f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={self.API_KEY}')

        #transform all data in json
        jsonApiData = apiData.json()

        #return only the articles
        return jsonApiData["articles"]
    