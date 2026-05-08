# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.

    Args:
        items: Lista de items (strings)

    Returns:
        Un diccionario con cada item y su cantidad
    """
    #pass  # Reemplazar con tu implementación
    inventario = {}
    for item in items:
        if item in inventario:
            #si, ya existe suma 1 
            inventario[item] = inventario[item] + 1
        else:
            inventario[item] = 1
    return inventario  


def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """
    #pass  # Reemplazar con tu implementación
    for item in items:
        if item in inventario:
            #aumenta lo que ya tenia
            inventario[item] = inventario[item] + 1
        else:
            inventario[item] = 1
    return inventario


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas: si un item se quiere
    restar más veces que su cantidad disponible, debe quedar en 0 y las
    solicitudes extra deben ser ignoradas.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a decrementar

    Returns:
        El inventario actualizado (sin valores negativos)
    """
    #pass  # Reemplazar con tu implementación
    for item in items:
        if item in inventario:
            cantidad_actual = inventario[item]
            if cantidad_actual > 0:
                inventario[item] = cantidad_actual - 1
    return inventario


def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.

    Args:
        inventario: Diccionario con el inventario actual
        item: String con el nombre del item a eliminar

    Returns:
        El inventario actualizado (o sin cambios si el item no existe)
    """
    #pass  # Reemplazar con tu implementación
    if item in inventario:
        del inventario[item]
    return inventario


def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.

    Args:
        inventario: Diccionario con el inventario

    Returns:
        Lista de tuplas (item, cantidad) con cantidad > 0
    """
    #pass  # Reemplazar con tu implementación
    lista_resultado = []
    # .tems() nos da la pareja (clae , valor) en cada vuelta
    for nombre , cantidad in inventario.items():
        if cantidad > 0 :
            tupla_item = (nombre , cantidad)
            lista_resultado.append(tupla_item)
    return lista_resultado

def find_max_value(diccionario):
    """
    Recibe un diccionario de nombres y puntajes, y retorna la clave
    (nombre) con el valor (puntaje) más alto. Si el diccionario está
    vacío, retorna "".

    Args:
        diccionario: Diccionario {nombre: puntaje}

    Returns:
        String con la clave de mayor valor, o "" si el dict está vacío

    Ejemplo:
        find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78}) -> 'Emma'
    """
    #pass  # Reemplazar con tu implementación
    if not diccionario : #si está vacío 
        return ""
    nombre_maximo = ""
    puntaje_maximo = float("-inf") 

    for nombre , puntaje in diccionario.items():
        if puntaje > puntaje_maximo:
            puntaje_maximo = puntaje
            nombre_maximo = nombre
    return nombre_maximo


def reverse_dict(diccionario):
    """
    Invierte un diccionario: cada valor pasa a ser clave, y cada clave
    pasa a ser valor. Si varias claves comparten el mismo valor, sus
    nombres se concatenan (en el orden en que aparecen).

    Args:
        diccionario: Diccionario original

    Returns:
        Nuevo diccionario invertido

    Ejemplo:
        reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2})
        -> {1: 'a', 2: 'be', 3: 'cd'}
    """
    #pass  # Reemplazar con tu implementación
    nuevo_dict = {}
    for nombre , valor in diccionario.items():
        if valor in nuevo_dict:
            #si el 
            nuevo_dict[valor] = nuevo_dict[valor] + nombre
        else:
            #si es la primera vez que veo este valor lo creo
            nuevo_dict[valor] = nombre
    return nuevo_dict


def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista y lo retorna
    como un diccionario {palabra: cantidad}.

    Args:
        palabras: Lista de palabras (strings). También debe soportar
                  un string vacío retornando un diccionario vacío.

    Returns:
        Diccionario con la frecuencia de cada palabra

    Ejemplo:
        word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
        -> {'apple': 3, 'banana': 2, 'orange': 1}
    """
    #pass  # Reemplazar con tu implementación
    #si recibe un string vacío en vez de lista devuelve dict vacio
    if palabras == "":
        return {}
    frecuencia = {}
    for p in palabras:
        if p in frecuencia:
            frecuencia[p] = frecuencia[p] + 1
        else:
            frecuencia[p] = 1
    return frecuencia


def find_biggest_expense(gastos):
    """
    Recibe un diccionario donde cada clave es una categoría y el valor
    una lista de gastos (números). Retorna la categoría con el
    promedio más alto. Si el diccionario está vacío, retorna "".

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        String con la categoría de mayor promedio, o "" si vacío

    Ejemplo:
        find_biggest_expense({'Food': [60, 80, 100],
                              'Transport': [10, 1, 2],
                              'Games': [10, 20, 30]}) -> 'Food'
    """
    #pass  # Reemplazar con tu implementación
    if not gastos:
        return ""
    mejor_categoria = ""
    max_promedio = -1

    for categoria , lista_gastos in gastos.items():
        #calcula promediomanual suma / cantidad
        suma = 0
        for g in lista_gastos:
            suma += g

        promedio = suma / len(lista_gastos)

        if promedio > max_promedio:
            max_promedio = promedio
            mejor_categoria = categoria
    return mejor_categoria


def sum_expenses(gastos):
    """
    Recibe un diccionario de categorías con listas de gastos y retorna
    un nuevo diccionario con la suma total de los gastos por categoría.

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        Diccionario {categoria: suma_total}

    Ejemplo:
        sum_expenses({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]})
        -> {'Food': 240, 'Transport': 13, 'Games': 60}
    """
    #pass  # Reemplazar con tu implementación
    resultado = {}
    for categoria , lista_gastos in gastos.items():
        suma_total = 0
        for g in lista_gastos:
            suma_total += g
        resultado[categoria] = suma_total
    return resultado



def sum_expenses_by_type(gastos):
    """
    Recibe un diccionario de categorías cuyos valores son listas de
    tuplas (tipo, monto). Retorna un nuevo diccionario con la suma
    de montos agrupada por tipo (no por categoría).

    Args:
        gastos: Diccionario {categoria: [(tipo, monto), ...]}

    Returns:
        Diccionario {tipo: suma_total_del_tipo}

    Ejemplo:
        sum_expenses_by_type({
            'Food': [("A", 60), ("B", 100), ("A", 20)],
            'Transport': [("A", 10), ("B", 50), ("C", 5)],
            'Games': [("A", 6), ("B", 24), ("C", 99)]
        })
        -> {'A': 96, 'B': 174, 'C': 104}
    """
    #pass  # Reemplazar con tu implementación
    totales_por_tipo = {}

    for lista_tuplas in gastos.values():
        for tipo , monto in lista_tuplas:
            if tipo in totales_por_tipo:
                totales_por_tipo[tipo] += monto
            else:
                totales_por_tipo[tipo] = monto
    return totales_por_tipo
