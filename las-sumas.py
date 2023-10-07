"""
Crea una función que encuentre todas las combinaciones de los números
 de una lista que suman el valor objetivo.
 - La función recibirá una lista de números enteros positivos
   y un valor objetivo.
 - Para obtener las combinaciones sólo se puede usar
   una vez cada elemento de la lista (pero pueden existir
   elementos repetidos en ella).
  - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
    Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
    (Si no existen combinaciones, retornar una lista vacía)
"""


def find_sums(numbers, target):
    def find_sum(combination):
        return

    numbers.sort()
    result = list()
    find_sum(0, [])
    return result



print(find_sums([1, 2, 3, 4], 6))
