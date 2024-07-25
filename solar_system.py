from star import Star
from planet import Planet
from asteroid import Asteroid
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sistema Solar")

sun = Star(image_path='images/sol.png', mass=2000, nucleo_status="Active")
mercury = Planet(image_path='images/mercurio.png', distance=100, orbit_speed=2, mass=50, nucleo_status="Inactive")
mars = Planet(image_path='images/marte.png', distance=180, orbit_speed=2, mass=250, nucleo_status="Active")
asteroid = Asteroid(image_path='images/asteroide.png', distance=210, orbit_speed=1, mass=20)

background_image = pygame.image.load("images/fondo.png").convert()
background_rect = background_image.get_rect()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Evento de salida
            running = False
            
    # Se dibuja el fondo
    screen.blit(background_image, background_rect)
    sun.draw(screen)
    mercury.draw(screen)
    mars.draw(screen)
    asteroid.draw(screen)

    # Aplicación del polimorfismo, cada tipo de objeto aplicará su propia sobreescritura del método
    # mercury.generate_magnetic_field(screen)
    # mars.generate_magnetic_field(screen)
    # sun.generate_magnetic_field(screen)

    sun.update()
    mercury.update()
    mars.update()
    asteroid.update()

    pygame.display.flip() # Sirve para actualizar los cambios automáticamente
    clock.tick(FPS) # Define los fotogramas por segundo para la ejecución del juego

pygame.quit()
            