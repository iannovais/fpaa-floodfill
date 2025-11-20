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