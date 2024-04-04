Aumentando la cantidad de hilos, el tiempo tiende a disminuir; en mi caso, a medida que se aumentaban los hilos, el tiempo seguía una tendencia a la baja. Sin embargo, llegaba un punto donde los registros de los tiempos se volvían inestables, y los resultados no mostraban un patrón claro.

Se probó con un vector de 1_000_000 elementos, con 300 y 500 hilos y la tendencia fue clara: el rendimiento dejaba de mejorar a partir de unos 150 hilos, momento en el cual la región inestable iniciaba. Se utilizó un conjunto de un millón de datos, ya que si se utilizaba uno menor, el tiempo era tan pequeño que no se podía apreciar la diferencia entre los tiempos de ejecución.