from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        return self.searchSubmatrix(matrix, target, 0, 0, m - 1, n - 1)
    
    def searchSubmatrix(self, matrix: List[List[int]], target: int, startRow: int, startCol: int, endRow: int, endCol: int) -> bool:
        if startRow > endRow or startCol > endCol:
            return False
        
        midRow = (startRow + endRow) // 2
        midCol = (startCol + endCol) // 2
        midElement = matrix[midRow][midCol]
        
        if midElement == target:
            return True
        elif midElement > target:
            # Divide a submatriz em quatro partes menores e realiza a recursão em cada uma delas
            return self.searchSubmatrix(matrix, target, startRow, startCol, midRow - 1, midCol - 1) or \
                   self.searchSubmatrix(matrix, target, startRow, midCol, midRow - 1, endCol) or \
                   self.searchSubmatrix(matrix, target, midRow, startCol, endRow, midCol - 1)
        else:
            # Divide a submatriz em quatro partes menores e realiza a recursão em cada uma delas
            return self.searchSubmatrix(matrix, target, startRow, midCol + 1, midRow, endCol) or \
                   self.searchSubmatrix(matrix, target, midRow + 1, startCol, endRow, midCol) or \
                   self.searchSubmatrix(matrix, target, midRow + 1, midCol + 1, endRow, endCol)
