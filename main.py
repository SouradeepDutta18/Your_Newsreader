import requests
from win32com.client import Dispatch
import json
with open("key.txt","r") as f:
    key = f.read()

def say(str):
 speak = Dispatch("SAPI.SpVoice")
 speak.Speak(str)

news = requests.get(f"http://newsapi.org/v2/top-headlines?country=in&apiKey={key}")  #put your api key in the curly braces.
news = news.json()
articles = news["articles"]
i = 0
for article in articles:
 say(article["title"])
 i+=1

