from Archivos.Miarchivo import *
from Modelado.Mimodelo import *
m = MiArchivo()
m2 = MiArchivoEscribir()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
listado = []

for d in lista:
    # print(d)
    p = Equipo(d[0], d[1], d[2], d[3])
    listado.append(p)
operaciones = Operaciones(listado)
op = int(input("Ordenar por nombre (1) o Ordenar por campeonato (2)"))
if op == 1:
    listado2 = operaciones.ordenar_nombre()
if op==2:
    listado2 = operaciones.ordenar_campeonatos()
for i in listado2:
	m2.agregar_informacion(i)
	print(i)