import os
from flask import Flask
from flask import Response
app = Flask(__name__)
@app.route('/')
def root():
<<<<<<< HEAD
    return app.send_static_file('Pyselenium.html')
=======
    return app.send_static_file('index.html')
>>>>>>> d6a5c0c5b7d6f7fbf57825d2808891e4b87bb4b7
@app.route('/env')
def env():
    html = "System Environment:\n\n"
    for env in os.environ.keys():
      html += env + ': ' + os.environ[env] + "\n"
    return Response(html, mimetype='text/plain')