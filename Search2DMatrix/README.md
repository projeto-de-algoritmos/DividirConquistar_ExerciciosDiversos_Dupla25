# Search a 2D Matrix II

(Traduzido do inglês)

Escreva um algoritmo eficiente que procure por um valor alvo em uma matriz de inteiros m x n chamada "matrix". Esta matriz possui as seguintes propriedades:

Os inteiros em cada linha estão ordenados em ordem crescente da esquerda para a direita.
Os inteiros em cada coluna estão ordenados em ordem crescente de cima para baixo.
Exemplo 1:

Entrada: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Saída: true

Exemplo 2:

Entrada: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Saída: false

Restrições:

m == comprimento da matriz
n == comprimento da matriz[i]
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
Todos os inteiros em cada linha estão ordenados em ordem crescente.
Todos os inteiros em cada coluna estão ordenados em ordem crescente.
-109 <= target <= 109