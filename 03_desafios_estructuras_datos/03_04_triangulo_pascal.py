""" Triangulo de Pascal

       1        fila 1 -> triangulo[0]
      1 1       fila 2 -> triangulo[1]
     1 2 1      fila 3 -> triangulo[2]
    1 3 3 1     fila 4 -> triangulo[3]

"""

def pascal_triangle(rows_count):
   triangle = []
   for row in range(rows_count):
      triangle_row = []
      for col in range(row + 1):
         if col == 0 or col == row:
            triangle_row.append(1)
         else:
            value = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle_row.append(value)
      triangle.append(triangle_row)
   return triangle

print(pascal_triangle(6)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]


def triangulo_pascal(cantidad_filas):

    triangulo = []

    for n_fila in range(cantidad_filas):

        fila = []

        for posicion in range(n_fila+1):

            if posicion == 0 or posicion == n_fila:
                fila.append(1)
            else:
                valor = triangulo[n_fila-1][posicion-1] + triangulo[n_fila-1][posicion]
                fila.append(valor)

        triangulo.append(fila)
    return triangulo

print(triangulo_pascal(6)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
