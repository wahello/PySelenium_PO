import os
from flask import Flask
from flask import Response
app = Flask(__name__)
@app.route('/')
def root():
    return app.send_static_file('index.html')
@app.route('/env')
def env():
    html = "System Environment:\n\n"
    for env in os.environ.keys():
      html += env + ': ' + os.environ[env] + "\n"
    return Response(html, mimetype='text/plain')