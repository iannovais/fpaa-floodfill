
# FPAA Flood Fill

## Descrição
Este projeto realiza a implementação e demonstração de um algoritmo Flood Fill para identificação e preenchimento de regiões conectadas em um grid 2D.
Ele tem como objetico, fornecer uma ferramenta simples em Python para detectar e preencher regiões conectadas (componentes) em uma matriz bidimensional, com uma interface mínima para teste e visualização.

## Introdução

## Instruções de Uso e Configuração
- **Requisitos:**
  - Python 3.8+ instalado

- **Como executar:**
  1. Navegue até a pasta do projeto:

	  `cd c:\Users\eduado\Desktop\fpaa-floodfill`

  2. Instale dependências. Este projeto é escrito em Python puro e não tem dependências externas obrigatórias, então normalmente não é necessário instalar pacotes extras.

  3. Para rodar a aplicação principal:

	  `python src\main.py`

  4. Arquivos principais:
	  - `src\floodfill.py` — implementação do algoritmo Flood Fill.
	  - `src\gui.py` — interface mínima para testar/visualizar.
	  - `src\main.py` — arquivo principal do programa.

---

## Explicação do Algoritmo Flood Fill

O algoritmo segue uma abordagem **iterativa baseada em fila (BFS)**, garantindo que cada célula navegável (`0`) seja agrupada de acordo com sua conectividade ortogonal (cima, baixo, esquerda e direita). Obstáculos (`1`) são preservados, e cada região encontrada recebe uma cor numérica distinta (`2–9`).

O funcionamento está organizado em três partes principais: detecção de vizinhos, preenchimento de uma única região e preenchimento completo de todas as regiões do grid.

---

### 1. A função `_vizinhos`

```python
def _vizinhos(x, y, num_linhas, num_colunas):
```

Retorna todos os vizinhos **ortogonais válidos**, respeitando os limites da grade.
Apenas as posições imediatamente adjacentes são consideradas — diagonais não contam como conexão.

**Exemplo: Ponto (2,1) em um grid 5×5:**

- Os vizinhos ortogonais válidos seriam:
   - Esquerda: **(1,1)**
   - Direita: **(3,1)**
   - Cima: **(2,0)**
   - Baixo: **(2,2)**

* Representação visual dos vizinhos:

```
      (2,0)
        ↑
(1,1) ← X → (3,1)
        ↓
      (2,2)
```

---

### 2. A função `preencher_regiao`

Essa função executa o Flood Fill de fato, utilizando uma **fila (deque)** para implementar BFS.

**Passo a passo:**

- Verifica se o grid é válido.
- Verifica se a posição inicial está dentro dos limites.
- Confirma que a célula inicial possui o valor-alvo (`0`).
- Insere essa célula na fila e altera seu valor para o rótulo adequado (a cor da região).
- Enquanto a fila não estiver vazia:
   - remove uma célula atual
   - verifica cada vizinho retornado por `_vizinhos`
   - se o vizinho possui o valor-alvo, ele é pintado e adicionado à fila

* Isso garante que todas as células conectadas e navegáveis sejam preenchidas.

### Exemplo do funcionamento de `preencher_regiao`

**Entrada:**

```
0 0 1
0 1 1
1 1 1
```

**Chamada:**

```python
preencher_regiao(grade, 0, 0, rotulo=2)
```

**Execução:**

- **(0,0)** → é livre **(0)**, então recebe **2**
- Vizinhos ortogonais:
   - **(1,0)** → de **0** → é atualizado para **2**
   - **(0,1)** → de **0** → é atualizado para **2**

* Todos os outros vizinhos são `1` (obstáculo), portanto o preenchimento encerra **nesse ponto**.
* Nenhuma outra célula livre está conectada ao ponto inicial.

**Resultado:**

```
2 2 1
2 1 1
1 1 1
```

- A função retorna `True` indicando que a região foi preenchida.

---

### 3. A função `preencher_todas_regioes`

Essa função coordena o preenchimento global do grid. Ela:

- Define um contador de cor que varia entre **2 e 9**, retornando para 2 após 9.
- Preenche a primeira região a partir da célula inicial.
- Percorre o grid totalmente (linha por linha):
   - toda vez que encontra um `0`, avança para a próxima cor e chama `preencher_regiao` novamente

Com isso:

- cada conjunto de células conectadas recebe um rótulo diferente
- obstáculos (`1`) são preservados
- regiões coloridas (`>= 2`) não são alteradas

### Exemplo completo usando o algoritmo

**Grade inicial:**
```
0 1 0
0 1 0
1 1 1
```

- Primeira célula livre encontrada: **(0,0)**
- Primeira região → recebe a cor **2**:

**Primeira região preenchida:**
```
2 1 0
2 1 0
1 1 1
```

- O algoritmo continua percorrendo o grid e encontra novo `0` em **(2,0)**.
   - Nova cor: **3**

**Segunda região preenchida:**
```
2 1 3
2 1 3
1 1 1
```

- Nenhuma célula livre restante, fim do processo.

---

### 4. A função `estatisticas_regioes`

Essa função percorre o grid e conta quantas células pertencem a cada cor (`>= 2`).

**Exemplo:**
```
2 2 1 3
2 1 1 3
1 4 4 1
```

**Estatísticas:**
```
Cor 2 → 3 células
Cor 3 → 2 células
Cor 4 → 2 células
```

---

### 5. Visualização com Tkinter (GUI)

O módulo `InterfaceGrade` exibe o grid visualmente:

- cada célula é desenhada como um retângulo colorido
- as cores seguem o dicionário `CORES`
- a interface é atualizada a cada alteração no grid

**Exemplo de conversão:**
```
2 2 1 3 3
```

- Representação visual:
```
🟥 🟥 ⬛ 🟧 🟧
```
---

### 6. Execução principal (MAIN.PY)

O arquivo `main` integra todas as partes do projeto:

**1.** Carrega o grid inicial.
**2.** Encontra a primeira célula livre.
**3.** Exibe o grid original no terminal.
**4.** Inicia a interface gráfica.
**5.** Executa `preencher_todas_regioes`.
**6.** Mostra o grid final.
**7.** Exibe estatísticas de cada região.
**8.** Atualiza a interface para mostrar o resultado colorido.

**Exemplo de saída no terminal:**
```
Regiões preenchidas: 5
Cor 2: 10 células
Cor 3: 7 células
Cor 4: 12 células
...
```
---
