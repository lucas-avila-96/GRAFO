
from src.classNodo import Nodo


class Lista:
    __comienzo = None
    __tamano = 0

    def __init__(self):
        self.__comienzo = None
        self.__tamano = 0

    def insertarAlFinal(self, item):
        acutual = self.__comienzo
        anterior = None
        pos = 0
        while pos < self.__tamano:
            anterior = acutual
            acutual = acutual.getSiguiente()
            pos += 1
        nuevoNodo = Nodo(item)
        if anterior is None:
            nuevoNodo.setSiguiente(acutual)
            self.__comienzo = nuevoNodo
        else:
            anterior.setSiguiente(nuevoNodo)
        self.__tamano += 1


    def __str__(self):
        aux = self.__comienzo
        out = ''
        while aux != None:
            out += str(aux.getDato()) + ' -> '
            aux=aux.getSiguiente()
        return out

    def getTamano(self):
        return self.__tamano

    def getLista(self):
        aux = self.__comienzo
        out = []
        while aux != None:
            out.append(aux.getDato())
            aux=aux.getSiguiente()
        return out