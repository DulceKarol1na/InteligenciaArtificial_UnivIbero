# deque significa "double-ended queue" o cola de doble extremo.
# Se importa deque del módulo collections.
from collections import deque

# Inicio de Base de conocimiento
# Definir las estaciones y sus distancias y tiempos
estaciones = [
    'Armenia', 'Bogotá', 'Cartagena', 'Medellín', 'Cali', 'Soacha', 'Granada', 'Silvania', 
    'Chinauta', 'Melgar', 'Cota', 'El Vino', 'San Francisco', 'La Vega', 'Villeta', 'Sincelejo', 
    'Circacia', 'Barrio Jupiter', 'La Pintada', 'Fredonia', 'Amaga', 'Caldas', 'Envigado'
]

distancias = {
    ('Bogotá', 'Soacha'): 17,
    ('Soacha', 'Granada'): 18,
    ('Granada', 'Silvania'): 22,
    ('Silvania', 'Chinauta'): 19,
    ('Chinauta', 'Melgar'): 35,
    ('Melgar', 'Armenia'): 164,
    ('Bogotá', 'Cota'): 22,
    ('Cota', 'El Vino'): 15,
    ('El Vino', 'San Francisco'): 11,
    ('San Francisco', 'La Vega'): 11,
    ('La Vega', 'Villeta'): 39,
    ('Villeta', 'Sincelejo'): 749,
    ('Sincelejo', 'Cartagena'): 188,
    ('Armenia', 'Circacia'): 12,
    ('Circacia', 'Barrio Jupiter'): 52,
    ('Barrio Jupiter', 'La Pintada'): 34,
    ('La Pintada', 'Fredonia'): 34,
    ('Fredonia', 'Amaga'): 23,
    ('Amaga', 'Caldas'): 13,
    ('Caldas', 'Envigado'): 12,
    ('Envigado', 'Sincelejo'): 479,
    ('Sincelejo', 'Cartagena'): 188,
    # Conexiones originales
    ('Armenia', 'Bogotá'): 285,
    ('Armenia', 'Cartagena'): 910,
    ('Bogotá', 'Cartagena'): 1028,
    ('Armenia', 'Medellín'): 260,
    ('Bogotá', 'Medellín'): 420,
    ('Medellín', 'Cartagena'): 630,
    ('Armenia', 'Cali'): 180,
    ('Cali', 'Bogotá'): 300,
    ('Cali', 'Medellín'): 250
}

tiempos = {
    ('Bogotá', 'Soacha'): 0.17,
    ('Soacha', 'Granada'): 0.18,
    ('Granada', 'Silvania'): 0.22,
    ('Silvania', 'Chinauta'): 0.19,
    ('Chinauta', 'Melgar'): 0.35,
    ('Melgar', 'Armenia'): 1.64,
    ('Bogotá', 'Cota'): 0.22,
    ('Cota', 'El Vino'): 0.15,
    ('El Vino', 'San Francisco'): 0.11,
    ('San Francisco', 'La Vega'): 0.11,
    ('La Vega', 'Villeta'): 0.39,
    ('Villeta', 'Sincelejo'): 7.49,
    ('Sincelejo', 'Cartagena'): 1.88,
    ('Armenia', 'Circacia'): 0.12,
    ('Circacia', 'Barrio Jupiter'): 0.52,
    ('Barrio Jupiter', 'La Pintada'): 0.34,
    ('La Pintada', 'Fredonia'): 0.34,
    ('Fredonia', 'Amaga'): 0.23,
    ('Amaga', 'Caldas'): 0.13,
    ('Caldas', 'Envigado'): 0.12,
    ('Envigado', 'Sincelejo'): 4.70,
    ('Sincelejo', 'Cartagena'): 1.83,
    # Tiempos originales
    ('Armenia', 'Bogotá'): 3,
    ('Armenia', 'Cartagena'): 9,
    ('Bogotá', 'Cartagena'): 11,
    ('Armenia', 'Medellín'): 3,
    ('Bogotá', 'Medellín'): 5,
    ('Medellín', 'Cartagena'): 6,
    ('Armenia', 'Cali'): 2,
    ('Cali', 'Bogotá'): 3,
    ('Cali', 'Medellín'): 2.5
}

