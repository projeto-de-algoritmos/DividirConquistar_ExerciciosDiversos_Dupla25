# Reverse Pairs

(Traduzido do inglês)

Dado um array de inteiros nums, retorne o número de pares invertidos no array.

Um par invertido é um par (i, j) onde:

0 <= i < j < tamanho de nums e
nums[i] > 2 * nums[j].

Exemplo 1:

Entrada: nums = [1,3,2,3,1]
Saída: 2
Explicação: Os pares invertidos são:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Exemplo 2:

Entrada: nums = [2,4,3,5,1]
Saída: 3
Explicação: Os pares invertidos são:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

Restrições:

1 <= tamanho de nums <= 5 * 104
-231 <= nums[i] <= 231 - 1