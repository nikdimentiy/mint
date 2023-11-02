from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

# Function to log requests and results
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)

# Route for handling POST requests to /search4
@app.route("/search4", methods=['POST'])
def do_search() -> str:
    # Get the 'phrase' and 'letters' parameters from the form data
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    
    # Perform the search using the search4letters function
    results = str(search4letters(phrase, letters))
    
    # Log the request and results
    log_request(request, results)
    
    # Render the results template and pass the data to it
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

# Routes for the root and /entry pages
@app.route("/")
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the WEB!')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
