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
Esta função recebe uma mensagem como entrada e retorna a codificação one-hot da mensagem.

## para_string(array)
Esta função recebe uma mensagem codificada em one-hot como entrada e retorna a mensagem original como uma string.

## cifrar(msg, P)
Esta função recebe uma mensagem e uma matriz de substituição P como entrada e retorna a mensagem criptografada.

## de_cifrar(msg, P)
Esta função recebe uma mensagem criptografada e uma matriz de substituição P como entrada e retorna a mensagem descriptografada.

## enigma_simples(msg, P, E)
Esta função recebe uma mensagem, uma matriz de substituição P e uma matriz de criptografia E como entrada e retorna a mensagem criptografada.

## de_nigma_simples(msg, P, E)
Esta função recebe uma mensagem criptografada, uma matriz de substituição P e uma matriz de criptografia E como entrada e retorna a mensagem descriptografada.

## enigma(msg, P, E)
Esta função recebe uma mensagem, uma matriz de substituição P e uma matriz de criptografia E como entrada e retorna a mensagem criptografada.

## de_nigma(msg, P, E)
Esta função recebe uma mensagem criptografada, uma matriz de substituição P e uma matriz de criptografia E como entrada e retorna a mensagem descriptografada.


Versão
A versão atual do módulo é 0.0.2.
