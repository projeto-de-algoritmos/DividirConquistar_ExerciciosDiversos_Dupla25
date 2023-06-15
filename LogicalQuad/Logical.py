class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # Verifica se uma das árvores é uma folha
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        
        # Divide as Quad Trees em subárvores
        topLeft1, topRight1, bottomLeft1, bottomRight1 = quadTree1.topLeft, quadTree1.topRight, quadTree1.bottomLeft, quadTree1.bottomRight
        topLeft2, topRight2, bottomLeft2, bottomRight2 = quadTree2.topLeft, quadTree2.topRight, quadTree2.bottomLeft, quadTree2.bottomRight
        
        # Recursivamente aplica o algoritmo nas subárvores
        topLeft = self.intersect(topLeft1, topLeft2)
        topRight = self.intersect(topRight1, topRight2)
        bottomLeft = self.intersect(bottomLeft1, bottomLeft2)
        bottomRight = self.intersect(bottomRight1, bottomRight2)
        
        # Verifica se todos os filhos resultantes são folhas e têm o mesmo valor
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
           topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            return Node(topLeft.val, True, None, None, None, None)  # Cria uma nova folha com o mesmo valor
        else:
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)  # Cria um novo nó interno com valor False
