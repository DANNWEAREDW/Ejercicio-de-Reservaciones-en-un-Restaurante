# Ejercicio-de-Reservaciones-en-un-Restaurante
El código de reservaciones en un restaurante gestiona una lista de reservaciones donde cada reservación está representada por una tupla que incluye el nombre del cliente, la cantidad de personas y la hora de la reserva.


Este proyecto implementa un sistema básico de gestión de reservaciones para un restaurante. Utiliza Python para administrar una lista de reservaciones, permitiendo añadir, eliminar, y actualizar reservas de manera sencilla, con validaciones para el número máximo de personas por reservación.

Funcionalidades
Añadir reservación: Permite agregar nuevas reservaciones asegurando que no excedan 10 personas por reserva.
Eliminar reservación: Elimina una reservación existente, asegurando que solo se eliminen reservaciones válidas.
Actualizar reservación: Actualiza la cantidad de personas o la hora de una reservación existente, con validaciones para asegurar que no exceda el límite permitido.
Mostrar reservaciones: Imprime todas las reservaciones actuales, proporcionando una vista completa del estado de las reservas.
Validaciones
Límite de 10 personas por reservación.
Manejo de errores si se intenta eliminar o actualizar una reservación que no existe.
Requisitos
Python 3.x
Uso
Clona este repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/gestion-reservaciones.git
Corre el script en tu entorno local:

bash
Copiar código
python gestion_restaurante.py
Sigue las instrucciones que aparecen en la consola para gestionar las reservaciones.

Ejemplos de Uso
Añadir una reservación:

python
Copiar código
agregar_reservacion("Carlos Gómez", 4, "19:00")
Eliminar una reservación:

python
Copiar código
eliminar_reservacion("Juan Pérez")
Actualizar una reservación:

python
Copiar código
actualizar_reservacion("María López", nuevas_personas=6)
Contribución
¡Las contribuciones son bienvenidas! Si encuentras algún error o deseas mejorar el código, no dudes en crear un pull request o abrir un issue.

![image](https://github.com/user-attachments/assets/0e2309e1-1a5a-4198-ae39-101580d0cc4a)

![image](https://github.com/user-attachments/assets/56f36d33-65b8-45f4-b8f4-306501b97d60)

