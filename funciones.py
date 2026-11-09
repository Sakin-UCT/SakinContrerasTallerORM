from conexion import Session
from modelos import Sala , Reserva
from sqlalchemy import select

def insertar_sala(nombre, capacidad):

    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacio")
        return

    if capacidad <= 0:
        print("Error: la capacidad debe ser mayor que cero")
        return

    with Session.begin() as session:

        sala = Sala(
            nombre=nombre,
            capacidad=capacidad
        )
        session.add(sala)

    print("Sala registrada correctamente")


def consultar_salas():
    with Session() as session:
        consulta = select(Sala)
        salas = session.scalars(consulta).all()

        if len(salas) == 0:
            print("No hay salas registradas.")
        else:
            print("\n--- LISTA DE SALAS ---")

            for sala in salas:
                print("----------------------")
                print("ID:", sala.id)
                print("Nombre:", sala.nombre)
                print("Capacidad:", sala.capacidad)
                print("Disponible:", sala.disponible)

def registrar_reserva(estudiante, sala_id, fecha):

    with Session.begin() as session:

        sala = session.get(Sala, sala_id)

        if sala is None:
            print("Error: la sala no existe.")
            return

        if sala.disponible == False:
            print("Error: la sala no está disponible.")
            return

        reserva = Reserva(
            estudiante=estudiante,
            sala_id=sala_id,
            fecha=fecha
        )

        session.add(reserva)
        sala.disponible = False

    print("Reserva registrada correctamente.")

def consultar_reservas():

    with Session() as session:

        consulta = select(Reserva)
        reservas = session.scalars(consulta).all()

        if len(reservas) == 0:
            print("No hay reservas registradas.")

        else:
            print("\n--- LISTA DE RESERVAS ---")

            for reserva in reservas:
                print("----------------------")
                print("ID:", reserva.id)
                print("Estudiante:", reserva.estudiante)
                print("Sala:", reserva.sala.nombre)
                print("Fecha:", reserva.fecha)

def cancelar_reserva(id_reserva):

    with Session.begin() as session:

        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            print("Error: no se encontró la reserva.")
            return

        sala = reserva.sala
        session.delete(reserva)
        sala.disponible = True

    print("Reserva cancelada correctamente.")