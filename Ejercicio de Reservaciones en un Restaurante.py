# Lista de reservaciones inicial (nombre, cantidad de personas, hora)
reservaciones = [
    ("Juan Pérez", 4, "13:00"),
    ("María López", 2, "14:00"),
    ("Carlos Sánchez", 6, "15:00"),
    ("Ana Rodríguez", 3, "16:00"),
    ("Luis Fernández", 5, "17:00")
]

# Función para eliminar una reservación, con manejo de errores si no existe
def eliminar_reservacion(nombre):
    for reservacion in reservaciones:
        if reservacion[0] == nombre:
            reservaciones.remove(reservacion)
            print(f"Reservación de {nombre} eliminada.")
            return
    print(f"No se encontró una reservación bajo el nombre {nombre}.")

# Función para actualizar una reservación
def actualizar_reservacion(nombre, nuevas_personas=None, nueva_hora=None):
    for i, reservacion in enumerate(reservaciones):
        if reservacion[0] == nombre:
            nombre_cliente, personas, hora = reservacion
            personas = nuevas_personas if nuevas_personas else personas
            hora = nueva_hora if nueva_hora else hora
            
            # Validación de cantidad de personas
            if personas > 10:
                print("No se permite más de 10 personas por reservación.")
                return

            reservaciones[i] = (nombre_cliente, personas, hora)
            print(f"Reservación de {nombre_cliente} actualizada: {personas} personas, {hora}.")
            return
    print(f"No se encontró una reservación bajo el nombre {nombre}.")

# Función para imprimir todas las reservaciones
def mostrar_reservaciones():
    for reservacion in reservaciones:
        nombre_cliente, personas, hora = reservacion
        print(f"Reservación para {nombre_cliente}, {personas} personas a las {hora}.")

# Añadir una nueva reservación (valida que no exceda 10 personas)
def agregar_reservacion(nombre, personas, hora):
    if personas > 10:
        print("No se permite más de 10 personas por reservación.")
    else:
        reservaciones.append((nombre, personas, hora))
        print(f"Reservación para {nombre} añadida: {personas} personas, {hora}.")

# Mostrar las reservaciones actuales
print("Reservaciones actuales:")
mostrar_reservaciones()

# Eliminar una reservación
eliminar_reservacion("Carlos Sánchez")

# Mostrar reservaciones después de la eliminación
print("\nReservaciones después de la eliminación:")
mostrar_reservaciones()

# Actualizar una reservación existente
actualizar_reservacion("Juan Pérez", nuevas_personas=8)

# Mostrar reservaciones después de la actualización
print("\nReservaciones después de la actualización:")
mostrar_reservaciones()

# Intentar añadir una reservación con más de 10 personas
agregar_reservacion("Sofía González", 12, "18:00")

# Mostrar reservaciones finales
print("\nReservaciones finales:")
mostrar_reservaciones()
