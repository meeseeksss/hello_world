from socket import *
#socket
def ip():
	ip=gethostbyname(gethostname())
	return ip
print(ip())
port=1000
ip_port=(ip,port)
cli=socket(AF_INET,SOCK_STREAM)
while True:
	server_ip=input("?")
	server_port=input("!")
	if not server_ip or not server_port:
		cli.close()
	try:
	    cli.connect((server_ip,int(server_port)))
	    print('connected to:'+server_ip+','+server_port)
	except gaierror:
	    continue
	while True:
		data=input('>>>')
		data=data.encode('utf-8')
		if not data:
			break
		cli.send(data)
		data=cli.recv(1024)
		print(data.decode('utf-8'))
			
