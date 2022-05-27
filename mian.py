import pygame

# Inicializar a pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption('Invasión espacial')
icono = pygame.image.load('./img/ovni.png')
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load('./img/rocket.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0

# Funcion jugador


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop del juego
se_ejecuta = True

while se_ejecuta:

    # Cambiando el color de la pantalla
    pantalla.fill((205, 144, 228))

    # Iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento precionar flechas
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar movimiento
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0

    elif jugador_x >= 736:
        jugador_x = 736

    # Pintando al jugador
    jugador(jugador_x, jugador_y)

    # Actualizar pantalla
    pygame.display.update()
