import pygame
import math
# Importación de método abstracto para que las clases hijas obligatoriamente lo tengan que sobreescribir
from abc import ABC, abstractmethod

# ABC es para que esta clase se comporte como una clase abstracta
class AstronomicalObject(ABC):
    # Por defecto se definen algunos parámetros para que no haya problemas con la estrella, que no tendrá ni distancia
    # ni velocidad de órbita. Estos parámetros se pueden modificar en los constructores de las clases que sí necesitan esos parámetros
    def __init__(self, image_path, mass, distance=0, orbit_speed=0):
        # Variables de instancia
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        # Las imágenes en pygame tienen un rectángulo de área mínima donde estará la imagen
        self.angle = 0
        self.mass = mass
        self.distance = distance
        self.__orbit_speed = 0 # Aplicación de encapsulamiento
        self.orbit_speed = orbit_speed # Modificación por medio del setter
        

    # Forma Pythónica de hacer un get, es como si estuviéramos obteniendo directamente el atributo, pero realmente lo estamos
    # obteniendo por medio de una propiedad
    @property
    def orbit_speed(self):
        return self.__orbit_speed

    # Forma Pythónica de hacer un set, parece que modificáramos el atributo directamente, pero realmente lo estamos modificando
    # por acá
    @orbit_speed.setter
    def orbit_speed(self, value):
        if value >= 0 and value <= 10:
            self.__orbit_speed = value
        else:
            raise ValueError('Orbit value error')

    # Aumento del ángulo para que pueda generarse el movimiento circular
    def update(self):
        self.angle += self.orbit_speed

    def draw(self, screen):
        # Movimiento circular de órbita
        x = (screen.get_width() // 2) + (self.distance * math.cos(math.radians(self.angle)))
        y = (screen.get_height() // 2) + (self.distance * math.sin(math.radians(self.angle)))
        # Se define que el rectángulo que tienen las imágenes en pygame tendrá como ubicación el centro de la imagen con las 
        # coordenadas x e y
        self.rect.centerx = x
        self.rect.centery = y
        screen.blit(self.image, self.rect)

    @abstractmethod
    def generate_magnetic_field(self, screen):
        pass
        
        
    