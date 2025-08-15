def triangular_number(n):
  if n < 0:
    return "Error: No se puede calcular el número triangular de un número negativo."
  elif n == 0:
    return 0
  else:
    return n + triangular_number(n - 1)

print(triangular_number(0))  # 0
print(triangular_number(3))  # 6
print(triangular_number(4))  # 10
print(triangular_number(5))  # 15
print(triangular_number(6))  # 21