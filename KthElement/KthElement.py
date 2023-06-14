class Solution(object):

    # Função para dividir o array em grupos de tamanho de 5 
    def dividir_cinco(self, lista):
        grupos = []

        for i in range(0, len(lista), 5):
            # Cada grupo é do ponto do array que parou + 5
            grupo = lista[i:(i+5)]
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
            mediana = (grupo_ordenado[meio - 1] + grupo_ordenado[meio]) / 2
            return mediana
        # Se for ímpar, retorna apenas o valor no meio
        else:
            mediana = grupo_ordenado[meio]
            return mediana

    # Função para encontrar o K-ésimo maior
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Se o K for maior que a lista recebida, retorna nada
        if k > len(nums):
            return None

        # Se a lista for menor que 5, retorna a mediana (antes, ordena)
        if len(nums) <= 5:
            return sorted(nums, reverse=True)[k - 1]

        # Cria grupos e pega as medianas deles
        grupos = self.dividir_cinco(nums)
        medianas_grupos = [self.mediana_grupo(grupo) for grupo in grupos]

        # Encontrar a mediana do "oráculo" de forma recursiva
        mediana_oraculo = self.findKthLargest(medianas_grupos, len(medianas_grupos) // 2)

        # Conjuntos da direita/esquerda/iguais
        direita = [num for num in nums if num > mediana_oraculo]
        esquerda = [num for num in nums if num < mediana_oraculo]
        iguais = [num for num in nums if num == mediana_oraculo]

        # Se o k for menor que o conjunto da direita (maiores), ele está na direita
        if k <= len(direita):
            return self.findKthLargest(direita, k)
        # Se o k for maior que o conjunto da direita (maiores) e dos iguais, ele está na esquerda
        elif k > len(direita) + len(iguais):
            return self.findKthLargest(esquerda, k - len(direita) - len(iguais))
        # Se não entrar em nenhum dos dois, k é o k-ésimo elemento
        else:
            return mediana_oraculo