
import numpy as np

from DiGrafoPonderado import DiGrafoPonderado


if __name__ == '__main__':
	aristas = [
		(0, 1, 3), (0, 3, 6), (1, 2, 1), (1, 4, 2), (1, 5, 1), (2, 3, 2),
        (3, 1, 3), (4, 3, 3), (4, 5, 2), (5, 3, 1), (5, 0, 5)
	]

	n = 6
	grafo = DiGrafoPonderado(n, aristas)

	grafo.printGrafo()