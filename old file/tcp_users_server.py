import socket
import threading

messages = []
lock = threading.Lock()


def handle_client_connection(client_socket, client_address):
    print(f'Пользователь с адресом: {client_address} подключился к серверу')

    try:
        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        with lock:
            messages.append(data)
            response = '\n'.join(messages)

        client_socket.send(response.encode())

    except ConnectionResetError:
        print(f"Пользователь с адресом: {client_address} неожиданно отключился.")
    finally:
        client_socket.close()
        print(f"Соединение с {client_address} закрыто.")


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")

    while True:
        client_socket, client_address = server_socket.accept()

        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
        client_thread.start()


if __name__ == '__main__':
    server()