import socket 

# 1) Crear socket TCP 
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 2) Asociar IP y puerto 
servidor.bind(("127.0.0.1", 8888)) 

# 3) Escuchar conexiones entrantes 
servidor.listen(1) 
print("Servidor TCP esperando conexión en puerto 8888...") 

# 4) Aceptar conexión 
conexion, direccion = servidor.accept() 
print(f"Conexión establecida desde {direccion}") 

# 5) Enviar mensaje al cliente 
conexion.send(b"Hola, cliente. Bienvenido al servidor TCP.\n") 

# 6) Recibir respuesta del cliente 
mensaje = conexion.recv(1024).decode() 
print("Mensaje recibido del cliente:", mensaje) 

# 7) Cerrar conexión 
conexion.close() 
servidor.close() 
print("Conexión cerrada.") 