class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # Função auxiliar para contar o número de pares reversos
        def mergeSort(nums, start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end)
            
            # Contagem de pares reversos
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Merge das duas metades ordenadas
            nums[start:end+1] = sorted(nums[start:end+1])
            
            return count
        
        # Chamada inicial do mergeSort
        return mergeSort(nums, 0, len(nums) - 1)

