class Solution(object):

    # Função para dividir o array em grupos de tamanho de 5 
    def dividir_grupos(self, lista):
        grupos = []

        for i in range(0, len(lista), 5):
            # Cada grupo é do ponto do array que parou + 5
            grupo = lista[i:i + 5]
            grupos.append(grupo)

        # Retorna todos os grupos (vários arrays)
        return grupos

    # Função para encontrar a mediana de um grupo 5 (utilizada para encontrar a mediana das medianas do "oráculo")
    def mediana_grupo(self, grupo):
        # Ordena o grupo e pega o meio
        grupo_ordenado = sorted(grupo)
        meio = len(grupo_ordenado) // 2

        # Se for par, a mediana retornada retorna a média entre os 2 do meio
        if len(grupo_ordenado) % 2 == 0:
            return (grupo_ordenado[meio - 1] + grupo_ordenado[meio]) / 2
        # Se for ímpar, retorna apenas o valor no meio
        else:
            return grupo_ordenado[meio]

    # Função para encontrar o k-ésimo maior número (utilizado no exercício KthElement)
    def kth_maior(self, lista, k):

        # Se o K for maior que a lista recebida, retorna nada
        if k > len(lista):
            return None

        # Se a lista for menor que 5, retorna a mediana (antes, ordena)
        if len(lista) <= 5:
            return sorted(lista, reverse=True)[k - 1]

        # Cria grupos e pega as medianas deles
        grupos = self.dividir_grupos(lista)
        medianas_grupos = [self.mediana_grupo(grupo) for grupo in grupos]

        # Encontrar a mediana do "oráculo" de forma recursiva
        mediana_oraculo = self.kth_maior(medianas_grupos, len(medianas_grupos) // 2)

        # Conjuntos da direita/esquerda/iguais
        maiores = [num for num in lista if num > mediana_oraculo]
        menores = [num for num in lista if num < mediana_oraculo]
        iguais = [num for num in lista if num == mediana_oraculo]

        # Se o k for menor que o conjunto da direita (maiores), ele está na direita
        if k <= len(maiores):
            return self.kth_maior(maiores, k)
        # Se o k for maior que o conjunto da direita (maiores) e dos iguais, ele está na esquerda
        elif k > len(maiores) + len(iguais):
            return self.kth_maior(menores, k - len(maiores) - len(iguais))
        # Se não entrar em nenhum dos dois, k é o k-ésimo elemento
        else:
            return mediana_oraculo

    # Função que calcula o XOR para cada posição da matriz e, posteriormente, procura o maior entre eles
    def kthLargestValue(self, matrix, k):
        m, n = len(matrix), len(matrix[0])

        # Calcula o valor XOR para cada coordenada da matriz
        xor_valores = [[0] * n for _ in range(m)]
        xor_valores[0][0] = matrix[0][0]

        # Calcula o valor XOR da primeira coluna
        for i in range(1, m):
            xor_valores[i][0] = xor_valores[i-1][0] ^ matrix[i][0]

        # Calcula o valor XOR da primeira linha
        for j in range(1, n):
            xor_valores[0][j] = xor_valores[0][j-1] ^ matrix[0][j]

        # Calcula o valor XOR restantes
        for i in range(1, m):
            for j in range(1, n):
                xor_valores[i][j] = xor_valores[i-1][j] ^ xor_valores[i][j-1] ^ xor_valores[i-1][j-1] ^ matrix[i][j]

        # Obtem todos os valores de coordenadas em uma lista
        valores_coord = [xor_valores[i][j] for i in range(m) for j in range(n)]

        # Encontra o k-ésimo maior valor usando a função kth_maior
        return self.kth_maior(valores_coord, k)