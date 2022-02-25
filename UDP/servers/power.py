import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5005  # (1024, 65535]
BUFFER_SIZE = 1024

power_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
power_server.bind((UDP_IP, UDP_PORT))
print(f'Power server listening on {UDP_IP}:{UDP_PORT}')
a, address = power_server.recvfrom(BUFFER_SIZE)
if not a:
    raise Exception('Error with the operator a')
print("Address: ", address[0])
print("Port: ", address[1])
print("\nOperator received (a): ", a.decode("UTF-8"))
power_server.sendto("Received".encode("UTF-8"), (address[0], address[1]))

b, address = power_server.recvfrom(BUFFER_SIZE)
if not b:
    raise Exception('Error with the operator b')
print("Operator received (b): ", b.decode("UTF-8"))

power = int(a) ** int(b)
print("Result sent: ", power)
power_server.sendto(str(power).encode("UTF-8"), (address[0], address[1]))

power_server.close()
