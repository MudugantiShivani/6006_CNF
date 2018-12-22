import socket
def Main():
	host  = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    s.listen(10)
    while True:
        c, address = s.accept()
        print ('connection from : '+ str(address))
        initial = 'welcome to guess my number'
        c.send(str(initial).encode())
        threading.Thread(target = Guess, args = (c, address)).start()