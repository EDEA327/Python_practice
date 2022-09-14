"""
Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver
True
si enalgún momento se ha ingresado al numero
cero (0)
repetido dos veces consecutivas.
"""

def two_times_zero(*args:int) -> bool:
    j:int = 1
    i:int = 0
    while j < len(args):
        print(f"En la vuelta {i+1} i = {i} , j = {j}\nargi = {args[i]}, argj = {args[j]}")
        if args[i]  == args[j]:
            if args[i] == 0:
                return True
            else:
                i,j = j, j + 1
        else:
            i,j = j, j + 1
    return False

print(two_times_zero(0,1,3,4,5,6,9,0))