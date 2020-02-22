from socketserver import (TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime
import socketserver
import re
import sys

host='127.0.0.1'
port = 1234
addr=(host,port)
name_list={}
names=[]
class MyRequestHandler(SRH):
    def handle(self):
     while True:
        global name_list
        global names
        try:
            name=self.rfile.readline()
        except ConnectionResetError:
            sys.exit()
        name=name.decode('utf-8').strip()
        if name not in names:
            names.append(name)
            print('connected from:',self.client_address,'('+name+')')
            self.wfile.write('ok'.encode('utf-8'))
        else:
            log_error='name used'
            self.wfile.write(log_error.encode('utf-8'))
            continue
        are=self.request
        name_list[are]=name
        des=are
        while True:
            try:
                data=self.rfile.readline()
                option=data.decode('utf-8').strip()
                print(self.client_address,'('+name+')',':'+option+' to',end=' ')
                
                if not option:
                    break
                elif option.startswith('>'):
                    a=re.match('^>(.+)',option)
                    d=a.group(1)
                    print(d)
                    for i in name_list:
                        if d == name_list[i]:
                            des=i
                        else:
                            print('none')
                elif option=='namelist':
                    for i in name_list:
                        self.wfile.write(name_list[i].encode('utf-8'))
                else:
                    f='from:'+name
                    f=f.encode('utf-8')
                    des.send(data+f)
                    print(name_list[des])
                
            except ConnectionResetError:
                names.remove(name)
                del name_list[are]
                break
ser=socketserver.ThreadingTCPServer(addr,MyRequestHandler)
print('waiting for connection')
ser.serve_forever()
