from flask import Flask
from flask import render_template

# Creates a Flask application
# Now 'app' is your web application object
# You can add routes to it, configure it, etc.
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p style="font-size: 300px;">Hello, World!</p>'

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
    # Aallows secure external connection on public ip + port 5000.

@app.route('/test')
def test():
    return render_template('test_page.html')