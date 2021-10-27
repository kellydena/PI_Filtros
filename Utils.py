import numpy as np
import matplotlib.image as im

def fileToMatriz(nome_file: str) -> np.array:
  matriz_colorida = im.imread(nome_file)
  matriz_8bit = matriz_colorida
  matriz_8bit = matriz_8bit.astype(np.uint16)
  return matriz_8bit

def imagemToCinza(matrix_colorida: np.array) -> np.array:
  linhas = matrix_colorida.shape[0]
  colunas = matrix_colorida.shape[1]

  matrix_gray = np.zeros((linhas, colunas))

  for i in range(linhas):
      for j in range(colunas):
          r, g, b = matrix_colorida[i, j]
          matrix_gray[i, j] = int((r + g + b) / 3)

  return matrix_gray


def matrizLimitada(matriz: np.array):
  lins = matriz.shape[0]
  cols = matriz.shape[1]
  matrizLimitada = matriz.copy()

  for i in range(1, lins-1):
    for j in range(1, cols-1):
      matrizLimitada[i][j] = max(0, matrizLimitada[i][j])
      matrizLimitada[i][j] = min(255, matrizLimitada[i][j])

  return matrizLimitada