#Servidor TCP
import socket
import threading

clients = []

class Server():
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket TCP IPV4
        self.socket.bind((host,port)) # conectando ao ipv4
        self.socket.listen()
        print('Aguardando conexões')

        connection = threading.Thread(target=self.get_connected)
        connection.start()

    def wait_message(self, conn, address):
        nome = conn.recv(1024).decode()
        while True:
            try:
                data = conn.recv(1024)
                msg = data.decode()
                msg = f'{nome}: {msg}'.encode()
                if not data:
                    print('Fechando a conexão!')
                    conn.close()
                    break
                for client in clients:
                    client['conn'].sendall(msg)
            except:
                conn.close()
                index = [enum for enum, c in enumerate(clients) if c['endr'] == address][0]
                clients.pop(index)
                break
    def get_connected(self):
        while True:
            conn, endr = self.socket.accept()
            if (len(clients) == 4):
                conn.close()
            else:
                print('Conectado em', endr)
                clients.append({'conn': conn, 'endr': endr})
                threading.Thread(target=lambda: self.wait_message(conn=conn, address=endr)).start()

host = '127.0.0.1' #end. de loopback
port = 50000 #porta do servidor
server = Server(host, port)