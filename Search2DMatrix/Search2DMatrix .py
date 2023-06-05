
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Verifica se a matriz ou a primeira linha são vazias
        if not matrix or not matrix[0]:
            return False
        
        # Obtém o número de linhas (m) e colunas (n) da matriz
        m, n = len(matrix), len(matrix[0])
        
        # Inicializa a posição de início na primeira linha e última coluna
        row = 0
        col = n - 1
        
        # Executa um loop enquanto a posição atual estiver dentro dos limites da matriz
        while row < m and col >= 0:
            # Verifica se o elemento atual é igual ao alvo
            if matrix[row][col] == target:
                return True
            # Se o elemento atual for maior que o alvo, move para a coluna anterior
            elif matrix[row][col] > target:
                col -= 1
            # Se o elemento atual for menor que o alvo, move para a próxima linha
            else:
                row += 1
        
        # Se o alvo não for encontrado na matriz, retorna False
        return False

