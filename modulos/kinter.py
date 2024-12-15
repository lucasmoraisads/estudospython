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


janela.mainloop()