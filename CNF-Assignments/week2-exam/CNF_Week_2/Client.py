import socket
def main():
	host  = '127.0.0.1'
	port = 5000
	s = socket.socket()
	s.connect((host,port))
	message = input("MARK-ATTENDANCE ROLLNUMBER : ")
    while message != 'q':
    	s.send(message.encode())
    	data = s.recv(1024)
    	if(data.decode() == "ROLLNUMBER NOT FOUND"):
    		print("ROLLNUMBER NOT FOUND")
    		break
    	else:
    		print('SECRETQUESTION is : ' + data.decode())
    		answer = input("SECRETANSWER is : ")
    		s.send(answer.encode())
    		result = s.recv(1024).decode()
    		if(result == 'ATTENDANCE-SUCCESS'):
    			print('ATTENDANCE-SUCCESS')
    			break
    s.close()
if __name__ == "__main__":
    main()