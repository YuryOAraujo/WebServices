import socket
import json
import random

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = client_socket.recv(1024)
json_object = json.loads(message)

for data in json_object:
    print(f"{data['name']} {data['classID']} ({data['year']})")
    
    leader = random.choice(data['studentList'])    
    leader_json = json.dumps(leader)
    
    for student in data['studentList']:
        print(f"- {student['name']}, {student['age']} anos, matrícula {student['registrationNumber']}")
    
    print(f"Lider: {leader['name']}, {leader['age']} anos, matrícula {leader['registrationNumber']}")
    
    client_socket.send(leader_json.encode())    
    client_socket.send('\n'.encode())    
    print("\n")

client_socket.close()
