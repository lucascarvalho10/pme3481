import numpy as np

# Criar um array de números de 2 a 120
numeros = np.arange(2, 121)
print (numeros)

# Calcular a mediana usando numpy
mediana = np.median(numeros)

# Exibir a mediana
print("A mediana do conjunto de números de 2 a 120 é:", mediana)