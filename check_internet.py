from socket import *
def ip():
	ip=gethostbyname(gethostname())
	return ip
def internet():
	if ip() =='127.0.0.1':
		return False
	else:
		return True
if internet():
	print('device online')
	print('ip:'+ip())
else:
	print('device offline')
