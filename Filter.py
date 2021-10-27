from matplotlib import cm
import matplotlib.image as im
import numpy as np
import matplotlib.pyplot as plt

from Utils import matrizLimitada

def blur(matrizImage: np.array) -> np.array:
  matrizImagemBlur = matrizImage.copy()
  lins = matrizImage.shape[0]
  cols = matrizImage.shape[1]

  m = matrizImage
  for i in range(1, lins-1):
    for j in range(1, cols-1):
      matrizImagemBlur[i][j] = (
                                  1*m[i-1][j-1] + 1*m[i-1][j  ] + 1*m[i-1][j+1] + 
                                  1*m[i  ][j-1] + 1*m[i  ][j  ] + 1*m[i  ][j+1] + 
                                  1*m[i+1][j-1] + 1*m[i+1][j  ] + 1*m[i+1][j+1]
                                )/9
  matrizImagemBlur.astype(int)
  return matrizImagemBlur


def whiteningBorder(matrizImage: np.array):
  matrizImagemSobelVertical = matrizImage.copy()
  matrizImagemSobelHorizontal = matrizImage.copy()

  lins = matrizImage.shape[0]
  cols = matrizImage.shape[1]

  m = matrizImage
  for i in range(1, lins-1):
    for j in range(1, cols-1):
        matrizImagemSobelVertical[i][j] = (
                                    1*m[i-1][j-1] + 0*m[i-1][j  ] + -1*m[i-1][j+1] + 
                                    2*m[i  ][j-1] + 0*m[i  ][j  ] + -2*m[i  ][j+1] + 
                                    1*m[i+1][j-1] + 0*m[i+1][j  ] + -1*m[i+1][j+1]
                                    )
        matrizImagemSobelVertical[i][j] = max(0, matrizImagemSobelVertical[i][j])
        matrizImagemSobelVertical[i][j] = min(255, matrizImagemSobelVertical[i][j])

  for i in range(1, lins-1):
    for j in range(1, cols-1):
        matrizImagemSobelHorizontal[i][j] = (
                                    1*m[i-1][j-1] +  2*m[i-1][j  ] +  1*m[i-1][j+1] + 
                                    0*m[i  ][j-1] +  0*m[i  ][j  ] +  0*m[i  ][j+1] + 
                                   -1*m[i+1][j-1] + -2*m[i+1][j  ] + -1*m[i+1][j+1]
                                    )
        matrizImagemSobelHorizontal[i][j] = max(0, matrizImagemSobelHorizontal[i][j])
        matrizImagemSobelHorizontal[i][j] = min(255, matrizImagemSobelHorizontal[i][j])

  matrizImagemSobel = matrizImagemSobelHorizontal + matrizImagemSobelVertical

  matrizImagemSobelLimitada = matrizLimitada(matrizImagemSobel)
  
  return matrizImagemSobelLimitada


def unsharp(matrizCinza: np.array, matrizBlur: np.array):
  matrizUnsharp = matrizCinza - matrizBlur
  matrizUnsharpLimitada = matrizLimitada(matrizUnsharp)
  return matrizUnsharpLimitada


def sharpening(matrizUnsharp: np.array, matrizCinza: np.array):
  matrizSharpening = matrizUnsharp + matrizCinza
  matrizSharpLimitada = matrizLimitada(matrizSharpening)
  return matrizSharpLimitada


def applyBlur(matrizCinza: np.array, matrizRgb: np.array):
  matrizImagemBlurCinza = blur(matrizCinza)
  plt.title('Filtro Blur na imagem cinza')
  plt.imshow(matrizImagemBlurCinza, cmap='gray')
  plt.show()

  matrizImagemBlurRgb = blur(matrizRgb)
  plt.title('Filtro Blur na imagem original')
  plt.imshow(matrizImagemBlurRgb)
  plt.show()
                     

def applyWhitening(matrizCinza: np.array):
  matrizImageSobel = whiteningBorder(matrizCinza)
  plt.title('Filtro de clareamento de bordas')
  plt.imshow(matrizImageSobel, cmap='gray')
  plt.show()


def applyUnsharp(matrizCinza: np.array, matrizBlur: np.array):
  matrizUnsharp = unsharp(matrizCinza, matrizBlur)
  plt.title('Filtro Unsharp')
  plt.imshow(matrizUnsharp, cmap='gray')
  plt.show()


def applySharpening(matrizUnsharp: np.array, matrizCinza: np.array):
  matrizSharpening = sharpening(matrizUnsharp, matrizCinza)
  plt.title('Filtro Sharpening')
  plt.imshow(matrizSharpening, cmap='gray')
  plt.show()
