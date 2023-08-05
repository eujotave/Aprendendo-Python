# Importação

from collections import OrderedDict

"""
O OrderedDict serve para garantir a ordem de inserção dos elementos em um dicionário, já que de forma padrão não é 
garantida. Ou seja, a partir do momento que este módulo é utilizado, a ordem dos elementos importa.
"""

# Utilizando o OrderedDict e Imprimindo os Dados

# Sem OrderedDict:

dicionario1 = {'a': 1, 'b': 2}
dicionario2 = {'b': 2, 'a': 1}

print(dicionario1 == dicionario2)  # True

# Com OrderedDict:

dicionario3 = OrderedDict({'a': 1, 'b': 2})
dicionario4 = OrderedDict({'b': 2, 'a': 1})

print(dicionario3 == dicionario4)  # False

"""
Podemos perceber que no primeiro caso, o resultado da comparação entre os dois dicionários será True, já que os dois 
são realmente iguais, levando em conta que os dicionários por padrão não garantem e não se importam com ordem, apenas
com valores.

Já no segundo caso, com o uso do OrderedDict, o resultado da comparação foi False, pois agora a ordem é importante, não
só os valores. Sendo assim, os dicionários são diferentes mesmo com valores iguais. 

Este é só um método de comparação para entendermos esta funcionalidade, pois este modulo é muito utilizado em casos
que são injetados muitos elementos em um só dict e o programa pode acabar por automatizar e utilizar uma ordem própria,
o que pode chegar a atrapalhar se você deseja a ordem certa de que os dados foram informados
"""
