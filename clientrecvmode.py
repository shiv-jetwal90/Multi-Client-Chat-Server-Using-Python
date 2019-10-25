import socket
import time
clients={}
s=socket.socket()
host="172.16.20.144"
#var=socket.gethostbyname("www.google.com")
print("server will start at",host)
port=1234
'''client
host=input("enter the name of  server")
port=1234
#added comment
'''
s.bind((host,port))
print("server created successfully waiting for connection...")
'''s.connect((host,port))
print("connected to server")
'''
i=0
s.listen(1)
#while True:
con,adr=s.accept()
#con2,dr=s.accept()
#	clients[adr]=con
#	print(adr,"is connected to server")
#	i=i+1
while(True):
	msg=input(">")
	msg=msg.encode()
	con.send(msg)
	#con2.send(msg)
	#print("")
	#while(i>0)
	i_msg=con.recv(1024)
	if i_msg=="":
		pass
	else:
		i_msg=i_msg.decode()
		print("client1 says->",i_msg)
	


