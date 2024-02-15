import requests
from flask import Flask, render_template, redirect, url_for, flash,request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html',is_joke = False)

@app.route('/get-joke',methods=['POST','GET'])
def get_joke():
    if request.method =='POST':
        response = requests.get("https://v2.jokeapi.dev/joke/Any", params={'type': 'single'}, verify=False)
        joke = response.json()['joke']
        return render_template('index.html',joke= joke,is_joke =True)






if __name__ == "__main__":
    app.run(debug=True)