import socket 

# 1) Crear socket TCP 
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 2) Conectarse al servidor 
cliente.connect(("127.0.0.1", 8888)) 
print("Conectado al servidor.") 

# 3) Recibir mensaje del servidor 
mensaje = cliente.recv(1024).decode() 
print("Mensaje del servidor:", mensaje) 

# 4) Enviar respuesta 
cliente.send(b"Gracias, servidor. Conexion exitosa.\n") 

# 5) Cerrar conexión 
cliente.close() 
print("Cliente desconectado.") 