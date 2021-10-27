import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt
import imghdr

from Filter import applyBlur, applyWhitening, applyUnsharp, applySharpening
from Filter import blur, unsharp

from Utils import fileToMatriz, imagemToCinza

def applyFilter(selectedFilter:int, image:str):
  matrizRgb = fileToMatriz(image)
  plt.imshow(matrizRgb)
  plt.show()

  matrizCinza = imagemToCinza(matrizRgb)
  plt.imshow(matrizCinza, cmap='gray')
  plt.show()

  if selectedFilter == 0:
    applyBlur(matrizCinza, matrizRgb)
  elif selectedFilter == 1:
    applyWhitening(matrizCinza, matrizRgb)
  elif selectedFilter == 2:
    matrizBlur = blur(matrizRgb)
    applyUnsharp(matrizRgb, matrizBlur)
  elif selectedFilter == 3:
    matrizBlur = blur(matrizRgb)
    matrizUnsharp = unsharp(matrizRgb, matrizBlur)
    applySharpening(matrizUnsharp, matrizRgb)
    
def checkTypeImage(path: str):
  if isValid(path):
    if imghdr.what(path) == 'jpeg':
      return True
    else:
      print('Formato invalido, por favor tente com uma imagem do tipo JPEG ou JPG')
      return False
  else:
    return False

def isValid(path: str):
  try:
    imghdr.what(path)
    return True
  except:
    print('Falha ao encontrar a imagem. tente novamente')
    return False

def selectedFilter():
  print('Escolha o filtro que deseja aplicar:')
  print('1 - Blur')
  print('2 - Clareamento das bordas')
  print('3 - Unsharp')
  print('4 - Sharpening')
  selectedFilter = int(input('Selecione:'))

  while selectedFilter not in (1,2,3,4):
    print("Filtro não existente. Por favor tente novamente!")
    selectedFilter = int(input('Selecione:'))
  
  return selectedFilter

def selectInput():
  print("Escolha o tipo de entrada:")
  print("1 - Imagem em disco")
  print('2 - Imagem do sistema')

  selectInput = int(input())

  while selectInput not in (1,2):
    print('Entrada não reconhecida. Por favor tente novamente!')
    selectInput = int(input("Escolha o tipo de entrada:"))

  return selectInput

def getPathImage(imageSelected: int):
  if imageSelected == 1:
    return 'Filtros/img/birds.jpg'
  elif imageSelected == 2:
    return 'Filtros/img/magenta.jpg'
  elif imageSelected == 3:
    return 'Filtros/img/star.jpg'
  elif imageSelected == 4:
    return 'Filtros/img/wine.jpg'
    

def getImageInput(typeInput : int):
  if typeInput == 2:
    print('Selecione uma das imagens abaixo:')
    print('1 - Passaros')
    print('2 - Magenta')
    print('3 - Ceu estrelado')
    print('4 - Wine')
    
    imgSelect = int(input())
    while imgSelect not in (1,2,3,4):
      print("Imagem não existente. Por favor tente novamente!")
      imgSelect = int(input('Selecione:'))

    pathImage = getPathImage(imgSelect)
    return pathImage

  else:
    pathImage = input("Digite o caminho da imagem:")
    while checkTypeImage(pathImage) != True:
      pathImage = input("Digite a path da imagem: ")

    return pathImage

def init():
  typeFilter = selectedFilter()
  typeInput =  selectInput()
  pathImage = getImageInput(typeInput)

  applyFilter(typeFilter, pathImage)


def applyFilter(selectedFilter:int, image:str):
  matrizRgb = fileToMatriz(image)
  plt.title('Imagem Escolhida')
  plt.imshow(matrizRgb)
  plt.show()

  matrizCinza = imagemToCinza(matrizRgb)
  plt.title('Imagem cinza')
  plt.imshow(matrizCinza, cmap='gray')
  plt.show()

  if selectedFilter == 1:
    applyBlur(matrizCinza, matrizRgb)
  elif selectedFilter == 2:
    applyWhitening(matrizCinza)
  elif selectedFilter == 3:
    matrizBlur = blur(matrizCinza)
    applyUnsharp(matrizCinza, matrizBlur)
  elif selectedFilter == 4:
    matrizBlur = blur(matrizCinza)
    matrizUnsharp = unsharp(matrizCinza, matrizBlur)
    applySharpening(matrizUnsharp, matrizCinza)
    

init()
