# IMPORTAR PROYECTO DIA 8 UNO NUMEROS ,PY
from consola_turnos import *

# FUNCIONES QUE ADMINISTRAN EL FUNCIONAMIENTO DEL PROGRAMA
# INSTUCIONES PARA ELEGIR AREA


def pregunta_turno():
    selecion_cliente = input("Que turno desea:\n[P]: Perfumeria\n[F]: Farmacia\n[M]: Maquillaje\n[S]: Salir"
                             "\nIngrese aca su respuesta:").upper()
    elegir_turno(selecion_cliente)
    if selecion_cliente in ["P", "F", "M"]:
        otro_turno()


def elegir_turno(selecion_cliente):
    while True:
        if selecion_cliente == "P":
            turno_informativo = su_turno_es(perfume)
            turno_informativo(range)
            break

        elif selecion_cliente == "F":
            turno_informativo = su_turno_es(farma)
            turno_informativo(range)
            break

        elif selecion_cliente == "M":
            turno_informativo = su_turno_es(maquilla)
            turno_informativo(range)
            break

        elif selecion_cliente == "S":
            print("gracias por venir")
            break
        elif selecion_cliente != "P" != "F" != "M":
            print("Letra no valida ")
            return pregunta_turno()

    pass

# DECIDIR SI TOMAR NUEVOS TURNOS O SI FINALIZAR EL PROGRAMA


def otro_turno():
    otro_turn = input("desea tomar otro turno? S: SI, N: NO: ").upper()

    while True:
        if otro_turn == "S":
            pregunta_turno()
            break

        elif otro_turn == "N":
            print("gracias por venir")
            break
    pass


# programa
pregunta_turno()