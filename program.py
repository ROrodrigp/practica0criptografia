#!/bin/sh
import fileinput
lista = []
suma = 0 
indice = 0 
archivo = fileinput.input()
while(True):
	numero = archivo.readline()
	n = numero.rstrip('\n')
	if (n == '') == True:
		break
	try:
		c = int(n)
		lista.append(c)
	except:

		c = float(n)
		lista.append(c)




for indice,num in enumerate(lista):
	suma = suma + lista[indice]
print(suma)


