#!/usr/bin/env python3
### This is a simple flask hello world application ###
# Import modules required for app
import os
from datetime import datetime
from flask import Flask, render_template, request
##### Create a Flask instance
app = Flask(__name__)
##### Define routes #####
@app.route('/')
def home(): 
    # RET_TEXT = 'Hello, World! ' + os.getenv('AAA','DefaultSSSS-AAA')
    # 現在の時刻を取得
    now = datetime.now()
    # 時刻を24時間表記の文字列にフォーマット
    time_24hr = now.strftime('%H:%M:%S')
    # POD nameを取得
    pod_name = request.headers.get('Pod-Name', 'Unknown Pod')

    RET_TEXT = time_24hr + ' Hello, World! ' + pod_name
    return RET_TEXT
    #return 'Hello, World!' 
    ### Using template
    #return render_template('default.html',url="home")
##### Run the Flask instance, browse to http://<< Host IP or URL >>:5000 #####
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
