'''
Use  NewsAPI and the requests module to fetch the daily news related to diferrnt topics.
and explore the various options to build you application
'''
import requests
import json

query=input("what type of news are you interseted in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-04-02&sortBy=publishedAt&apiKey=5c1a46cae3c44287ac88b0c4cef3cc35"

r=requests.get(url)
news=json.loads(r.text)
#print(news,type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("_________")


