import os
import sys
import configparser
from image import makeImage
from imageflow import imageflow
from readtweet import readtweets
from queue import Queue
import subprocess
from getkeys  import getkeys
from flask import Flask
app = Flask(__name__)

@app.route('/starthere/<keyword>')

def getkeyword(keyword):
  keys = getkeys()
  consumer_key = keys[0]
  consumer_secret = keys[1]
  access_key = keys[2]
  access_secret = keys[3]

  line = keyword
  words = line.split(',')
  q = Queue(words)
  video_num = 0
  print(q.isEmpty())
  print(q.length())
  while not q.isEmpty():
    word = q.items[0]
    tImage = "images/"+ str(video_num) + "-%01d.png"
    video = word+".avi"
    tweets = readtweets(word,consumer_key,consumer_secret,access_key,access_secret)
    imageflow(video_num,tweets)
    video_num = video_num+1
    subprocess.call(['ffmpeg','-y', '-framerate', '.1', '-i', tImage, video])
    q.queuedown()
  return keyword
