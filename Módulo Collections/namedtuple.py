# Importação

from collections import namedtuple

"""
O namedtuple se trata de uma tupla diferente, onde é possível passar um nome e parâmetros para uma tupla. Fazendo com
que possamos injetar dados na mesma.  
"""

# Utilizando o namedtuple

# Existem 3 formas de fazer o namedtuple

# Forma 1:

compras = namedtuple("comidas", "produto marca quantidade ")

# Forma 2:

compras = namedtuple("comidas", "produto, marca, quantidade")

# Forma 3:

compras = namedtuple("comidas", ["produto", "marca", "quantidade"])

# Utilizando/Injetando Dados

molho = compras(produto="Molho de Tomate", marca="Quero", quantidade="3")

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
