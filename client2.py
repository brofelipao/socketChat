import socket
import threading


class Cliente():
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #com o secket criado vamos solicitar uma conexão
        self.socket.connect((host,port))

        threading.Thread(target=self.listen_to_server).start()
        threading.Thread(target=self.send_message).start()
    
    def send_message(self):
        nome = input('Digite seu nome: ')
        while nome == "" or nome == None:
            nome = input('Inválido! Digite seu nome: ')
        msg=str.encode(nome)
        self.socket.sendall(msg)
        while msg !='\x18':
            msg = input()
            self.socket.sendall(str.encode(msg))
        self.socket.close()

    def listen_to_server(self):
        while True:
            data = self.socket.recv(1024)
            print(data.decode())

host = '127.0.0.1' #endereço do servidor
port = 50000 #porta do servidor

Cliente(host, port)