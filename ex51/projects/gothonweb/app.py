from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET'])
def index():
    greeting = "Hello Jim"
    #return render_template("index.html", greeting=greeting)
    #name = request.args.get('name')
    #greet = request.args.get('greet', 'hello')
    #name = request.args.get('name', 'Nobody')

    if request.method =="POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":
    app.run()