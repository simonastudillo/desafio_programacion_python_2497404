def factorial(numero):
  if numero < 0:
    return "Error: No se puede calcular el factorial de un número negativo."
  elif numero == 0 or numero == 1:
    return 1
  else:
    resultado = 1
    for i in range(2, numero + 1):
      resultado *= i
    return resultado


print(factorial(0)) # 1
print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120


def calcular_factorial_recursivo(numero):

    if numero == 0 or numero == 1:
        return 1

    return numero * calcular_factorial_recursivo(numero-1)


print(calcular_factorial_recursivo(0)) # 1
print(calcular_factorial_recursivo(3)) # 6
print(calcular_factorial_recursivo(4)) # 24
print(calcular_factorial_recursivo(5)) # 120
