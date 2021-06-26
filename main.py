import numpy as np
row = 100
col = 100
identifier = int(input('Ingrese el número de su cédula: '))
dimension = (100, 100)
matrix = np.ones(dimension)

def full(matrix):
  for i in range(row):
    for j in range(col):
      matrix[i][j] = identifier
  print('Matrix: ')
  print(matrix)

def sumac(matrix):
  sc= np.sum(matrix,axis=0,)
  print('Sum colum of matrix : ', sc)

def sumaf(matrix):
  sf= np.sum(matrix,axis=0,)
  print('Sum file of matrix : ', sf)

def sumad(matrix):
  sd = 0
  for i in range(100):
    sd += matrix[i][i]
  print('Sum d of matrix diagonal: ', sd)

def multc(matrix):
  mc= np.multiply(matrix,axis=0,)
  print('multiply colum of matrix : ', mc)

def multf(matrix):
  mf= np.multiply(matrix,axis=0,)
  print('multiply file of matrix : ', mf)

def multd(matrix):
  print('multiplicacion d of matrix diagonal: 0',)


  
full(matrix)


menu = int (input("Prueba 1: \n1.-Suma Columna\n 2.-Suma Fila\n 3.-Suma Diagonal\n 4.-Multiplica Columna\n 5.-Multiplica Fila\n6.-Multiplica Diagonal\n 7.- Salir" ))
while menu !=7:
  if menu ==1:
    sumac(matrix)
  elif menu ==2:
    sumaf(matrix)
  elif menu ==3:
    sumad(matrix)
  elif menu ==4:
    multc(matrix)
  elif menu ==5:
    multf(matrix)
  elif menu ==6:
    multd(matrix)
  else:
    print("no valido")
  menu = int (input("Prueba 1: \n1.-Suma Columna\n 2.-Suma Fila\n 3.-Suma Diagonal\n 4.-Multiplica Columna\n 5.-Multiplica Fila\n6.-Multiplica Diagonal\n 7.- Salir" ))

 