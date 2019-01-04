from Archivos.Miarchivo import *
from Modelado.Mimodelo import *
m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
#op = input("Ordenar por nombre (1) o Ordenar por campeonato (2)")
#listado = []
for d in lista:
    # print(d)
    p = Equipo(d[0], d[1], d[2], d[3])
    listado = [p]
#if op == 1:
    lista = [p.nombre for e in listado]
    lista.sort()#Ordena la lista 
    print(lista)#Imprime la Lista ordenada
#if op == 2:
    lista2 = [p.campeonatos for e in listado]
    lista2.sort()#Ordena la lista 
    print(lista2)#Imprime la Lista ordenada