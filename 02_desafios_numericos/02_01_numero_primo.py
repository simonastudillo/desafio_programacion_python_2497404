def is_primo(numero):
  if numero <= 1:
    return False
  for n in range(2, numero):
    if numero % n == 0:
      return False
  return True


print(is_primo(5)) # True
print(is_primo(4)) # False
print(is_primo(3)) # True
print(is_primo(12)) # False
print(is_primo(43)) # True