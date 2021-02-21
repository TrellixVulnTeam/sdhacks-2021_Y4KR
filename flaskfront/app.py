from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/test')

def test():

    message = {'greeting':'Hello from Flask!'}
    return jsonify(message)  # serialize and use JSON headers
