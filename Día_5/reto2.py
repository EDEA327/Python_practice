"""
Escribe una función
(puedes ponerle cualquier nombre que quieras)
que reciba cualquier palabra como parámetro, y que devuelva todas sus letras únicas
(sin repetir)
pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra "entretenido",
debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
"""
from typing import List
# Solution

def order_a_string_n_quit_duplicates(word:str) -> List[str]:
    new_list:List[str] = []
    for letter in word:
        new_list.append(letter) # se añaden las letras a la lista
    # con sorted() se ordena la lista, con set() se eliminan los duplicados
    # y con list() volvemos el set() a una lista.
    return sorted(list(set(new_list)))

print(order_a_string_n_quit_duplicates("entretenido"))




