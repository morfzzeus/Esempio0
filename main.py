from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "<h2>Primo Esempio</h2>"

@app.route('/prova')
def prova():
    return "<h2>Pagina della route prova</h2>"


app.run(host = "localhost", debug = True)