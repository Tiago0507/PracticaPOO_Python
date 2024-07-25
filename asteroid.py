from astronomical_object import AstronomicalObject

class Asteroid(AstronomicalObject):
    def __init__(self, image_path, mass, distance, orbit_speed):
        super().__init__(image_path=image_path, mass=mass, distance=distance, orbit_speed=orbit_speed)

    # Sobreescritura de método abstracto. No se hace nada porque el asteroide no tendrá campo magnético
    def generate_magnetic_field(self, screen):
        pass