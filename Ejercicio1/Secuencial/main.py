
import numpy as np

from Grafo import Grafo


if __name__ == '__main__':
    aristas = [
		(0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
		(3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
	]

    '''
    aristas = [
        (0, 3), (0, 1), (3, 4), (1, 2), (4, 2)
    ]
    '''
    n = 8
    grafo = Grafo(n, aristas)

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
