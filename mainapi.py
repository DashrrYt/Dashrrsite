import random 
import flask
from flask import Flask, request, url_for, redirect, render_template, jsonify
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import os

siteurl = "127.0.0.1:5000"

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
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html") 
@app.route("/api/")
def apiList(): 
  return render_template("apilist.html", siteurl=siteurl)
@app.route('/api/v1/8ball', methods=['GET'])
def api8ball(): 
  token = request.args.get("token")
  if token == "0":
    time.sleep(3)
    return jsonify(random.choice(answer8ball))
  elif token==apikey:
    time.sleep(1)
    return jsonify(random.choice(answer8ball))
  elif token==None: 
    return "No Token Passed"
  else:
    return "Invalid token has been passed"
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=False)