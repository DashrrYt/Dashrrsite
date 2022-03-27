import random 
import flask
from flask import Flask, request, url_for, redirect, render_template, jsonify
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import os
<<<<<<< HEAD
import praw
siteurl = "dashrr.cf"
=======

siteurl = "127.0.0.1:5000"
>>>>>>> 73ae7f9ce6b21138c7c2c5a998e4780de031976a

with open("json/token.json") as f: 
  apitoken = json.load(f)
apikey=apitoken[0]["token"]
print(apikey)
with open("json/8ball.json") as d:
  answer8ball = json.load(d)

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")
<<<<<<< HEAD
@app.route("/donate")
def donate():
  return render_template("donate.html")
=======
>>>>>>> 73ae7f9ce6b21138c7c2c5a998e4780de031976a
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html") 
@app.route("/api/")
def apiList(): 
  return render_template("apilist.html", siteurl=siteurl)
<<<<<<< HEAD

=======
>>>>>>> 73ae7f9ce6b21138c7c2c5a998e4780de031976a
@app.route('/api/v1/8ball', methods=['GET'])
def api8ball(): 
  token = request.args.get("token")
  if token == "0":
<<<<<<< HEAD
    time.sleep(1)
=======
    time.sleep(3)
>>>>>>> 73ae7f9ce6b21138c7c2c5a998e4780de031976a
    return jsonify(random.choice(answer8ball))
  elif token==apikey:
    time.sleep(1)
    return jsonify(random.choice(answer8ball))
  elif token==None: 
    return "No Token Passed"
  else:
    return "Invalid token has been passed"
<<<<<<< HEAD

reddit = praw.Reddit(
  client_id = "cyAr-LQpdSWlmOSQ4IWAoA", 
  client_secret = "Um421poK7wj1milKgiglP8K1CMd9yg", 
  username = "DashrrYT", 
  password = "Vien@123", 
  user_agent = "Catpics by u/DashrrYT"
)

@app.route("/api/v1/cats", methods=["GET"])
def cats(): 
  subreddit = reddit.subreddit("catpics")
  all_subs = []
  top = subreddit.top(limit=420) # bot will choose between the top 250 memes
  for submission in top:
    all_subs.append(submission)
  random_sub = random.choice(all_subs)
  jsonContent = { "title": f"{random_sub.title}", "image_url": f"{random_sub.url}" }
  token = request.args.get("token")
  if token == 0: 
    time.sleep(1)
    return jsonify(jsonContent)
  elif token==apikey: 
    return jsonify(jsonContent)
  elif token==None : 
    return "No token passed"
  else:
    return "invalid token"
=======
>>>>>>> 73ae7f9ce6b21138c7c2c5a998e4780de031976a
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=False)