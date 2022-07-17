import pyautogui
import numpy as np
import cv2

#? Raw Pixel Descriptor
#Esta função irá retornar uma lista de números correspondento a intensidade bruta de pixels	na imagem
def GetRawPixel(dir):
	#Esta linha irá ler a imagem informada e retornar um array, contendo as dimensões da imagem e os canais (RGB)
	image = cv2.imread(dir)
	#A função "Flatten", vai dar um tipo de "explode" na imagem, ou seja, vai transformar a imagem em um array
	return image.flatten()

#? Color Mean Descriptor
# Esta função irá retornar o valor médio de cada canal (RGB) da imagem
def GetColorMean(dir):
	image = cv2.imread(dir)
	#Será retornada uma lista, contendo o valor médio de cada canal
	return cv2.mean(image)

#? Color Mean and Standard Deviation Descriptor
# Esta função irá retornar o valor médio e o desvio padrão de cada canal (RGB) da imagem
def GetColorMeanAndStdDev(dir):
	image = cv2.imread(dir)
	#Serão retornados dois valores, o valor médio e o desvio padrão
	(means, stds) = cv2.meanStdDev(image)
	#Retorna 6 valores, a média de cada canal, bem como o desvio padrão de cada canal na imagem.
	return np.concatenate([means, stds]).flatten()


#? Color Histogram Descriptor
# Esta função irá retornar um array contendo o histograma de cada canal (RGB) da imagem
def GetColorHistogram(dir):
	image = cv2.imread(dir)
	hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
	return hist


print(GetColorHistogram('charizard.png'))
	