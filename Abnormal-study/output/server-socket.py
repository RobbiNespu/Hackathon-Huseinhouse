from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send,emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
    
@socketio.on('backend', namespace='/rekathon')
def backend(data):
    send(data)
    
@socketio.on('frontend', namespace='/rekathon')
def frontend(data):
    emit('frontend', data)
    
if __name__ == '__main__':
    print 'running'
    socketio.run(app, host='0.0.0.0',port = 5001)