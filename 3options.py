import tkinter as tk

def verificar_toggle():
    # Verifica quantos checkbuttons estão selecionados
    if check1_var.get() and check2_var.get():
        # Se os dois primeiros estiverem selecionados, desmarcar o terceiro
        check3_var.set(0)

# Criação da janela
root = tk.Tk()
root.title("Exemplo de Toggle")

# Variáveis para os Checkbuttons
check1_var = tk.IntVar()
check2_var = tk.IntVar()
check3_var = tk.IntVar()

# Criando os Checkbuttons
check1 = tk.Checkbutton(root, text="Toggle 1", variable=check1_var, command=verificar_toggle)
check2 = tk.Checkbutton(root, text="Toggle 2", variable=check2_var, command=verificar_toggle)
check3 = tk.Checkbutton(root, text="Toggle 3", variable=check3_var, command=verificar_toggle)

# Posicionando os Checkbuttons na janela
check1.pack()
check2.pack()
check3.pack()

# Rodando a interface gráfica
root.mainloop()
