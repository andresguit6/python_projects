# escribir decorador
def su_turno_es(funcion):

    def turno(x):
        print("Su turno es:")
        print(next(funcion))
        print("En un momento sera atenido.")
    return turno


# escribir los generadores


def perfumeria(x):
    for x in range(1, 101):
        yield f"Perfumeria P-{x}"


def farmacia(x):
    for x in range(1, 101):
        yield f"Farmacia F-{x}"


def maquillaje(x):
    for x in range(1, 101):
        yield f"Maquillaje M-{x}"


perfume = perfumeria(range)
maquilla = maquillaje(range)
farma = farmacia(range)

su_turno_es(perfume)