import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

from Car import Car
from Obstacle import Obstacle, Road
from Car_sprite import Car_sprite

GREEN = (0, 255, 0)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car")
        width = 1280
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # image_path = os.path.join(current_dir, "car.png")
        # car_image = pygame.image.load(image_path)
        car = Car(0, 0, self.screen)
        obs = Obstacle(150, 250, 100, 50)
        road = Road(self.screen)
        obs_sprite = pygame.sprite.Group()
        obs_sprite.add(obs)
        ppu = 32
        i = 0
        while not self.exit:
            dt = self.clock.get_time() / 1000.0
            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                if car.velocity.x < 0:
                    car.acceleration = car.brake_deceleration
                else:
                    car.acceleration += 100 * dt
            elif pressed[pygame.K_DOWN]:
                if car.velocity.x > 0:
                    car.acceleration = -car.brake_deceleration
                else:
                    car.acceleration -= 100 * dt
            elif pressed[pygame.K_SPACE]:
                if abs(car.velocity.x) > dt * car.brake_deceleration:
                    car.acceleration = -copysign(car.brake_deceleration, car.velocity.x)
                else:
                    car.acceleration = -car.velocity.x / dt
            else:
                if abs(car.velocity.x) > dt * car.free_deceleration:
                    car.acceleration = -copysign(car.free_deceleration, car.velocity.x)
                else:
                    if dt != 0:
                        car.acceleration = -car.velocity.x / dt
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))

            if pressed[pygame.K_RIGHT]:
                car.steering -= 80 * dt
            elif pressed[pygame.K_LEFT]:
                car.steering += 80 * dt
            else:
                car.steering = 0
            car.steering = max(-car.max_steering, min(car.steering, car.max_steering))

            # Logic
            obs_sprite.update()
            if pygame.Rect.colliderect(car.rect, obs.rect):
                car = Car(0, 0, self.screen)
            # if pylygon.Polygon.collidepoly()
            # Drawing

            self.screen.fill((0, 0, 0))
            # line = pygame.draw.aaline(self.screen, (255, 255, 255),
            #                           [10, 70],
            #                           [290, 55])
            road.update()
            car.update(dt)
            obs_sprite.draw(self.screen)
            if pygame.Rect.colliderect(car.rect, road.rect):
                car = Car(0, 0, self.screen)
            i += 1
            if i % 120 == 0:
                # print(f'rect {car.rect.center}, pos {car.position}')
                print(f'car {car.rect}, obs {obs.rect}')
            pygame.display.flip()

            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
