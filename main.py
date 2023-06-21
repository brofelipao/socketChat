import tkinter as tk

fg = '#FFFFFF'
bg_root = '#1d1d1d'
font = ('Montserrat', 18, 'bold')
bg_button = '#C69749'

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = ('App de Mensagens')
        self.root.geometry('500x420')
        self.root.maxsize(500, 420)
        self.root.minsize(500, 420)
        self.root.configure(bg=bg_root)

        self.margem(10)
        tk.Label(self.root, bg=bg_root, fg=fg, font=font, text='Chat - Redes').pack()

        frame = tk.Frame(self.root, bg=bg_root)
        frame.pack()
        txt = tk.Text(frame, bg=bg_root, fg=fg, font=font, width=60)
        txt.grid(row=1, column=0, columnspan=2)
        scrollbar = tk.Scrollbar(txt)
        scrollbar.place(relheight=1, relx=0.974)
        e = tk.Entry(frame, bg=bg_button, fg=fg, font=font, width=55)
        e.grid(row=2, column=0)
        
        send = tk.Button(frame, text="Enviar", padx=1, pady=20, fg=fg,
            activebackground=bg_button, activeforeground=fg, bg=bg_button, relief=tk.FLAT, font=font)
        send.grid(row=2, column=1)
        tk.mainloop()
    
    def margem(self, altura):
        tk.Canvas(self.root, width=500, height=altura, bg=bg_root, bd=0, highlightthickness=0, relief='ridge').pack()

App()