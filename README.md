# Enigma-Sigma
O módulo é chamado de Enigma Sigma.

Descrição
O módulo fornece um conjunto de funções que permitem criptografar e descriptografar mensagens usando uma cifra de substituição simples. Também inclui funções para codificar e decodificar mensagens usando um esquema de codificação one-hot.

Instalação
Este módulo pode ser instalado via pip. Para instalar o módulo, execute o seguinte comando:

```
pip install git+https://github.com/marchettomarcelo/Enigma-Sigma
```
Uso
Para usar este módulo, importe-o da seguinte maneira:

```
import enigma_sigma
```
Funções
O módulo cipher fornece as seguintes funções:

## para_one_hot(msg)
Esta função recebe uma mensagem como entrada e retorna a codificação one-hot da mensagem. Para isso, utilizamos uma matriz identidade e uma string com nosso alfabeto. 

A string nos da a posição de cada caracter, e depois adicionamos a linha da matriz correspondente ao index() do caracter em uma lista, por fim transformamos essa lista em um array e o transpomos. Assim, cada coluna representa uma letra do nosso alfabeto.


## para_string(array)
Esta função recebe uma mensagem codificada em one-hot como entrada e retorna a mensagem original como uma string. 

A entrada é um array, então, o transpomos de novo (cada letra é representada por uma linha) e vemos qual é o index() do 1 de cada uma dessas linhas do array. Por fim, adicionamos a letra (do nosso alfabeto) correspondente a esse índice em uma string, que é retornada ao final da operação.


## cifrar(msg, P)
Esta função recebe uma mensagem e uma matriz de permutação "P" como entrada e retorna a mensagem criptografada. 

Utilizando a multiplicação de matrizes, modificamos a mensagem original. Ela entra como string, é transformada em matriz (para_one_hot()), é modificada através da multiplicação pela matriz de permutação escolhida (enviada na função), e é retornada como string (para_string()).


## de_cifrar(msg, P)
Esta função recebe uma mensagem criptografada e uma matriz de permutação "P" como entrada e retorna a mensagem descriptografada. 

O processo inverso ao cifrar ocorre. Utilizamos o para_one_hot() para transformar a string em matriz, utilizamos a inversa da matriz de permutação na hora de realizar a multiplicação, e retornamos uma string ao final (para_string()).


## enigma_simples(msg, P, E)
Esta função recebe uma mensagem (em string), uma matriz de permutação "P" e uma matriz de criptografia "E" como entrada e retorna a mensagem criptografada. 

Utilizamos as duas matrizes na hora de realizar a cifragem, então, é a matriz de permutação multiplicada pela matriz "enigma" (outra matriz de roatação da matriz identidade do alfabeto original), e retornamos a versão em string do resultado da multplicação.


## de_nigma_simples(msg, P, E)
Esta função recebe uma mensagem criptografada (em string), uma matriz de permutação "P" e uma matriz de criptografia "E" como entrada e retorna a mensagem descriptografada. 

Dessa vez, por utilizarmos duas matrizes, é o inverso de E multiplicando o inverso de P que multiplica a matriz da mensagem. O resultado dessa conta é tranformado em string no final e retornado.


## enigma(msg, P, E)
Esta função recebe uma mensagem (em string), uma matriz de permutação "P" e uma matriz de criptografia "E" como entrada e retorna a mensagem criptografada. 

A cada coluna da nossa matriz da mensagem, realizamos uma multiplicação que é cada vez maior. Começando sendo apenas E @ P @ msg, e incrementando o número de vezes que E é multiplicado a cada linha, assim, dificultando o processo inverso (já que não é apenas uma questão de multiplicar pela matriz inversa, cada linha tem um caminho de volta diferente).


## de_nigma(msg, P, E)
Esta função recebe uma mensagem criptografada (em string), uma matriz de permutação "P" e uma matriz de criptografia "E" como entrada e retorna a mensagem descriptografada.

A mensagem descriptografada é obtida por meio de uma multiplicação em série da inversa de E, seguindo a mesma lógica do enigma(). Então, na primeira coluna temos inv(E) @ inv(P) @ msg_coluna, na segunda temos inv(E) @ inv(E) @ inv(P) @ msg_coluna, e assim por diante. Dessa maneira, cada coluna precisa de sua própria sequência específica de multiplicações, dificultante o trabalho de decifrar a mensagem. Por fim, retornamos a mensagem resultante em string.


Versão
A versão atual do módulo é 0.0.2.
