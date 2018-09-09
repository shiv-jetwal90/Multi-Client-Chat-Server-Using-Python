import sys
import socket               # Import socket module
from _thread import *
import threading
s = socket.socket()         
host = '172.16.20.144' 
port = 1234 
data = "" 
data1=" "
fla=0	
flag=0
name=[]
sd=[]
first=0
def on_new_client(conn,addr):
	global data
	global flag
	global fla
	global data1 
	global first
	temp=1
	nm=conn.recv(1024)
	nm=nm.decode()
	sd.append(nm)
	dat=conn.recv(1024)
	dat=dat.decode()
	if dat=="1":
		while True:
			if first == 0:
				if temp==1 and flag == 0:
					lock.acquire()
					data=conn.recv(1024)
					data=data.decode()
					print(data)  
					lock.release()
					temp=0
					flag=1
					first=1
			elif first == 2:
				if temp==1 and flag == 0:
				    lock.acquire()
				    data=conn.recv(1024)
				    data=data.decode()
				    print(data)  
				    lock.release()
				    temp=0
				    flag=1
				elif temp == 0 and flag == 0:
					conn.send(data.encode('utf-8'))
					temp=1
	elif dat=="2":
		lock.acquire()
		data1=conn.recv(1024)
		data1=data1.decode()
		lock.release()
		fla=1


def on_new_client1(conn1,addr):
	global data
	global flag
	global fla
	global data1
	global firs
t	tempp=0
	nm=conn1.recv(1024)
	nm=nm.decode()
	sd.append(nm)
	name.append(conn1)
	dt=conn1.recv(1024)
	dt=dt.decode()
	if dt=="1":
		while True:
			if tempp==0 and flag==1 and first==1:
				print("xx")
				st=data.split(":")
				print(st[1])
				if st[0] in sd:
					conn1.send(st[1].encode('utf-8'))
					tempp=1
				else:
					print("name not found")
					break
			elif tempp == 0 and flag == 1 and first == 2:
				conn1.send(data.encode('utf-8'))
				tempp=1
			elif tempp==1:
				lock.acquire()
				data=conn1.recv(1024)
				data=data.decode()
				print(data)
				lock.release()
				tempp=0
				flag=0
				first=2
	else:
		while True:
			if fla==1:
				for i in name:
					print(i)
					i.send(data1.encode('utf-8'))
			fla=0



		

lock=threading.Lock()
print ('Server started!')
print ('Waiting for clients...')
s.bind((host, port))        
s.listen(5)                  
print ('Got connection from')
while True:
    c, addr = s.accept()
    print("connected with"+addr[0]+":"+str(addr[1]))
    x=c.recv(1024)
    x=x.decode()
    if x=='1':
    	start_new_thread(on_new_client,(c,addr))
    elif x=='2':
    	start_new_thread(on_new_client1,(c,addr))


s.close()
