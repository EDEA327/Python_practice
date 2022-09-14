""" Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
    Si la suma de los 3 numeros es mayor a 15 va a devolver el número mayor
.   Si la suma de los 3 numeros es menor a 10,va a devolver el número menor.
    Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio
"""
def devolver_distintos(num1: int, num2: int , num3: int) -> int:
    suma = num1 + num2 + num3
    major = max(num1, num2, num3)
    minor = min(num1, num2, num3)
    medio = suma - max(num1, num2, num3) - min(num1, num2, num3)
    if suma > 15 :
        print(f"The sum is {suma} you get the major number")
        return major
    elif suma < 10:
        print(f"The sum is {suma} you get the minor number")
        return minor
    elif suma in range(10,16):
        print(f"The sum is {suma} you get the middle number")
        return medio


print(devolver_distintos(3,2,4))

