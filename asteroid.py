from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            self.random_angle = random.uniform(20,50)
            vect1 = self.velocity.rotate(self.random_angle)
            vect2 = self.velocity.rotate(-self.random_angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.aster1 = Asteroid(self.position.x,self.position.y,self.new_radius)
            self.aster1.velocity = vect1 * 1.2
            self.aster2 = Asteroid(self.position.x,self.position.y,self.new_radius)
            self.aster2.velocity = vect2 * 1.2
