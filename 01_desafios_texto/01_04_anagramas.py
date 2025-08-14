def anagrama(palabra_1, palabra_2):

    letras_palabra_1 = sorted(palabra_1.lower())
    letras_palabra_2 = sorted(palabra_2.lower())

    return letras_palabra_1 == letras_palabra_2


print(anagrama("lama", "Mala"))   # True
print(anagrama("calor", "coral")) # True
print(anagrama("gato", "gota")) # True
print(anagrama("cama", "casa"))   # False
