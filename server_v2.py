import time
import zmq
from math import sqrt

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

operands = list()
operations = {'+', '-', '*', '/', '%', '**'}
functions = {'sqrt'}


def is_digit(string):
	try:
		int(string)
		return True
	except ValueError:
		return False


while True:
	flag = False
	#  Wait for next request from client
	message = socket.recv().decode("ascii")
	print("Received request: %s" % message)
	if(message in operations):
		#str(message).join(operands)
		stringOperands = message.join(operands)
		print(stringOperands)
		result = str(eval(stringOperands))
		flag = True
		operands.clear()
	elif(message in functions):
		newOperands = list(map(lambda x: message+'('+x+')', operands))
		print(newOperands)
		resultList = list(map(lambda x: str(eval(x)), newOperands))
		result = ' '.join(resultList)
		flag = True
		operands.clear()
	elif(is_digit(message)):
		operands.append(message)
		result = "The operand has been received: "+message
	else:
		result = "An error has occurred: '"+message + "' is invalid!!, you can continue..."
		
		
	#  Send reply back to client
	socket.send_json({
		"data":result,
		"stop": flag
	})
