from flask import Flask

# Creates a Flask application
# Now 'app' is your web application object
# You can add routes to it, configure it, etc.
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p style="font-size: 300px;">Hello, World!</style></p>'