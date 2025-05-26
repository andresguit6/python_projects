"""import pygame
import random
import math
from pygame import mixer

# inicializar a pygame
pygame.init()

# para mostrar la pantalla pygame.display.set_mode((800,600)) siempre va en tuplas
pantalla = pygame.display.set_mode((800,600))
# si se ejecuta solo este codigo muestra 1segundo la pantalla

# para colocarle nombre a la ventana
pygame.display.set_caption("Invación espacíal")
# descargo la imagen en png de flaticon y la guardo donde estoy trabajando (dia 10)
icono = pygame.image.load("ovni-volando.png")
# para mostrar el icono en la pantalla
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")


# agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)  # para subir o bajar volumen de 0 a 1
mixer.music.play(-1)


# variables del jugador
img_jugador = pygame.image.load("nave_espacial.png")
# para que quede a la mitad se divide 800en dos que es el tamaño de pantalla, da 400 y a eso se le resta la
# mitad de lo que mide la imagen si mide 64/2 = 32 entonces 400-32 = 368 jugador_X = 368
# si se quiere que la imagen quede tocando el inicio de pantalla (600 el total de la pantalla - altura jugador 64)
# 600 - 64 = 536
jugador_X = 368
jugador_y = 500
jugador_x_cambio = 0


# variables del enemigo
img_enemigo = []
enemigo_X = []
enemigo_y = []
enemigo_X_cambio = []
enemigo_Y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_X.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_X_cambio.append(0.5)
    enemigo_Y_cambio.append(50)

# variables de la bala
img_bala = pygame.image.load("bala.png")
bala_X = 0
bala_y = 500
bala_X_cambio = 0
bala_Y_cambio = 0.8
bala_visible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

#  texto final de juego
fuente_final = pygame.font.Font("freesansbold.ttf", 40)


def texto_final():
    mi_fuente_final = fuente_final.render("juego terminado", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


# funcion mostrar puntaje (asi se agrega texto en la pantalla)
def mostrar_texto(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))


# funcion jugador
def jugador(x,y):
    # para mostrar en pantalla
    pantalla.blit(img_jugador, (x,y))


# funcion enemigo
def enemigo(x,y, ene):
    # para mostrar en pantalla
    pantalla.blit(img_enemigo[ene], (x,y))


# funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_2 - y_1,2))
    if distancia < 27:
        return  True
    else:
        return False


# este codigo se ejecuta para que muestre la pantalla hasta que el usuario le de en la X
se_ejecuta = True
while se_ejecuta:
    # se coloca el RGB de pantalla (color)
    # para cambiar de color del fondo .fill(relleno) https://colorspire.com/rgb-color-wheel/ para mirar los colores
    # pantalla.fill((205, 144, 228)) # se pone al incio para que no tape nada, si se de ultimo tapa lo que se hace
    # si se quiere agregar solo color se hace lo que esta en RGB
    # si se quiere agregar un fondo se hace como imagen de fondo, se descarga la imagen se edita
    # para que sea los mismos pixeles y se importa

    # imagen de fondo
    pantalla.blit(fondo, (0,0))
    # iterar eventos
    for evento in pygame.event.get():

        # evento cerrar
        if evento.type == pygame.QUIT: # de esta manera se le dice que si el usuario seleciona la X salga
            se_ejecuta = False
        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:  # KEYDOWN para decirle al sistema cuando se preciona una tecla
            if evento.key == pygame.K_LEFT:  # le dice que se preciona la tecla izquierda
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_X = jugador_X
                    disparar_bala(bala_X,bala_y)

        # evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar ubicación del jugador
    jugador_X += jugador_x_cambio

    # mantener dentro de bordes al jugador
    if jugador_X <= 0:
        jugador_X = 0
    elif jugador_X >= 736:  # para que no pase de la pantalla (grande de pantalla - grande nave espacial)
        jugador_X = 736  # 800-64 = 736 (es 64 por que fue el tamaño de imagen que descargamos de flaticon)

    # modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_X[e] += enemigo_X_cambio[e]

    # mantener dentro de bordes al enemigo
        if enemigo_X[e] <= 0:
            enemigo_X_cambio[e] = 0.5
            enemigo_y[e] += enemigo_Y_cambio[e]
        elif enemigo_X[e] >= 736:
            enemigo_X_cambio[e] = -0.5
            enemigo_y[e] += enemigo_Y_cambio[e]

        # colision
        colision = hay_colision(enemigo_X[e], enemigo_y[e], bala_X, bala_y)
        if colision:
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_X[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_X[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_X, bala_y)
        bala_y -= bala_Y_cambio

    jugador(jugador_X,jugador_y)
    mostrar_texto(texto_x, texto_y)

    # actualizar
    pygame.display.update()"""