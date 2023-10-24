#!/usr/bin/env python3
### This is a simple flask hello world application ###
# Import modules required for app
import os
from flask import Flask, render_template, request
##### Create a Flask instance
app = Flask(__name__)
##### Define routes #####
@app.route('/')
def home(): 
    return 'Hello, World!'
    #Using template
    #return render_template('default.html',url="home")
##### Run the Flask instance, browse to http://<< Host IP or URL >>:5000 #####
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
