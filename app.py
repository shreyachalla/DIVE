#!flask/bin/python
import sys, os, flask

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask import render_template, redirect


app = Flask(__name__, static_url_path="")


@app.route('/', methods=['GET'])
def home_page():
    """ Home page route.
    get:
        description: Endpoint to return home page.
    """ 

    return render_template('index.html')

@app.route('/process_input_form', methods=['POST'])
def process_input_form(): 
    """ Input form route.
    post:
        description: Print out the inputs chosen by user.
    """ 
    supportingTool = request.form['supportingTool']
    model = request.form['modelOptions']
    optimizations = request.form.getlist('optimizations')
    hw_system = request.form['system']
    return f"Selected options: {supportingTool}: {model}, {hw_system}, {', '.join(optimizations)}"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
