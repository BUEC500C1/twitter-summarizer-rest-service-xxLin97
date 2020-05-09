from flask import Flask, render_template, request, send_file
from flask_restful import reqparse, Api, Resource
import os
import T2V
import mult
import zipfile
app = Flask(__name__)

@app.route('/') #creates the flask html route
def root():
    return render_template('tweet.html')

@app.route('/', methods=['POST'])
def upload():
    N1 = request.form['x1']  
    N2 = request.form['x2']
    N3 = request.form['x3']
    tweet_name=[]
    if N1 !="":
        tweet_name.append(N1)
    if N2 !="":
        tweet_name.append(N2)
    if N3 !="":
        tweet_name.append(N3)
    print(tweet_name)
    queue_mul.Mul_Threads(tweet_name,3)
    print("this is finished")
    zipFolder = zipfile.ZipFile('videos.zip', 'w', zipfile.ZIP_DEFLATED)
    for name in tweet_name:
        video_names = name +'.avi'
        zipFolder.write(video_name)

    zipFolder.close()
    return send_file('videos.zip', mimetype='zip',attachment_filename='videos.zip',as_attachment=True)

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port = 80, debug=True)
