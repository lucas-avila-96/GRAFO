
import numpy as np

from DiGrafoPonderado import DiGrafoPonderado


if __name__ == '__main__':
    aristas = [
		(0, 4, 3), (2, 4, 5), (3, 2, 7), (1, 3, 4), (0, 1, 2)
	]

    n = 8
    grafo = DiGrafoPonderado(n, aristas)

    grafo.mostrar()
    print(grafo.esCiclico())
    print(grafo.esConexo(0))
    print('\nAmplitud')
    grafo.BFS(0)
    print('\nProfundiad')
    grafo.DFS(0)

    visitados = [False] * n
    (origen, destino) = (0, 2)
    print('\nTodos los caminos')
    grafo.todosLosCaminos(origen, destino, visitados)
    grafo.menorCamino(origen, destino)
