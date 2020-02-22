from socket import *
def ip():
	ip=gethostbyname(gethostname())
	return ip
print(ip())
port=1001
ser=socket(AF_INET,SOCK_STREAM)
ser.bind((ip(),port))
ser.listen()

while True:
	print('.....')
	cli,addr=ser.accept()
	print('connected')
	
	while True:
		data=cli.recv(1024)
		if not data:
			break
		cli.send(data)
