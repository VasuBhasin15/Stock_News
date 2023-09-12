from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    url="https://www.businesstoday.in/markets/stocks"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"lxml")
    maindata=soup.find_all("div",class_="widget-listing",limit=6)
    finalnews=""
    for data in maindata:
        news=data.div.div.a["title"]
        finalnews += "\u2022"+" "+news+"\n"
    return render_template("index.html",News=finalnews)
        
