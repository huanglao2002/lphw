from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    #greeting = "Hello Jim"
    #return render_template("index.html", greeting=greeting)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()