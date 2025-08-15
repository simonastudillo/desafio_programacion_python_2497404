def order_buble(number_list):
  temporal = []
  change = True
  while change:
    change = False
    for i in range(len(number_list) - 1):
      if number_list[i] > number_list[i + 1]:
        temporal = number_list[i]
        number_list[i] = number_list[i + 1]
        number_list[i + 1] = temporal
        change = True
  return number_list

print(order_buble([3,8,4,1,2])) # [1, 2, 3, 4, 8]




def ordenamiento_burbuja(lista):

    for i in range(len(lista)):

        for j in range(0, len(lista) - i - 1):

            if lista[j] > lista[j+1]:
                temporal = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal

    return lista

print(ordenamiento_burbuja([3,8,4,1,2])) # [1, 2, 3, 4, 8]
