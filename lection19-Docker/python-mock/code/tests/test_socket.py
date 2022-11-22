import requests
from _socket import timeout

import settings


url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'


def test_with_socket_client():
    requests.post(f'{url}/add_user', json={'name': '123'})

    import socket
    import json

    target_host = settings.APP_HOST
    target_port = int(settings.APP_PORT)

    params = '/get_user/123'

    # создаём объект клиентского сокета
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # выставляем ожидание для сокета
    client.settimeout(0.1)

    # устанавливаем соединение
    client.connect((target_host, target_port))

    # создаем и выполняем запрос
    request = f'GET {params} HTTP/1.1\r\nHost:{target_host}\r\n\r\n'
    client.send(request.encode())

    total_data = []

    try:
        while True:
            # читаем данные из сокета до тех пор пока они там есть
            data = client.recv(4096)
            if data:
                print(f'received data: {data}')
                total_data.append(data.decode())
            else:
                break
    except timeout:
        pass

    data = ''.join(total_data).splitlines()
    assert json.loads(data[-1])['age'] > 0
