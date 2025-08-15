def flattening(array):
   if type(array) is not list:
      return array
   new_list = []
   repeat = False
   for element in array:
      if type(element) is list:
         new_list.extend(element)
         repeat = True
      else:
         new_list.append(element)
   if repeat:
      return flattening(new_list)
   return new_list

print(flattening([2, 3, 4, [3, 2]])) # [2, 3, 4, 3, 2]
print(flattening([2, 3, 4, [[2],[6,5]]])) # [2, 3, 4. [2]]

def aplanar_lista(lista):

    nueva_lista = []

    for elemento in lista:

        if type(elemento) is list:
            nueva_lista.extend(elemento)
        else:
            nueva_lista.append(elemento)

    return nueva_lista


print(aplanar_lista([2, 3, 4, [3, 2]])) # [2, 3, 4, 3, 2]
print(aplanar_lista([2, 3, 4, [[2]]])) # [2, 3, 4. [2]]
