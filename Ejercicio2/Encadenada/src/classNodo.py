class Nodo:
    __item = None
    __siguiente = None

    def __init__(self, item):
        self.__item = item
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__item
    
    def setDato(self, item):
        self.__item = item