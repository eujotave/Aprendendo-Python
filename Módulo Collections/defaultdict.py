# Importação

from collections import defaultdict

"""
O defaultdict vai servir para criar um valor default/padrão para um determinado dicionário, utilizando-se de um lambda
para isso. 

Este valor padrão vai ser exibido quando for solicitado por exemplo uma chave inexistente dentro do dict, 
assim evitando o KeyError.

Exemplo:

dicionario = {'raca': 'bulldog', 'idade: '7'} 

print(dicionario['raca']

print(dicionario[cor]) -> KeyError  //  Já que esta chave é inexistente
"""

# Utilizando o defaultdict
dicionario = defaultdict(lambda:"Não encontrado")

dicionario['raca'] = 'bulldog'
dicionario['idade'] = '7'

# Imprimindo os Dados

print(dicionario)
print(dicionario['cor'])

"""
Observe que exigimos uma chave inexistente. 
Sem o defaultdict iria aparecer o KeyError. Entretanto, por estarmos utilizando este módulo, será exibido o valor 
que definimos no lambda, neste caso 'Não encontrado'

Prestando também um pouco de atenção na forma como é exibido o primerio print, podemos ver que o que está sendo impresso 
na verdade é o próprio defaultdict, que utiliza-se de uma tupla com a função lambda e o nosso dicionário informado.
"""
