from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    user={"name":"Jeffron", "favGame":"Debugger"}
    return render_template('index.html', user=user)

@app.route('/secret')
def secret():
    return render_template('secret.html')
    
@app.route('/sendBreakfast', methods=["GET", "POST"])
def sendBreakfast():
    if request.method=="GET":
        return "you didnt fill out the form"
    else:
        userData = dict(request.form)
        nickname = userData["nickname"]
        nickname = model.shout(nickname)
        breakfast = userData["breakfast"]
        breakfast = model.shout(breakfast)
        return render_template("breakfast.html", nickname = nickname, breakfast = breakfast)
        