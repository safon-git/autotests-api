import socket


def client(message_to_send):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        client_socket.connect(server_address)
        client_socket.send(message_to_send.encode())

        response = client_socket.recv(4096).decode()

        print("--- Ответ от сервера ---")
        print(response)
        print("------------------------")

    except ConnectionRefusedError:
        print("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.")
    finally:
        client_socket.close()


if __name__ == '__main__':
    client("Привет, сервер2323!")