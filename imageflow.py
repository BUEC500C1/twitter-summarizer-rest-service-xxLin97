
from image import makeImage

def imageflow (video, tweets):
  image = 0;
  for tweet in tweets:
    makeImage(video, image, tweet)
    image += 1