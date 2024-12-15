import tkinter as tk

# 1 criar uma vanela

janela = tk.Tk()
janela.geometry("300x150")
janela.title("Gerencia Frases")

# 2 adicionar um frame

frame = tk.Frame(janela)
frame.pack(padx=10, pady=10, fill='x',expand=True)

# 3 adicionando um label
label = tk.Label(frame, text="Óla Mundo")
label.pack(fill='x', expand=True)

# 4 adiconando o input texto

frase = tk.Label(frame, text="Frase")
frase.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - função para altera o texto

def Click():
    label.config(text=frase_inp.get())


# 6 adicionar botão

button = tk.Button(frame, text="Enviar", command=Click)
button.pack()

janela.mainloop()