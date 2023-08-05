# Importação

from collections import Counter

# Módulo Counter

"""
O Counter basicamente vai receber um itéravel como parâmetro e vai criar um objeto do tipo Collections Counter, que 
funciona como um dicionário (Sendo passado como chave o nome da lista (parâmetro) e o valor que será a quantidade de 
ocorrências do elemento, ou seja, quantas vezes determinado elemento aparece naquela lista). Também é representado por 
Chaves{}, assim como um dict, como já foi dito.
"""

# Declarando os iteráveis

lista1 = [1, 1, 1, 2, 3, 3, 3, 3]
poema = ("Se olharmos a vida em seus pequenos detalhes, tudo parece bem ridículo. "
         "É como uma gota d`água vista num microscópio, uma só gota cheia de protozoários. "
         "Achamos muita graça como eles se agitam e lutam tanto entre si. "
         "Aqui, no curto período da vida humana, essa atividade febril produz um efeito cômico.")

palavras = poema.split()

# Utilizando o Counter

contagem = Counter(lista1)
contagem2 = Counter(palavras)

# Imprimindo os resultados

print(contagem)
print(contagem2)

"""
Se notarmos, no primeiro resultado ele imprimirá:

Counter({3: 4, 1: 3, 2: 1}) 

Ou seja, demonstra que o número 3 apareceu 4 vezes, o número 1 apareceu 3 vezes e por fim, o número 2 apareceu apenas
1 vez na lista em questão.

Já no segundo resultado, o Counter contou quantas vezes apareceu cada palavra, já que usamos o .split para dividir o 
poema. 

Counter({'vida': 2, 'como': 2, 'uma': 2, 'gota': 2, 'Se': 1, 'olharmos': 1, 'a': 1, 'em': 1, 'seus': 1...})

"""

# Também podemos descobrir os elementos mais comuns do iterável/Counter por meio do most_common, podendo ser muito útil

print(contagem2.most_common(3))  # Dentro do parênteses passamos a quantidade de resultados que queremos
