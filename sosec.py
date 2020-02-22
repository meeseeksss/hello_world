from socket import *
import sys
import threading
host='127.0.0.1'
port=1234
addr=(host,port)
buff=1024
cli=socket(AF_INET,SOCK_STREAM)
cli.connect(addr)

def listen():
    while True:
        data=cli.recv(1024)
        data=data.decode('utf-8')
        print(data.strip())

while True:
    name=input('your name:')
    name=name+'\r\n'
    cli.send(name.encode('utf-8'))
    data=cli.recv(1024)
    data=data.decode('utf-8')
    print(data.strip())
    if data.strip() == 'name used':
        print('bob')
        continue
    t=threading.Thread(target=listen)
    t.start()
    while True:
        a=input('>>>')
        if not a:
            cli.close()
        data='%s\r\n'%a
        cli.send(data.encode('utf-8'))



