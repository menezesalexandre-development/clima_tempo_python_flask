import requests
from flask import Flask, render_template
from openweathertest import clima_tempo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
