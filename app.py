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
        responses: Returns all the albums.
    """ 

    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
