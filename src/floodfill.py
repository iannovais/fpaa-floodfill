from collections import deque
from typing import List, Tuple, Dict

LIVRE = 0
OBSTACULO = 1

Grade = List[List[int]]

def _vizinhos(x: int, y: int, num_linhas: int, num_colunas: int):
    if x > 0:
        yield x - 1, y
    if x + 1 < num_colunas:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y + 1 < num_linhas:
        yield x, y + 1


def preencher_regiao(grade: Grade, inicio_x: int, inicio_y: int, rotulo: int, alvo: int = LIVRE) -> bool:
    if not grade or not grade[0]:
        return False

    num_linhas = len(grade)
    num_colunas = len(grade[0])

    if not (0 <= inicio_y < num_linhas and 0 <= inicio_x < num_colunas):
        return False
    
    if grade[inicio_y][inicio_x] != alvo:
        return False

    fila: deque[Tuple[int, int]] = deque([(inicio_x, inicio_y)])
    grade[inicio_y][inicio_x] = rotulo

    while fila:
        x, y = fila.popleft()
        for nx, ny in _vizinhos(x, y, num_linhas, num_colunas):
            if grade[ny][nx] == alvo:
                grade[ny][nx] = rotulo
                fila.append((nx, ny))
    
    return True

def preencher_todas_regioes(grade: Grade, inicio_x: int, inicio_y: int) -> Grade:
    if not grade or not grade[0]:
        return grade

    def proximo_rotulo(atual: int) -> int:
        return 2 if atual >= 9 else atual + 1

    rotulo = 1
    
    rotulo = proximo_rotulo(rotulo) 
    preencher_regiao(grade, inicio_x, inicio_y, rotulo, alvo=LIVRE)

    for y in range(len(grade)):
        for x in range(len(grade[0])):
            if grade[y][x] == LIVRE:
                rotulo = proximo_rotulo(rotulo)
                preencher_regiao(grade, x, y, rotulo, alvo=LIVRE)
    
    return grade