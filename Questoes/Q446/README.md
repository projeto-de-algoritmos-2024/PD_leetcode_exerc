## 115. Distinct Subsequences

### Enunciado:
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

- For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
- For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

- For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

The test cases are generated so that the answer fits in 32-bit integer.

### Exemplo 1
>**Input:** nums = [2,4,6,8,10]
>**Output:** 7

### Exemplo 2
>**Input:** nums = [7,7,7,7,7]
>**Output:** 16

#### Entradas e saídas obtidas:

Codigo de teste:
<br>

![TestesRodados](https://github.com/projeto-de-algoritmos-2024/PD_leetcode_exerc/blob/master/Questoes/Q446/assets/CodigoTeste.png "TestesRodados")

Saída obtida:
<br>

![SaidasObtidas](https://github.com/projeto-de-algoritmos-2024/PD_leetcode_exerc/blob/master/Questoes/Q446/OutputTeste.png "SaidasObtidas")

Para realização desta questão foi utilizado um algoritmo de programação dinâmica, onde recebemos um array de inteiros, e devemos calcular a quantidade de combinações possíveis que atenda ao critério de uma subsequência de tamanho no mínimo 3, com diferença x entre cada elemento da sequência. Para realizá de tal foi utilizado o conceito de array de dicionários como memoization onde ao fim de cada operação de comparações obtemos um possível elemento de uma sequência, semelhante ao algoritmo clássico maior subsequência.
<br>

![Submissao](https://github.com/projeto-de-algoritmos-2024/PD_leetcode_exerc/blob/master/Questoes/Q446/assets/LeetCode.png "Exercicio Submetido")



