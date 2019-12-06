import socket

#create a new socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Error While Creaing Socket",err)

#Reserve port
port=80

#Get ip of google.com
try:
    ip=socket.gethostbyname('www.google.com')

    s.connect((ip,port))
    print("Socket Succesfully Created  Socket on ",ip  )
except socket.gaierror as err:
    print("Cant resolve Host : " ,err)
