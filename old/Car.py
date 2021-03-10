import os
from math import sin, radians, degrees

import pygame
from pygame.math import Vector2


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, angle=0.0, length=4, max_steering=50, max_acceleration=30.0):
        pygame.sprite.Sprite.__init__(self)
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 20
        self.brake_deceleration = 50
        self.free_deceleration = 10
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        self.image = pygame.image.load(image_path)
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotated.get_rect()
        self.acceleration = 0.0
        self.steering = 0.0
        self.screen = screen

    def update(self, dt):

        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotated.get_rect()
        self.rect.x, self.rect.y = self.position.x * 32 - self.rect.width / 2, self.position.y * 32 - self.rect.height / 2
        self.screen.blit(self.rotated, self.position * 32 - (self.rect.width / 2, self.rect.height / 2))
