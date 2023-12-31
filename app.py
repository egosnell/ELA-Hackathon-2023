from flask import Flask, render_template, request

import pandas as pd 
import json 
import plotly
import plotly.express as px 


app = Flask(__name__, static_url_path='/static')

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
    title = "The Problem ACAP Faces"
    return render_template("problem.html", title="Catfish Coders", active_page=active_page, page_title=title)

@app.route("/Discussion", methods = ['GET', 'POST'])
def Discussion():
    active_page = "discussion"
    return render_template("discussion.html", title="Catfish Coders", active_page=active_page)

@app.route("/Thread1", methods = ['GET', 'POST'])
def Thread1():
    active_page = "thread1"
    return render_template("thread1.html", title="Catfish Coders", active_page=active_page)
if __name__ == '__main__':
   app.run(debug = True)

@app.route("/Thread2", methods = ['GET', 'POST'])
def Thread2():
    active_page = "thread2"
    return render_template("thread2.html", title="Catfish Coders", active_page=active_page)
if __name__ == '__main__':
   app.run(debug = True)


@app.route("/Data", methods=['GET', 'POST'])
def Data():
    active_page = "data"
    site_list = [];
    if request.method == 'POST':
        for s in ['LorneUp','LorneDown','StRestUp','StRestDown','SouthBayUp','SouthBayDown','INUP','INDN',
                  'MCUP','MCDN','LittleRiverUp','LittleRiverDown','HazenCreekUp','RedHeadMarsh']:
            site = request.form.get(s)
            if site != None:
                print(site)
                site_list.append(site)

    # Ensure site_list is always defined
    if not site_list:
        site_list = []

    return render_template("data.html", title="Catfish Coders", active_page=active_page, site_list=site_list)

if __name__ == '__main__':
   app.run(debug = True)

