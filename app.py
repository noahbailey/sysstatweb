#!/usr/bin/env python3

from flask import Flask
from flask import render_template

import os

# Get the system hostname
hostname = os.uname()[1]

# Set up Flask webapp
app = Flask(__name__)

def sysstat(metric): 

    # List of sar(1) options
    cmds = {
        'cpu'   : '-u', 
        'load'  : '-q LOAD', 
        'mem'   : '-r', 
        'io'    : '-d', 
        'net'   : '-n ALL', 
        'temp'  : '-m TEMP', 
        'fan'   : '-m FAN'
    }

    # When the metric is validated, run the sar command 
    if metric in cmds: 
        svg = os.popen("sadf -T -g -O showtoc,skipempty -- " + cmds[metric]).read()
    else: 
        svg = "<h1>Metric not found!</h1><p>Please try another metric type...</p>"
    return svg
    

@app.route("/sysstat/")
def menu(): 
    return render_template('index.html', hostname=hostname )

@app.route("/sysstat/<string:metric>")
def get_metrics(metric): 
    return sysstat(metric)


if __name__ == "__main__": 
    app.run() 
