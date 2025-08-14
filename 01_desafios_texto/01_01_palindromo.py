def es_palindromo(texto):

  texto_minuscula = texto.lower()
  texto_sin_espacios = texto_minuscula.replace(" ", "")
  texto_sin_acentos = texto_sin_espacios.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
  return texto_sin_acentos == texto_sin_acentos[::-1]


print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False
