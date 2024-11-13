import socket

# Configura la dirección y el puerto del servidor
HOST = "127.0.0.1"  # Dirección local (localhost)
PORT = 5000  # Puerto en el que escuchar

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
        print(f"Conexión aceptada desde {client_address}")

        # Maneja la conexión con el cliente en un bloque 'with' para cerrarla automáticamente al finalizar
        with client_socket:
            # Recibe y envía datos en un bucle
            while True:
                data = client_socket.recv(
                    1024
                )  # Tamaño del buffer de recepción en bytes
                if not data:
                    break  # Sale del bucle si el cliente cierra la conexión

                print(f"Mensaje recibido: {data.decode('utf-8')}")

                # Envía una respuesta al cliente
                response = f"Servidor recibió: {data.decode('utf-8')}"
                client_socket.sendall(response.encode("utf-8"))
                print("Respuesta enviada al cliente.")

            print(f"Conexión cerrada con {client_address}")
