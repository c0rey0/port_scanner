import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('77.222.153.190',3389))
if result == 0:
   print("Port is open")
else:
   print("Port is not open")
sock.close()