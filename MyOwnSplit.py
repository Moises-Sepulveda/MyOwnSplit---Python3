#!/usr/bin/env python3
#_*_ coding: utf8 _*_

def mysplit(characterString,separatorCharacter):
	characterString = characterString.strip(separatorCharacter)
	lista = []
	counter = 0
	while True:
		if characterString.count(separatorCharacter) == 0:	
			lista.append(characterString)
			for i in range(len(lista)):
				lista[i] = lista[i].replace(separatorCharacter,"")

			return lista
		else:
			indice = characterString.index(separatorCharacter)
			lista.append(characterString [0:(indice+1)])
			characterString = characterString.replace(lista[counter],"")
			characterString = characterString.strip(separatorCharacter)
			counter+=1

separator = input("Introduce the separator character: ")
data = input("Introduce the data to convert in list: ")

print(mysplit(data,separator))