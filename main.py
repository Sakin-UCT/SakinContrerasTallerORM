from funciones import (
    insertar_sala,
    consultar_salas,
    registrar_reserva,
    consultar_reservas,
    cancelar_reserva
)
from datetime import date

while True:

    print("\n========= SISTEMA DE RESERVAS =======")
    print("1. Registrar sala")
    print("2. Consultar salas")
    print("3. Registrar reserva")
    print("4. Consultar reservas")
    print("5. Cancelar reserva")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la sala: ")

        try:
            capacidad = int(input("Ingrese la capacidad: "))
            insertar_sala(nombre, capacidad)
        except ValueError:
            print("Error: debe ingresar un número.")

    elif opcion == "2":
        consultar_salas()

    elif opcion == "3":
        estudiante = input("Nombre del estudiante: ")

        try:
            sala_id = int(input("ID de la sala: "))
        except ValueError:
            print("Error: el ID debe ser un número.")

        fecha_texto = input("Fecha AAAA-MM-DD")

        try:
            fecha = date.fromisoformat(fecha_texto)
            registrar_reserva(estudiante, sala_id, fecha)

        except ValueError:
            print("Error: ingrese fecha valida AAAA-MM-DD")


    elif opcion == "4":

        consultar_reservas()

    elif opcion == "5":

        try:
            id_reserva = int(input("Ingrese el ID de la reserva: "))
            cancelar_reserva(id_reserva)

        except ValueError:
            print("Error: debe ingresar un número.")

    elif opcion == "0":

        print("ZZZ")
        break

    else:

        print("Opción no válida. Intente nuevamente.")
