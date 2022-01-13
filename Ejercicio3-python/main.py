# Ejercicio 3
# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.
# Objetivo:
# - Uso de bucles anidados
# - El uso de colecciones

def main():
    pass

def primeNumCalculate (n):
    listPrimNums = []

    divisorList = list(range(1, n+1))
    dividendList = list(range(1, n+1))

    for x in divisorList:
        result = list(map(lambda n: x % n, dividendList))
        if result.count(0) == 2:
            listPrimNums.append(x)
    print(listPrimNums)

primeNumCalculate(100)

if __name__ == '__main__':
    main()

