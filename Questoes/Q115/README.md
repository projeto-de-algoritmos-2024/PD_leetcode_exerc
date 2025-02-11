## 115. Distinct Subsequences

### Enunciado:
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

### Exemplo 1
>**Input:** s = "rabbbit", t = "rabbit"
>**Output:** 3

### Exemplo 2
>**Input:** s = "babgbag", t = "bag"
>**Output:** 5

#### Entradas e saídas obtidas:

Codigo de teste:
<br>

![TestesRodados](https://github.com/projeto-de-algoritmos-2024/PD_leetcode_exerc/blob/master/Questoes/Q115/assets/CodigoTeste.png "TestesRodados")

Saída obtida:
<br>

![SaidasObtidas](https://github.com/projeto-de-algoritmos-2024/PD_leetcode_exerc/blob/master/Questoes/Q115/OutputTeste.png "SaidasObtidas")

Para realização desta questão foi utilizado um algoritmo de programação dinâmica, onde recebemos 2 strings, e devemos calcular a quantidade de possibilidades de escrever uma string “A” com caracteres de uma string “B” de maneira ordenada. Para realizá de tal foi utilizado o conceito de uma matriz como memoization onde ao fim da operação obtemos a quantidade necessária, semelhante ao algoritmo clássico de edit string.
<br>

![Submissao](https://github.com/projeto-de-algoritmos-2024/PD_leetcode_exerc/blob/master/Questoes/Q115/assets/Aceito.png "Exercicio Submetido")



