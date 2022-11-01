
import numpy as np

from DiGrafo import DiGrafo


if __name__ == '__main__':
    aristas = [
		(0, 4), (2, 4), (3, 2), (1, 3), (0, 1)
	]

    n = 8
    grafo = DiGrafo(n, aristas)

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
