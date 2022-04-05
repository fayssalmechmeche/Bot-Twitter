
from cgitb import text
from urllib import response
import tweepy
import config
import json
import os
import sys
import time
import keep_alive
from datetime import datetime
import mysql.connector

keep_alive.keep_alive()

consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 


client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAP5gbAEAAAAAl%2FVec0ozYRE9xcA9%2BjM6gQIc0Bc%3DdAHfhbDjXjEvIF2X7jZPNKYpmp4VUskCRs7Q4GqHQnl17HwcTk',
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)
# Replace the text with whatever you want to Tweet about


def bot():
  try :
    # Connectez- vous à la base de données.
    db = mysql.connector.connect(host='mysql-mechmeche.alwaysdata.net',
                             user='mechmeche',
                             password='93220fat',                             
                             database='mechmeche_bot')
    print ("connect successful!!") 
  except :
    print("raté")
    
 
  
          
  tweetss = 0
  searchs = 0
  limitTweets = 300
  limitSearchs = 180
  stop = False
  while(not stop):
      try:
          tweets = client.search_recent_tweets(
              query='quoi',  max_results=100)
          searchs += 1
          for tweet in tweets.data:
              texte = str(tweet.text).split(' ')
              last = texte[-1]
              if str(tweet).endswith('quoi'):
                  reponse = client.create_tweet(
                      in_reply_to_tweet_id=tweet.id, text='Salut est-ce que tu peux RT et FAV le tweet cela me permettra de trouver une alternance pour mon école https://twitter.com/Fysslisback/status/1495498502591373318?s=20&t=XWFK8T6OHWCSSrU8Qxcuxw')
                  user = tweet.get_user(tweet.id)
                  print('ok')
                  cur = db.cursor()
                  sql = "INSERT INTO Tweet (idtweet, message,pseudo) VALUES (%s, %s,%s)"
                  value = (tweet.id,tweet.text,user.name)
                  cur.execute(sql, value)
                  db.commit()
                  print(cur.rowcount, "ligne insérée.")
                  print(str(datetime.now()))
                  tweetss += 1
      except:
          print("Erreur (probablement de quota, on arrete)")
          stop = True
      if(searchs >= limitSearchs):
          print("Limite atteinte des searchs")
          stop = True
      print(f"On a tweeté {str(tweetss)} fois !")
      time.sleep(5)
  print("Fini, on attend 1H maintenant et on reprend.")
  time.sleep(3800)
  bot()
bot()
