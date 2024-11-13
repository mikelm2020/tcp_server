import os
import socket

from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")  # Dirección del servidor
PORT = int(os.getenv("PORT"))  # Puerto del servidor


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    client_socket.sendall(b"Hola servidor")
    data = client_socket.recv(1024)
    print(f'Cliente envía: {data.decode("utf-8")}')

    client_socket.sendall(b"DESCONEXION")
    print("Mensaje de desconexión enviado.")
