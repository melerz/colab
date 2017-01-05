from flask import Flask
from flask_socketio import SocketIO, send

appChat = Flask(__name__)
appChat.config['SECRET_KEY']= 'mysecret'
socketio = SocketIO(appChat)


@socketio.on('message')
def handleMessage(msg):
    print('Message: '+msg)
    send(msg,broadcast=True)

#todo run the server
socketio.run(appChat)