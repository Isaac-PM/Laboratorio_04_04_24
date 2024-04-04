import threading
import random
import matplotlib.pyplot as plt
import time

suma_de_tiempos = 0

def ordenar_subvector(subvector, hilo):
    global suma_de_tiempos
    tiempo_inicio = time.time()
    subvector.sort()
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    suma_de_tiempos += tiempo_ejecucion
    # print(f"Hilo {hilo}: Subvector ordenado (Tiempo: {tiempo_ejecucion} segundos)")


def dividir_vector(vector, num_hilos):
    longitud_subvector = len(vector) // num_hilos
    subvectores = [
        vector[i : i + longitud_subvector]
        for i in range(0, len(vector), longitud_subvector)
    ]
    return subvectores


def unir_vectores(subvectores):
    vector_ordenado = [num for subvector in subvectores for num in subvector]
    return vector_ordenado


def ordenar_vector(vector, num_hilos):
    subvectores = dividir_vector(vector, num_hilos)
    threads = []

    for i, subvector in enumerate(subvectores):
        thread = threading.Thread(target=ordenar_subvector, args=(subvector, i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    vector_ordenado = unir_vectores(subvectores)
    # print(f"Vector ordenado final: {vector_ordenado}")


vector_grande_copia = [random.randint(1, 10) for _ in range(1_000_000)]
# totales = {}
# num_hilos = int(input("Ingrese la cantidad de hilos: "))
num_hilos_list = []
tiempo_list = []

for num_hilos in range(1, 300):
    vector_grande = list(vector_grande_copia)
    suma_de_tiempos = 0
    ordenar_vector(vector_grande, num_hilos)
    print(f"La suma de tiempo total es: {suma_de_tiempos} con {num_hilos} hilos")
    num_hilos_list.append(num_hilos)
    tiempo_list.append(suma_de_tiempos)

# Graficar los datos
plt.plot(num_hilos_list, tiempo_list)
plt.xlabel('Cantidad de Hilos')
plt.ylabel('Tiempo')
plt.title('Tiempo vs Cantidad de Hilos')
plt.grid(True)
plt.show()



"""
Entre mayor cantidad de hilos, 

"""