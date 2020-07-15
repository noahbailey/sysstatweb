#!/usr/bin/env python3

from flask import Flask
from flask import render_template

import os

# Get the system hostname
hostname = os.uname()[1]

# Set up Flask webapp
app = Flask(__name__)

def sysstat(metric): 
    cmd = ""

    if metric == "cpu": 
        cmd = 'sadf -g -- -u'
    elif metric == "load": 
        cmd = 'sadf -g -- -q LOAD'
    elif metric == "mem": 
        cmd = 'sadf -g -- -r'
    elif metric == "io": 
        cmd = 'sadf -g -- -d'
    elif metric == "net": 
        cmd = 'sadf -g -- -n ALL'
    elif metric == "temp": 
        cmd = 'sadf -g -- -m TEMP'
    elif metric == "fan": 
        cmd = 'sadf -g -- -m FAN'

    # If the metric is defined, execute the sar command: 
    if cmd != "": 
        svg = os.popen(cmd).read()
    else: 
        svg = "Metric not found!"

    return svg
    

@app.route("/sysstat/")
def menu(): 
    return render_template('index.html', hostname=hostname )

@app.route("/sysstat/<string:metric>")
def get_metrics(metric): 
    svg = sysstat(metric)
    return svg


if __name__ == "__main__": 
    app.run() 
