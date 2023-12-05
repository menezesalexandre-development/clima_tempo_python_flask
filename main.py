import datetime
import requests
from flask import Flask, render_template, request
from openweathertest import clima_tempo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


app.add_url_rule('/photos/static', endpoint='photos', view_func=app.send_static_file)


@app.route('/', methods=['POST'])
def form_cidade():
    now = datetime.datetime.now()
    time_string = now.strftime('%Y-%m-%d %H:%M')
    template_data = {
        'title': 'Latest Photo',
        'time': time_string
    }
    text = request.form['input_cidade'] + ', BR'
    processed_text = text.capitalize()
    cidade_tempo = clima_tempo(processed_text)
    cidade = cidade_tempo[0]['cidade']
    return render_template('cidade_tempo.html',
                           cidade=cidade,
                           desc_icon=cidade_tempo[0]['desc_icon'],
                           temperatura=cidade_tempo[0]['temperatura'],
                           desc_text=cidade_tempo[0]['desc_text'],
                           umidade=cidade_tempo[0]['umidade'],
                           visibilidade=cidade_tempo[0]['visibilidade'],
                           **template_data)


if __name__ == '__main__':
    app.run(debug=True)
