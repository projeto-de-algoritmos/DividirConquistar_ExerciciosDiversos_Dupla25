class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # Se uma das árvores for uma folha, retorna a árvore que é uma folha e tem o valor True,
        # ou a outra árvore se a folha tiver valor False.
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        else:
            # Recursivamente chama a função intersect para cada um dos quatro filhos de quadTree1 e quadTree2.
            topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            
            # Se todos os quatro filhos forem folhas e tiverem o mesmo valor, cria uma nova folha com esse valor e retorna.
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
               topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                # Caso contrário, cria um novo nó interno com valor False e os quatro filhos resultantes das chamadas recursivas.
                return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
