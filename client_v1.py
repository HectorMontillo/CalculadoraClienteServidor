import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
quit = False
while not quit:
    print("--------Wellcome--------")
    print("In this calculator you can execute the following operations:")
    print("addintion: x1 + x2")
    print("subtraction: x1 - x2")
    print("division: x1 / x2")
    print("multiplication: x1 * x2")
    print("module: x1 % x2")
    print("power: x1 ** x2")
    print("sqrt(x1)")
    print("-----------------------")
    print("Write a expresion: ")
    expresion = input()
    socket.send_string(expresion)
    #  Get the reply.
    message = socket.recv()
    print("Result from server: %s" % (message.decode("ascii")))
    print("-----------------------")
    print("Continue? (y/n)")
    option = input().lower()
    if(option == 'n' or option == 'no' or option == 'not' or option == '0'):
        quit = True
    print("Good bye!!")
