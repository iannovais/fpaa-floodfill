from floodfill import preencher_todas_regioes, estatisticas_regioes, LIVRE
from gui import InterfaceGrade
import time
from typing import List, Tuple

def escolher_primeira_livre(grade: List[List[int]]) -> Tuple[int, int]:
    for y, linha in enumerate(grade):
        for x, valor in enumerate(linha):
            if valor == LIVRE:
                return x, y
    return 0, 0


def imprimir_grade(grade: List[List[int]], titulo: str = "Grade"):
    print(f"\n{titulo}:")
    for linha in grade:
        print("  ", end="")
        for valor in linha:
            print(f"{valor:2}", end=" ")
        print()
    print()

def main():
    grade = [
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0],
    ]

    inicio_x, inicio_y = escolher_primeira_livre(grade)
    linhas, colunas = len(grade), len(grade[0])
    print(f"Iniciando flood fill em (x={inicio_x}, y={inicio_y}) tamanho={linhas}x{colunas}")
    
    imprimir_grade(grade, "Grade original")

    gui = InterfaceGrade(grade)
    gui.desenhar_grade()
    gui.janela.update()

    time.sleep(1)

    preencher_todas_regioes(grade, inicio_x, inicio_y)
    
    imprimir_grade(grade, "Grade após flood fill (números = cores)")
    
    stats = estatisticas_regioes(grade)
    print(f"Regiões preenchidas: {len(stats)}")
    for rotulo, tamanho in sorted(stats.items()):
        print(f"  Cor {rotulo}: {tamanho} células")

    gui.desenhar_grade()
    gui.executar()


if __name__ == "__main__":
    main()
