import numpy as np

class DiGrafo:
    __matriz = None
    __nroNodos = None

    def __init__(self, n, aristas) -> None:
        self.__matriz = np.zeros((n,n), dtype=int)
        self.__nroNodos = n

        for (origen, destino) in aristas:
            self.__matriz[origen][destino] = 1

    def adyacentes(self, origen):
        ady = []
        if origen <= self.__nroNodos:
            for i in range(self.__nroNodos):
                if self.__matriz[origen][i] == 1:
                    ady.append(i)
        return ady

    def _esConexo(self, origen, visitados):
        visitados = [False] * self.__nroNodos
        visitados[origen] = True
        c = 1
        q = [origen]
        while q:
            p = q[0]
            q.pop(0)
            for i in self.adyacentes(p):
                if visitados[i] == False:
                    q.append(i)
                    visitados[i] = True
                    c += 1
        if c == self.__nroNodos:
            return True
        else:
            return False
        

    def esConexo(self, origen):
        visitados = [False] * self.__nroNodos
        res = self._esConexo(origen, visitados)
        return res

    def esClicioRecursivo(self, v, visitados, padre):
        visitados[v] = True
        for i in self.adyacentes(v):
            if visitados[i] == False:
                if(self.esClicioRecursivo(i, visitados, v)):
                    return True
            elif padre != i:
                return True
        return False

    def esCiclico(self):
        visitados = [False]*self.__nroNodos
        for i in range(self.__nroNodos):
            if visitados[i] == False:
                if(self.esClicioRecursivo(i, visitados, -1)) == True:
                    return True
        return False

    def arbolRecubrimiento(self):
        pass

    def BFS(self, origen):
        visitados = [False] * self.__nroNodos
        visitados[origen] = True
        q = [origen]
        while q:
            p = q.pop(0)
            print(p, end = ' ')
            for i in self.adyacentes(p):
                if visitados[i] == False:
                    q.append(i)
                    visitados[i] = True
                    
    def _DFS(self, origen, visitados, out = ''):
        print(origen, end = ' ')
        visitados[origen] = True
        for i in self.adyacentes(origen):
            if visitados[i] == False:
                self._DFS(i, visitados)

    def DFS(self, origen):
        visitados = [False] * self.__nroNodos
        self._DFS(origen, visitados)

    def mostrar(self):
        print(self.__matriz)

    def todosLosCaminos(self, origen, destino, visitados, camino = []): 
        visitados[origen]= True
        camino.append(origen)
        if origen == destino: 
            print(camino)
        else: 
            for i in self.adyacentes(origen): 
                if visitados[i]==False: 
                    self.todosLosCaminos(i, destino, visitados, camino) 
        camino.pop()
        visitados[origen]= False

    def menorCamino(self, origen, destino):
        visitados = []
        q = [[origen]]
        if origen == destino:
            print("Mismo nodo")
            return
        while q:
            camino = q.pop(0)
            nodo = camino[-1]
            if nodo not in visitados:
                for i in self.adyacentes(nodo):
                    nuevoCamino = list(camino)
                    nuevoCamino.append(i)
                    q.append(nuevoCamino)
                    if i == destino:
                        print("Menor camnio: ", nuevoCamino)
                        return
                visitados.append(nodo)
        print("No existe camino")
        return