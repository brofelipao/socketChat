import tkinter as tk
import socket
import threading


fg = '#FFFFFF'
bg_root = '#1d1d1d'
font = ('Montserrat', 18, 'bold')
fg_button = '#000000'
bg_button = '#28cc89'

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        self.login = tk.Toplevel(background=bg_root)
        self.login.title('Login')
        # Nome
        tk.Canvas(self.login, height=10, bg=bg_root, bd=0, highlightthickness=0, relief='ridge').pack()
        tk.Label(self.login, text='Insira seu nome:', justify=tk.CENTER, font=font, bg=bg_root, fg=fg).pack()
        self.nome = tk.Entry(self.login, justify=tk.CENTER, width=20, font=font, bg=fg, fg=fg_button)
        self.nome.pack()
        # IP
        tk.Canvas(self.login, height=10, bg=bg_root, bd=0, highlightthickness=0, relief='ridge').pack()
        tk.Label(self.login, text='Insira o IP do servidor:', justify=tk.CENTER, font=font, bg=bg_root, fg=fg).pack()
        self.ip = tk.Entry(self.login, justify=tk.CENTER, width=20, font=font, bg=fg, fg=fg_button)
        self.ip.pack()
        # Porta
        tk.Canvas(self.login, height=10, bg=bg_root, bd=0, highlightthickness=0, relief='ridge').pack()
        tk.Label(self.login, text='Insira a porta do servidor:', justify=tk.CENTER, font=font, bg=bg_root, fg=fg).pack()
        self.porta = tk.Entry(self.login, justify=tk.CENTER, width=20, font=font, bg=fg, fg=fg_button)
        self.porta.pack()

        self.aviso = tk.Label(self.login, justify=tk.CENTER, font=font, bg=bg_root, fg="red")
        self.aviso.pack()
        # Botao de entrar
        tk.Canvas(self.login, height=10, bg=bg_root, bd=0, highlightthickness=0, relief='ridge').pack()
        tk.Button(self.login, text='Entrar', font=font, command=self.iniciar_chat, justify=tk.CENTER, bg=bg_button, fg=fg_button).pack()
        tk.Canvas(self.login, height=10, bg=bg_root, bd=0, highlightthickness=0, relief='ridge').pack()
        self.root.mainloop()
    
    def iniciar_chat(self):
        nome = self.nome.get()
        if nome != '' and nome != None:
            try:
                ip = self.ip.get()
                porta = int(self.porta.get())
                self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.socket.connect((ip, porta))
                self.socket.sendall(str.encode(nome))
                self.login.destroy()
                self.chat()
            except:
                self.aviso["text"] = 'Não foi possível conectar ao servidor especificado.'
        else:
            self.aviso["text"] = 'Insira um nome.'

    def chat(self):
        self.root.deiconify()
        self.root.title = ('App de Mensagens')
        self.root.configure(bg=bg_root)
        self.root.geometry('1045x660')
        self.root.maxsize(1045, 660)
        self.root.minsize(1045, 660)

        tk.Label(self.root, bg=bg_root, fg=fg, font=font, text='Chat - Redes').grid(row=0, columnspan=3)
        self.txt = tk.Text(self.root, bg=bg_root, fg=fg, font=font, height=20)
        self.txt.grid(row=1, column=0, columnspan=3)
        scrollbar = tk.Scrollbar(self.txt)
        scrollbar.place(relheight=1, relx=0.985)
        self.message = tk.Entry(self.root, bg=fg, fg=fg_button, font=font, width=70)
        self.message.grid(row=2, column=0)
        self.message.focus()

        loadimage = tk.PhotoImage(file="images/send_button.png").subsample(2, 2)

        send = tk.Button(self.root, image=loadimage, bg=bg_root, border=0, command=self.send_message, activebackground=bg_root, borderwidth=0)
        send.grid(row=2, column=2)
        threading.Thread(target=self.listen_to_server).start()
        self.root.mainloop()

    def send_message(self):
        msg = self.message.get()
        self.message.delete(0, tk.END)
        if msg != None and msg != '':
            self.socket.sendall(str.encode(msg))
    
    def listen_to_server(self):
        while True:
            data = self.socket.recv(1024)
            msg = data.decode()
            self.txt.insert(tk.END, "\n" + msg)

App()