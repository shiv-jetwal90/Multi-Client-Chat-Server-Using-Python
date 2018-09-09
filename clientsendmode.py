#client code for private chatting application
import socket
s=socket.socket()
host=input('enter the name of server--')
code=1234
s.connect((host,code))
print('connected  to server')
#flag=1
name0=input("sending mode")
name0=name0.encode('utf-8')
s.send(name0)
name=input("name:-")
name=name.encode('utf-8')
s.send(name)
name1=input("send to personal")
name1=name1.encode('utf-8')
s.send(name1)
#mode=input("1 for sending and 2 for recieving mode")
#s.send(mode.encode('utf-8'))
#print('Enter 1 to send message personal person....','\n','Enter 2 to send message all connected person...')
#x=input()
#s.send(x.encode('utf-8'))
while(1):
	msg=input('>>')
	msg=msg.encode('utf-8')
	s.send(msg)
	i_msg=s.recv(1024)
	i_msg=i_msg.decode()
	print('server says---',i_msg)

	    