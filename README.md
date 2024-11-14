

  <h3 align="center">tcp_server</h3>

  <p align="center">
    Servidor TCP
    <br />
    <br />
    <br />
    <!-- <a href="https://service-streaming.onrender.com/">View Demo</a> -->
    ·
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

Esta es una prueba técnica

El objetivo es:
* Crear un servidor TCP
* Enviar un mensaje a traves de un cliente
* El servidor debe responder con el mensaje en mayusculas
* Si el cliente envía DESCONEXION se cierra la conexión con el cliente

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Instalación

1. Clonar el repositorio
  ```sh
   git clone https://github.com/mikelm2020/tcp_server.git
   ```
2. Crear el ambiente virtual
  ```sh
   python3 -m venv .venv
   ```
3. Preparar el ambiente virtual
  ```sh
   source .venv/bin/activate
   ```
   ```sh
   pip install -r requirements.txt
   ```
4. Crear un archivo .env file con las variables de entorno del archivo de ejemplo .env_example

5. Las variables de entorno son usadas para configurar el servidor TCP

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Uso

Las instrucciones para usarlo son:
1. Ejecutar el servidor en una terminal
```sh
   python3 server.py
   ```
2. Ejecutar el cliente en otra terminal
```sh
   python3 client.py
   ```
