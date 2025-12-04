import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

server_socket = socket.socket()


server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)


while True:
    client_socket, client_address = server_socket.accept()
    request_data = b''
    while True:
        chunk = client_socket.recv(1024)
        request_data += chunk
        if len(chunk) < 1024:
            break
    request_data = request_data.decode('utf-8')
    lines = request_data.split('\n')
    first_line = lines[0]
    parts = first_line.split()
    method = parts[0]
    path = parts[1]
    protocol = parts[2]

    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTTP Request Parser</title>
    </head>
    <body>
        <h1>Распарсенный HTTP запрос</h1>
        <p><strong>Метод:</strong> {method}</p>
        <p><strong>Путь:</strong> {path}</p>
        <p><strong>Протокол:</strong> {protocol}</p>
        <h2>Полный запрос:</h2>
        <pre>{request_data}</pre>
    </body>
    </html>
    '''

    response = 'HTTP/1.1 200 OK\r\n'
    response += 'Content-Type: text/html; charset=utf-8\r\n'
    response += f'Content-Length: {len(html_content.encode("utf-8"))}\r\n'
    response += '\r\n'
    response += html_content

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()
