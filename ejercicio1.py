import pygame
import random

# Inicializar Pygame
pygame.init()

# Tamaño de ventana
WIDTH, HEIGHT = 800, 600
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dibujo de puntos de colores - Sesión 2")

# Función para dibujar puntos aleatorios
def dibujar_puntos():
    for _ in range(200):  # cantidad de puntos
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        color = (
            random.randint(0, 255), 
            random.randint(0, 255), 
            random.randint(0, 255)
        )
        pygame.draw.circle(pantalla, color, (x, y), 3)

def main():
    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pantalla.fill((0, 0, 0))  # Fondo negro
        dibujar_puntos()

        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
