import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

from Car import Car
from Obstacle import Obstacle
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

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image = pygame.image.load(image_path)
        car = Car(0, 0)
        # car1 = Car(15, 15)
        # obs = Obstacle(100, 100, 10, 60)
        car_sprite = Car_sprite(200, 200)
        # all_sprites = pygame.sprite.Group()
        # all_sprites.add(obs)
        car_sprites = pygame.sprite.Group()
        car_sprites.add(car_sprite)

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

            ###
            #
            # if pressed[pygame.K_w]:
            #     if car1.velocity.x < 0:
            #         car1.acceleration = car1.brake_deceleration
            #     else:
            #         car1.acceleration += 100 * dt
            # elif pressed[pygame.K_s]:
            #     if car1.velocity.x > 0:
            #         car1.acceleration = -car1.brake_deceleration
            #     else:
            #         car1.acceleration -= 100 * dt
            # elif pressed[pygame.K_SPACE]:
            #     if abs(car1.velocity.x) > dt * car1.brake_deceleration:
            #         car1.acceleration = -copysign(car1.brake_deceleration, car1.velocity.x)
            #     else:
            #         car1.acceleration = -car1.velocity.x / dt
            # else:
            #     if abs(car1.velocity.x) > dt * car1.free_deceleration:
            #         car1.acceleration = -copysign(car1.free_deceleration, car1.velocity.x)
            #     else:
            #         if dt != 0:
            #             car1.acceleration = -car1.velocity.x / dt
            # car1.acceleration = max(-car1.max_acceleration, min(car1.acceleration, car1.max_acceleration))
            #
            # if pressed[pygame.K_d]:
            #     car1.steering -= 80 * dt
            # elif pressed[pygame.K_a]:
            #     car1.steering += 80 * dt
            # else:
            #     car1.steering = 0
            # car1.steering = max(-car1.max_steering, min(car1.steering, car1.max_steering))
            #
            ###

            # if pressed[pygame.K_y]:
            #     if car_sprite.velocity.x < 0:
            #         car_sprite.acceleration = car_sprite.brake_deceleration
            #     else:
            #         car_sprite.acceleration += 100 * dt
            # elif pressed[pygame.K_h]:
            #     if car_sprite.velocity.x > 0:
            #         car_sprite.acceleration = -car_sprite.brake_deceleration
            #     else:
            #         car_sprite.acceleration -= 100 * dt
            # elif pressed[pygame.K_SPACE]:
            #     if abs(car_sprite.velocity.x) > dt * car_sprite.brake_deceleration:
            #         car_sprite.acceleration = -copysign(car_sprite.brake_deceleration, car_sprite.velocity.x)
            #     else:
            #         car_sprite.acceleration = -car_sprite.velocity.x / dt
            # else:
            #     if abs(car_sprite.velocity.x) > dt * car_sprite.free_deceleration:
            #         car_sprite.acceleration = -copysign(car_sprite.free_deceleration, car_sprite.velocity.x)
            #     else:
            #         if dt != 0:
            #             car_sprite.acceleration = -car_sprite.velocity.x / dt
            # car_sprite.acceleration = max(-car_sprite.max_acceleration, min(car_sprite.acceleration, car_sprite.max_acceleration))
            #
            # if pressed[pygame.K_j]:
            #     car_sprite.steering -= 80 * dt
            # elif pressed[pygame.K_g]:
            #     car_sprite.steering += 80 * dt
            # else:
            #     car_sprite.steering = 0
            # car_sprite.steering = max(-car_sprite.max_steering, min(car_sprite.steering, car_sprite.max_steering))

            ###
            # print(car_sprite.rect.center)
            # Logic
            car.update(dt)
            # car1.update(dt)
            # all_sprites.update()
            # car_sprites.update(dt)
            # Drawing
            self.screen.fill((0, 0, 0))
            rotated = pygame.transform.rotate(car_image, car.angle)
            rect = rotated.get_rect()
            rect = rotated.get_rect()
            # all_sprites.draw(self.screen)
            # car_sprites.draw(self.screen)
            # rotated1 = pygame.transform.rotate(car_image, car1.angle)
            # rotated2 = pygame.transform.rotate(car_sprite.image, car_sprite.angle)
            # rect1 = rotated1.get_rect()
            # rect2 = rotated2.get_rect(center=car_sprite.rect.center)
            i += 1
            if i % 120 == 0:
                print(f'car\naccel {car.acceleration}\nvelocity {car.velocity}\n'
                      f'steering {car.steering}\nposition {car.position}\nangle {car.angle}')
                print(f'car_sprite\naccel {car_sprite.acceleration}\nvelocity {car_sprite.velocity}\n'
                      f'steering {car_sprite.steering}\nposition {car_sprite.position}\nangle {car_sprite.angle}\n\n')
                print(car_sprite.position, Vector2(car_sprite.rect.centerx, car_sprite.rect.centery))
            self.screen.blit(rotated, car.position * ppu - (rect.width / 2, rect.height / 2))
            # self.screen.blit(rotated1, car1.position * ppu - (rect1.width / 2, rect1.height / 2))
            # self.screen.blit(rect2, car_sprite.rect)
            pygame.display.flip()

            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
