from flask import Flask
import socket
import os
app = Flask(__name__)
author = os.environ['AUTHOR']
uuid = os.environ['UUID']

@app.route('/hostname')
def getHostname():
    return socket.gethostname()

@app.route('/author')
def getAuthor():
    return author

@app.route('/id')
def getUUID():
    return uuid

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)