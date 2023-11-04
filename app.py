from flask import Flask, render_template

import pandas as pd 
import json 
import plotly
import plotly.express as px 





app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def Home():
    return render_template("home.html", title="Catfish Coders")

@app.route("/About_ACAP", methods = ['GET', 'POST'])
def About_ACAP():
    active_page = "about"
    return render_template("about.html", title="Catfish Coders", active_page=active_page)

@app.route("/The_Problem", methods = ['GET', 'POST'])
def The_Problem():
    active_page = "problem"
    return render_template("problem.html", title="Catfish Coders", active_page=active_page)

@app.route("/Data", methods = ['GET', 'POST'])
def Data():
    active_page = "data"
    df = px.data.Trial()
    figl = px.bar(df x = "MonitoringLocationID")

    return render_template("data.html", title="Catfish Coders", active_page=active_page, title="Home")
 

if __name__ == '__main__':
   app.run(debug = True)


