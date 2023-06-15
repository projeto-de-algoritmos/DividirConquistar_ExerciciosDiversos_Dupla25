class Solution(object):

    # Função de resolução: encontra a mediana dos 2 arrays
    def findMedianSortedArrays(self, nums1, nums2):
        merge_array = self.merge(nums1, nums2)

        # Se for par, a mediana retornada retorna a média entre os 2 do meio
        if len(merge_array) % 2 == 0:
            return (merge_array[len(merge_array) // 2 - 1] + merge_array[len(merge_array) // 2]) / 2.0
        # Se for ímpar, retorna apenas o valor no meio
        else:
            return merge_array[len(merge_array) // 2]

    # Função padrão de merge
    def merge(self, nums1, nums2):
        merge_array = []
        i = 0
        j = 0

        # Compara os elementos enquanto nenhum dos arrays acabam
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merge_array.append(nums1[i])
                i += 1
            else:
                merge_array.append(nums2[j])
                j += 1

        # Adiciona os elementos restantes de nums1, se houver
        while i < len(nums1):
            merge_array.append(nums1[i])
            i += 1

        # Adiciona os elementos restantes de nums2, se houver
        while j < len(nums2):
            merge_array.append(nums2[j])
            j += 1

        return merge_array