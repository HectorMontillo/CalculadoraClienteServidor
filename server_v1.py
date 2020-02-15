import time
import zmq
from math import sqrt

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
    result = eval(message)
    #  Send reply back to client
    socket.send_string(str(result))
