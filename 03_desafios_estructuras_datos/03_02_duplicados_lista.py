def search_repeted(list):
  repetead_item = []
  for item in list:
    if (list.count(item) > 1 and item not in repetead_item):
      repetead_item.append(item)
  return repetead_item

  
print(search_repeted(["ana", "paco", "paco", "emilio", "javier", "ana"])) # ["paco", "ana"]
print(search_repeted(["ana", "paco", "pacos", "emilio", "javier", "anita"])) # ["paco", "ana"]

def encontrar_duplicados(lista):

    elementos_lista = []
    duplicados = []

    for elemento in lista:

        if elemento in elementos_lista:
            duplicados.append(elemento)
        else:
            elementos_lista.append(elemento)

    return duplicados


print(encontrar_duplicados(["ana", "paco", "paco", "emilio", "javier", "ana"])) # ["paco", "ana"]
print(search_repeted(["ana", "paco", "pacos", "emilio", "javier", "anita"])) # ["paco", "ana"]
