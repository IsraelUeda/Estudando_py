"""
deque é uma lista de alta performace
pode adicionar elementos no começo ou no final
"""

from collections import deque

deq= deque("israel")

print(deq)

deq.append("u")

print(deq)

deq.appendleft("l")

print(deq)

deq.pop() #remove e retorna o ultimo elemento

deq.popleft() #remove e retorna o primeiro elemento