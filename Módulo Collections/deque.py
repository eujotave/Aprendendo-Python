# Importação

from collections import deque

"""
O módulo deque se trata de uma lista de alta perfomance. Entretanto, age um pouco diferente de uma lista como nós
conhecemos. No caso do deque, ao invés de aceitar vários elementos e formar uma lista, ele só aceita 1 único elemento
e divide ele em vários outros elementos, como se fosse utilizado um .split

Exemplo:

fruta = deque("Banana")

print(fruta) -> deque(['B', 'a', 'n', 'a', 'n', 'a'])

Em listas, nós podemos utilizar os comandos:

.append -> Adiciona um elemento no fim da lista
.pop -> Remove um elemento do fim da lista
"""

# Exemplo .append

lista = [1, 2, 3, 4, 4, 5]

lista.append(9)
print(lista)  # [1, 2, 3, 4, 4, 5, 9]

# Exemplo .pop

lista = [1, 2, 3, 4, 4, 5]

lista.pop()
print(lista)  # [1, 2, 3, 4, 4]

"""
Se percebemos, nós só conseguimos adicionar e remover elementos ao final da lista, o que pode acabar impossibilitando 
casos que devemos adicionar ou remover valores do inicio.

Nestes casos, podemos usar o deque, já que por ser uma "lista de alta perfomance", conseguimos usar os comandos:

.appendleft
.popleft 
"""

# Utilizando o deque e imprimindo os resultados

# Exemplo .appendleft

deq = deque("Goiaba")

deq.appendleft("A")

print(deq)  # deque(['A', 'G', 'o', 'i', 'a', 'b', 'a'])

# Perceba que o 'A' foi adicionado ao inicio e não ao fim como normalmente ocorre

# Exemplo .popleft

deq = deque("Goiaba")

deq.popleft()

print(deq)  # deque(['o', 'i', 'a', 'b', 'a'])

# Perceba que o primeiro elemento foi removido ao invés do ultimo como normalmente ocorre


