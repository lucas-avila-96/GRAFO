
import numpy as np

from Grafo import Grafo


if __name__ == '__main__':
	aristas = [
		(0, 1), (0, 3), (1, 2), (1, 4), (1, 5), (2, 3),
        (3, 1), (4, 3), (4, 5), (5, 3), (5, 0)
	]

	n = 6
	grafo = Grafo(n, aristas)

	grafo.menorCamino(0, 2)