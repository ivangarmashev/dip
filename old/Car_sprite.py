import pygame
from pygame.math import Vector2
from math import sin, radians, degrees, copysign


class Car_sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0.0, length=4, max_steering=50, max_acceleration=30.0):
        # pygame.sprite.Sprite.__init__(self)
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # image_path = os.path.join(current_dir, "car.png")
        # car_image = pygame.image.load(image_path)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 10))
        self.image.fill((0, 210, 0))
        # self.image = car_image
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 20
        self.brake_deceleration = 50
        self.free_deceleration = 10
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # self.speedx = 1
        # self.speedy = 1

        self.acceleration = 0.0
        self.steering = 0.0

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt