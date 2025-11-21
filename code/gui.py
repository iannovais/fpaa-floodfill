import tkinter as tk

CORES = {
    0: "white",     # livre
    1: "black",     # obstáculo
    2: "red",
    3: "orange",
    4: "yellow",
    5: "green",
    6: "cyan",
    7: "blue",
    8: "purple",
    9: "pink"
}


class InterfaceGrade:
    def __init__(self, grade):
        self.grade = grade
        self.num_linhas = len(grade)
        self.num_colunas = len(grade[0])
        self.tamanho_celula = 40

        self.janela = tk.Tk()
        self.janela.title("Flood Fill - Visualização")

        largura = self.num_colunas * self.tamanho_celula
        altura = self.num_linhas * self.tamanho_celula

        self.tela = tk.Canvas(self.janela, width=largura, height=altura)
        self.tela.pack()

        self.desenhar_grade()

    def desenhar_grade(self):
        self.tela.delete("all")

        for i in range(self.num_linhas):
            for j in range(self.num_colunas):
                cor = CORES.get(self.grade[i][j], "gray")
                x1 = j * self.tamanho_celula
                y1 = i * self.tamanho_celula
                x2 = x1 + self.tamanho_celula
                y2 = y1 + self.tamanho_celula

                self.tela.create_rectangle(x1, y1, x2, y2, fill=cor, outline="gray")

        self.janela.update()

    def executar(self):
        self.janela.mainloop()