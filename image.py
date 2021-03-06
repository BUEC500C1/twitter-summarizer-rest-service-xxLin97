"""
from PIL import Image, ImageDraw, ImageFont

def tweet2image(video, image, tweet):
  tweets = tweet.split(" ")
  tw_len = 0
  text_temp = ""
  for tw in tweets:
    tweet_len = tw_len + len(tw) + 1
    if (tweet_len > 60):
      text_temp =  text_temp + "\n"
      tweet_len = 0
    text_temp = text_temp + "" + tw
  print(text_temp)
  text_temp = text_temp.encode('utf-8')


 font = ImageFont.load_default()
 filename = "images/" + str(video) + "-" + str(image) + ".png"
 tw_image = Image.new(mode = "RGB", size = (500,200), color = 'white')
 tweeter = ImageDraw.Draw(tw_image)
 tweeter.text((0,50),txt,fill=(0,0,0),spacing=10,align='left')
 tw_image.save(filename)   

"""

from PIL import Image, ImageDraw, ImageFont


def makeImage(video_num,image_num,tweet): 
  tweets = tweet.split(" ")
  txt = ""
  l = 0
  for t in tweets:
    l = l + len(t) + 1
    if l > 60:
      txt = txt + "\n"
      l = 0
    txt = txt + " "+ t
  print(txt)
  txt = txt.encode('utf-8')



  font = ImageFont.load_default()
  filename = "images/" + str(video_num) + "-" + str(image_num) + ".png"
  image = Image.new(mode = "RGB", size = (600,200), color = 'white')
  tweeter = ImageDraw.Draw(image)
  tweeter.text((0,50),txt,fill=(0,0,0),spacing=10,align='left')
  image.save(filename)

  def makeImages (video_num, tweets):
    image_num = 0;
    for tweet in tweets:
      makeImage(video_num, image_num, tweet)
      image_num += 1