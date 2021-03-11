from math import sin, radians, degrees, cos, copysign

import play

# ЭКРАН
from play import line, pygame
from pygame.math import Vector2

play.set_backdrop('light blue')
# frames = 155 # частота кадров
# lose = play.new_text(words='YOU LOSE', font_size=100, color='red')
# win = play.new_text(words='YOU WIN', font_size=100, color='yellow')
# platform = play.new_box(color='brown', y=-250, width=150, height=15, angle=45)
# ball = play.new_circle(color='green', y=-160, radius=15)

blocks = []
dt = 60 / 1000

class Car(play.Box):
    def __init__(self, color, x, y, width, height):
        super().__init__(color=color, x=x, y=y, width=width, height=height)
        self.x = x
        self.y = y
        self.radar = Radar(self.x+(self.width/2), self.y, 100)

        ###
        # self.position = Vector2(self.x, self.y)
        # self.velocity = Vector2(0.0, 0.0)
        self.angle = 0
        self.length = width
        self.max_acceleration = 30
        self.max_steering = 50
        self.max_velocity = 20
        self.brake_deceleration = 50
        self.free_deceleration = 10
        self.acceleration = 0.0
        self.steering = 0.0

    def update(self):

        ###
        self.physics.x_speed += self.acceleration
        # self.velocity += (self.acceleration, 0)
        self.physics.x_speed = max(-self.max_velocity, min(self.physics.x_speed, self.max_velocity))
        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.physics.x_speed / turning_radius
        else:
            angular_velocity = 0
        self.x += cos(-self.angle) * self.physics.x_speed - sin(-self.angle) * self.physics.y_speed
        self.y += sin(-self.angle) * self.physics.x_speed + cos(-self.angle) * self.physics.y_speed
        # self.position += self.velocity.rotate(-self.angle)
        self.angle += degrees(angular_velocity)
        # self.turn(self.angle)
        # self.rect = self.rotated.get_rect()
        # self.rect.x, self.rect.y = self.position.x * 32 - self.rect.width / 2, self.position.y * 32 - self.rect.height / 2
        # self.screen.blit(self.rotated, self.position * 32 - (self.rect.width / 2, self.rect.height / 2))
        ###

        self.radar.update(self.physics.x_speed, self.physics.y_speed)


class Radar(line):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.line1 = play.new_line(x=self.x, y=self.y, length=length, angle=0)
        self.line2 = play.new_line(x=self.x-15, y=self.y, length=length, angle=45)
        self.line3 = play.new_line(x=self.x-15, y=self.y, length=length, angle=-45)
        self.lines = [self.line1, self.line2, self.line3]
        for line in self.lines:
            line.start_physics(stable=True, bounciness=0, friction=100, obeys_gravity=False)

    def update(self, x_speed, y_speed):
        for line in self.lines:
            line.physics.x_speed = x_speed
            line.physics.y_speed = y_speed



# class Robot(Car, Radar):
#     def __init__(self, color, x, y, width, height, angle_car, angle_line):
#         super(Car).__init__(color='green')
#         # super(Radar).__init__()
#         # super(Radar).__init__(x, y, angle=angle_line)
#         # self.car = Car(color, y, width, height, angle_car)(
#         # self.radar = Radar(x, y, angle_line)


platform = Car(color='brown', x=100, y=-250, width=150, height=55)
# platform2 = Car(color='brown', y=-250, width=150, height=15)
# line1 = play.new_line(length=200, x=10, y=15, angle=45, thickness=10
# radar = Radar()
# robot = Robot('green', 12, 13, 20, 30, 45, 10)


@play.when_program_starts
def start():
    platform.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=1
    )
    platform.show()


@play.repeat_forever
def game():

    # перемещение платформы
    # if play.key_is_pressed('a'):
    #     platform.physics.x_speed = -20
    # elif play.key_is_pressed('d'):
    #     platform.physics.x_speed = 20
    # elif play.key_is_pressed('w'):
    #     platform.physics.y_speed = 20
    # elif play.key_is_pressed('s'):
    #     platform.physics.y_speed = -20
    # else:
    #     platform.physics.x_speed = 0
    #     platform.physics.y_speed = 0

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if platform.physics.x_speed < 0:
            platform.acceleration = platform.brake_deceleration
        else:
            platform.acceleration += 100 * dt
    elif pressed[pygame.K_DOWN]:
        if platform.physics.x_speed > 0:
            platform.acceleration = -platform.brake_deceleration
        else:
            platform.acceleration -= 100 * dt
    elif pressed[pygame.K_SPACE]:
        if abs(platform.physics.x_speed) > dt * platform.brake_deceleration:
            platform.acceleration = -copysign(platform.brake_deceleration, platform.physics.x_speed)
        else:
            platform.acceleration = -platform.physics.x_speed / dt
    else:
        if abs(platform.physics.x_speed) > dt * platform.free_deceleration:
            platform.acceleration = -copysign(platform.free_deceleration, platform.physics.x_speed)
        else:
            if dt != 0:
                platform.acceleration = -platform.physics.x_speed / dt
    platform.acceleration = max(-platform.max_acceleration, min(platform.acceleration, platform.max_acceleration))

    if pressed[pygame.K_RIGHT]:
        platform.steering -= 80 * dt
    elif pressed[pygame.K_LEFT]:
        platform.steering += 80 * dt
    else:
        platform.steering = 0
    platform.steering = max(-platform.max_steering, min(platform.steering, platform.max_steering))


    platform.update()


play.start_program()
