# Logical OR of Two Binary Grids Represented as Quad-Trees

(Traduzido do inglês)

Uma Matriz Binária é uma matriz na qual todos os elementos são 0 ou 1.

Dadas as quadTree1 e quadTree2. quadTree1 representa uma matriz binária de n * n e quadTree2 representa outra matriz binária de n * n.

Retorne uma Quad-Tree que represente a matriz binária de n * n que é o resultado da operação lógica OU bit a bit das duas matrizes binárias representadas por quadTree1 e quadTree2.

Observe que você pode atribuir o valor de um nó como Verdadeiro ou Falso quando isLeaf é Falso, e ambos são aceitos na resposta.

Uma Quad-Tree é uma estrutura de dados em árvore na qual cada nó interno tem exatamente quatro filhos. Além disso, cada nó possui dois atributos:

val: Verdadeiro se o nó representa uma grade de 1's ou Falso se o nó representa uma grade de 0's.
isLeaf: Verdadeiro se o nó é um nó folha na árvore ou Falso se o nó tem os quatro filhos.
class Node {
public boolean val;
public boolean isLeaf;
public Node topLeft;
public Node topRight;
public Node bottomLeft;
public Node bottomRight;
}

Podemos construir uma Quad-Tree a partir de uma área bidimensional seguindo as seguintes etapas:

Se a grade atual tiver o mesmo valor (ou seja, todos os 1's ou todos os 0's), defina isLeaf como Verdadeiro, val como o valor da grade e defina os quatro filhos como Nulos e pare.
Se a grade atual tiver valores diferentes, defina isLeaf como Falso, val como qualquer valor e divida a grade atual em quatro subgrades, conforme mostrado na imagem.
Recurse para cada um dos filhos com a subgrade apropriada.

Se você quiser saber mais sobre a Quad-Tree, consulte a wiki.

Formato da Quad-Tree:

A entrada/saída representa o formato serializado de uma Quad-Tree usando a travessia em nível, onde nulo significa um terminador de caminho onde nenhum nó existe abaixo.

É muito semelhante à serialização de uma árvore binária. A única diferença é que o nó é representado como uma lista [isLeaf, val].

Se o valor de isLeaf ou val for Verdadeiro, representamos como 1 na lista [isLeaf, val] e se o valor de isLeaf ou val for Falso, representamos como 0.

Exemplo 1:

Entrada: quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
, quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Saída: [[0,0],[1,1],[1,1],[1,1],[1,0]]
Explicação: quadTree1 e quadTree2 são mostradas acima. Você pode ver a matriz binária que é representada por cada Quad-Tree.
Se aplicarmos a operação lógica OU bit a bit nas duas matrizes binárias, obtemos a matriz binária abaixo, que é representada pela Quad-Tree resultante.
Observe que as matrizes binárias mostradas são apenas para ilustração, você não precisa construir a matriz binária para obter a árvore resultante.

Exemplo 2:

Entrada: quadTree1 = [[1,0]], quadTree2 = [[1,0]]
Saída: [[1,0]]
Explicação: Cada árvore representa uma matriz binária de tamanho 11. Cada matriz contém apenas zero.
A matriz resultante também tem tamanho 11 e também contém zero.

Restrições:

quadTree1 e quadTree2 são ambas Quad-Trees válidas, cada uma representando uma grade n * n.
n == 2x, onde 0 <= x <= 9.