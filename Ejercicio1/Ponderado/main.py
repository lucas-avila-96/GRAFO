
import numpy as np

from GrafoPonderado import GrafoPonderado


if __name__ == '__main__':
    aristas = [
		(0, 3, 1), (1, 0, 4), (1, 2, 6), (1, 4, 2), (2, 7, 3), (3, 4, 6),
		(3, 5, 6), (4, 3, 2), (4, 6, 9), (5, 6, 4), (6, 7, 1)
	]

    '''
    aristas = [
        (0, 3), (0, 1), (3, 4), (1, 2), (4, 2)
    ]
    '''
    n = 8
    grafo = GrafoPonderado(n, aristas)

    grafo.mostrar()
    print(grafo.esCiclico())
    print(grafo.esConexo(0))
    print('\nAmplitud')
    grafo.BFS(0)
    print('\nProfundiad')
    grafo.DFS(0)

    visitados = [False] * n
    (origen, destino) = (0, 7)
    print('\nTodos los caminos')
    grafo.todosLosCaminos(origen, destino, visitados)
    grafo.menorCamino(origen, destino)
