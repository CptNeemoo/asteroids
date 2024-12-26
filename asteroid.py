import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            right = self.velocity.rotate(angle)
            left = self.velocity.rotate(-angle)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            left_ast = Asteroid(self.position.x, self.position.y, smaller_radius)
            left_ast.velocity = left * 1.2
            right_ast = Asteroid(self.position.x, self.position.y, smaller_radius)
            right_ast.velocity = right * 1.2