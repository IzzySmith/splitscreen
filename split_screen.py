import re
from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/<session_id>')
def index_session_id(session_id):
   return render_template('follower_side.html')


@app.route('/first_frame')
def first_frame():
   return render_template('first_frame.html')

