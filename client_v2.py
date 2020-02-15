import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
quit = False
print("--------Wellcome--------")
print("In this calculator you must first send the operands one by one and finally the operation:")
print("addintion: x1 x2 +")
print("subtraction: x1 x2 -")
print("division: x1 x2 -")
print("multiplication: x1 x2 *")
print("module: x1 x2 %")
print("power: x1 x2 **")
print("x1 sqrt")
print("-----------------------")
while not quit:

	while True:
		operand = input()
		socket.send_string(operand)
		message = socket.recv_json()
		#print(message)
		print("Replay from server: "+message['data'])
		if(message['stop']):
			break

	print("-----------------------")
	print("Continue? (y/n)")
	option = input().lower()

	if(option == 'n' or option == 'no' or option == 'not' or option == '0'):
		quit = True
		print("Good bye!!")
