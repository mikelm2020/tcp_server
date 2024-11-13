import os
import socket

from dotenv import load_dotenv

load_dotenv()

# Configura la dirección y el puerto del servidor
HOST = os.getenv("HOST")  # Dirección local (localhost)
PORT = int(os.getenv("PORT"))  # Puerto en el que escuchar

# Crea el socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Permite reutilizar el mismo puerto sin esperar
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Asocia el socket a la dirección y puerto especificados
    server_socket.bind((HOST, PORT))

    # Configura el socket para escuchar conexiones entrantes
    server_socket.listen()
    print(f"Servidor TCP escuchando en {HOST}:{PORT}...")

    # Acepta conexiones entrantes en un bucle
    while True:
        # Acepta una nueva conexión
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada desde el Cliente {client_address}")

        # Maneja la conexión con el cliente en un bloque 'with' para cerrarla automáticamente al finalizar

        with client_socket:
            # Recibe y envía datos en un bucle
            while True:
                data = client_socket.recv(
                    1024
                )  # Tamaño del buffer de recepción en bytes

                if not data:
                    break  # Sale del bucle si el cliente cierra la conexión

                message = data.decode("utf-8").strip()
                print(f"Mensaje recibido: {message}")

                # Verifica si el mensaje es DESCONEXION
                if message == "DESCONEXION":
                    print(
                        "Recibido mensaje de desconexión. Cerrando la conexión con el cliente."
                    )
                    break

                # Convierte el mensaje a mayúsculas y Envía una respuesta al cliente
                response = message.upper()
                client_socket.sendall(response.encode("utf-8"))
                print(f"Servido responde: {response} CLIENTE")

            print(f"Conexión cerrada con Cliente {client_address}")
