from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "Hello developer"


@app.route("/search4", methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))

@app.route('/entry')
def entry_page()-> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the WEB!')

app.run(debug=True)
