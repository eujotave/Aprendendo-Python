# Importação

from collections import namedtuple

"""
O namedtuple (Tupla Nomeada), se trata de uma tupla diferente, onde é possível passar um nome e parâmetros para uma 
tupla (Como uma espécie de dicionário). 

OBS: Diferentemente dos dicionários, as tuplas e tuplas nomeadas são indexadas, permitindo assim o acesso de cada
elemento por meio do índice
"""

# Utilizando o namedtuple

# Existem 3 formas de fazer o namedtuple

# Forma 1:

compras = namedtuple("comidas", "produto marca quantidade ")

# Forma 2:

compras = namedtuple("comidas", "produto, marca, quantidade")

# Forma 3:

compras = namedtuple("comidas", ["produto", "marca", "quantidade"])

# Utilizando o namedtuple para atribuir valores

molho = compras(produto="Molho de Tomate", marca="Quero", quantidade=3)

# Imprimindo/Acessando Dados

print(molho)

# Também podemos acessar cada dado da tupla, para isso, podemos utilizar 2 formas:

# Forma 1 (Por meio do index):

print(molho[0])  # Produto
print(molho[1])  # Marca
print(molho[2])  # Quantidade

# Forma 2 (Por meio dos parâmetros // Mais Recomendada):

print(molho.produto)  # Produto
print(molho.marca)  # Marca
print(molho.quantidade)  # Quantidade

"""
Com isso, nos podemos utilizar O MODELO (nome e parâmetros) daquela tupla em outras diversas vezes, como nesse caso 
para adicionar novos elementos nas compras, onde também podemos acessar cada parâmetro passado. 
"""

frango = compras(produto="Peito de Frango", marca="Sadia", quantidade=2)
milho = compras(produto="Milho Enlatado", marca="Quero", quantidade=3)

print(frango)
print(milho)

print(frango.marca)
print(milho.quantidade)

