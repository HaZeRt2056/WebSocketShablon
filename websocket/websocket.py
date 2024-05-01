# from flask import Flask
# from flask_socketio import SocketIO, emit
#
# app = Flask(__name__)
# socketio = SocketIO(app)
#
# @socketio.on('message')
# def handle_message(message):
#     print('Received message:', message)
#     # Отправка ответа клиенту
#     emit('response', {'data': 'Response from server'})
#
# @socketio.on('qwrety')
# def message(qwrety):
#     print(qwrety)
#
# if __name__ == '__main__':
#     socketio.run(app, allow_unsafe_werkzeug=True)


#emit()


from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('connected', {'status': 'success', 'message': 'You are now connected to the server'})

@socketio.on('message')
def handle_message(message):
    print('Message:', message)
    emit('message', {'orders': message})

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)