# Agregar el origen y el destino y se asegura que todas las rutas en la base de conocimiento sean bidireccionales.
for (origen, destino) in list(distancias.keys()):
    distancias[(destino, origen)] = distancias[(origen, destino)]
    tiempos[(destino, origen)] = tiempos[(origen, destino)]

# Fin de Base de conocimiento

# Inicio de Reglas lógicas

# Función para expandir nodos
def expandir_nodos(nodo_actual):
    vecinos = []
    for estacion in estaciones:
        if (nodo_actual, estacion) in distancias:
            vecinos.append(estacion)
    return vecinos

# Función para evaluar si un movimiento es válido
def es_movimiento_valido(nodo_actual, vecino):
    return (nodo_actual, vecino) in distancias

# Función para calcular el costo de moverse de un nodo a otro 
def calcular_costo(nodo_actual, vecino):
    # Buscar en el diccionario distancias la distancia entre el nodo_actual y el vecino.
    distancia = distancias[(nodo_actual, vecino)]
    # Buscar en el diccionario tiempos el tiempo entre el nodo_actual y el vecino.
    tiempo = tiempos[(nodo_actual, vecino)]
    return distancia, tiempo

# Fin de Reglas lógicas

# Inicio del análisis para encontrar la ruta más corta
# Función para encontrar la mejor ruta usando BFS
def encontrar_mejor_ruta(origen, destino):
    if origen == destino:
        return [origen], 0, 0

    # Cola para BFS (Breadth-First Search, Búsqueda en Amplitud)
    cola = deque([(origen, [origen], 0, 0)])  # (nodo_actual, ruta, distancia_total, tiempo_total)
    visitados = set()

    while cola:
        nodo_actual, ruta, distancia_total, tiempo_total = cola.popleft()

        # Si el nodo actual ya ha sido visitado, continuar con la siguiente iteración del bucle
        if nodo_actual in visitados:
            continue

        # Marcar el nodo actual como visitado
        visitados.add(nodo_actual)

        # Expandir los nodos vecinos del nodo actual
        for vecino in expandir_nodos(nodo_actual):
            # Verificar si el movimiento hacia el vecino es válido
            if es_movimiento_valido(nodo_actual, vecino):
                # Crear una nueva ruta añadiendo el vecino a la ruta actual
                nueva_ruta = ruta + [vecino]
                # Calcular la distancia y el tiempo de moverse al vecino
                nueva_distancia, nuevo_tiempo = calcular_costo(nodo_actual, vecino)
                # Actualizar la distancia total acumulada y el tiempo total acumulado
                distancia_total_actualizada = distancia_total + nueva_distancia
                tiempo_total_actualizado = tiempo_total + nuevo_tiempo

                # Si el vecino es el destino, retornar la ruta encontrada junto con la distancia y el tiempo total
                if vecino == destino:
                    return nueva_ruta, distancia_total_actualizada, tiempo_total_actualizado

                # Encolar el vecino junto con la nueva ruta, distancia y tiempo actualizados
                cola.append((vecino, nueva_ruta, distancia_total_actualizada, tiempo_total_actualizado))

    # Si la cola se vacía y no se ha encontrado el destino, retornar None e infinitos para distancia y tiempo
    return None, float('inf'), float('inf')

# Fin del análisis para encontrar la ruta más corta

# Ejemplo de uso
origen = 'Pasto'
destino = 'Cartagena'

ruta, distancia, tiempo = encontrar_mejor_ruta(origen, destino)
if ruta:
    print(f"La mejor ruta de {origen} a {destino} es: {' -> '.join(ruta)}")
    print(f"Distancia total: {distancia} km")
    print(f"Tiempo total: {tiempo} horas")
else:
    print(f"No hay ruta disponible de {origen} a {destino}")
