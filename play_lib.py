from math import sin, radians, degrees, cos, copysign

import play

# ЭКРАН
from play import line, pygame, Circle
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
        # self.radar = BallRadar(self.x, self.y, 10)
        # self.radar = Radar(self.x, self.y, 100)
        self.ball = play.new_circle(x=self.x, y=self.y, transparency=30)
        self.ball.start_physics(stable=True, obeys_gravity=False, bounciness=0)
        self.position = Vector2(self.x, self.y)
        self.velocity = Vector2(0, 0)
        self.angle = 0
        self.max_acceleration = 30
        self.max_steering = 50
        self.max_velocity = 50
        self.brake_deceleration = 50
        self.free_deceleration = 10
        self.acceleration = 0.0
        self.steering = 0.0

    def update(self):
        self.velocity.x += self.acceleration * dt
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
        if self.steering:
            turning_radius = self.width / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(self.angle) * dt
        self.angle += degrees(angular_velocity) * dt
        self.x, self.y = self.position
        self.steering = max(-self.max_steering, min(self.steering, self.max_steering))
        self.ball.x = self.position.x
        self.ball.y = self.position.y
        # self.radar.update(self.position, self.angle)


# class Radar():
#     def __init__(self, x, y, length):
#         super().__init__()
#         self.line = play.new_line(x=x, y=y, length=100, angle=45)
#         # self.line2 = play.new_line(x=self.x, y=self.y, length=100, angle=0)
#         # self.line3 = play.new_line(x=self.x, y=self.y, length=100, angle=-45)
#         # self.lines = [self.line1, self.line2, self.line3]
#         # self.position = Vector2(self.x, self.y)
#         self.line.start_physics(can_move=True, stable=True, obeys_gravity=False)
#         # for line in self.lines:
#         #     line.start_physics(stable=True, bounciness=0, friction=100, obeys_gravity=False)
#         #     print(line.x, line.y)
#
#     def update(self, position, angle):
#         self.line.x = position.x
#         self.line.y = position.y
#         # self.line.angle = angle


# class BallRadar(Circle):
#     def __init__(self, x, y, radius):
#         super().__init__(x, y, radius)
#         self.x = x
#         self.y = y
#         self.line = play.new_line(x=self.x, y=self.y, length=100, angle=45)
#         # self.line2 = play.new_line(x=self.x, y=self.y, length=100, angle=0)
#         # self.line3 = play.new_line(x=self.x, y=self.y, length=100, angle=-45)
#         # self.lines = [self.line1, self.line2, self.line3]
#         self.position = Vector2(self.x, self.y)
#         self.line.start_physics(can_move=True, stable=True, obeys_gravity=False)
#         # for line in self.lines:
#         #     line.start_physics(stable=True, bounciness=0, friction=100, obeys_gravity=False)
#         #     print(line.x, line.y)
#
#     def update(self, position, angle):
#         self.line.x = position.x * 2
#         self.line.y = position.y
#         self.angle = angle + 45


platform = Car(color='brown', x=100, y=-250, width=150, height=55)
platform2 = play.new_box()


@play.when_program_starts
def start():
    platform.start_physics(
        can_move=True, stable=True, obeys_gravity=False
    )
    platform.show()
    # line1 = play.new_line(x=10, y=10, length=600, angle=45)
    platform2.start_physics(can_move=True, stable=True, obeys_gravity=False)
    platform2.show()


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
    platform2.turn(0.1)
    i=0
    i+=1
    print(i)
    if play.key_is_pressed('w'):
        if platform.velocity.x < 0:
            platform.acceleration = platform.brake_deceleration
        else:
            platform.acceleration += 30 * dt
    elif play.key_is_pressed('s'):
        if platform.velocity.x > 0:
            platform.acceleration = -platform.brake_deceleration
        else:
            platform.acceleration -= 30 * dt
    else:
        if abs(platform.velocity.x) > dt * platform.free_deceleration:
            platform.acceleration = -copysign(platform.free_deceleration, platform.velocity.x)
        else:
            if dt != 0:
                platform.acceleration = -platform.velocity.x / dt

    if play.key_is_pressed('d'):
        platform.steering -= 30 * dt
    elif play.key_is_pressed('a'):
        platform.steering += 30 * dt
    else:
        platform.steering = 0



    # pressed = pygame.key.get_pressed()
    #
    # if pressed[pygame.K_UP]:
    #     if platform.physics.x_speed < 0:
    #         platform.acceleration = platform.brake_deceleration
    #     else:
    #         platform.acceleration += 100 * dt
    # elif pressed[pygame.K_DOWN]:
    #     if platform.physics.x_speed > 0:
    #         platform.acceleration = -platform.brake_deceleration
    #     else:
    #         platform.acceleration -= 100 * dt
    # elif pressed[pygame.K_SPACE]:
    #     if abs(platform.physics.x_speed) > dt * platform.brake_deceleration:
    #         platform.acceleration = -copysign(platform.brake_deceleration, platform.physics.x_speed)
    #     else:
    #         platform.acceleration = -platform.physics.x_speed / dt
    # else:
    #     if abs(platform.physics.x_speed) > dt * platform.free_deceleration:
    #         platform.acceleration = -copysign(platform.free_deceleration, platform.physics.x_speed)
    #     else:
    #         if dt != 0:
    #             platform.acceleration = -platform.physics.x_speed / dt
    # platform.acceleration = max(-platform.max_acceleration, min(platform.acceleration, platform.max_acceleration))

    # if pressed[pygame.K_RIGHT]:
    #     platform.steering -= 80 * dt
    # elif pressed[pygame.K_LEFT]:
    #     platform.steering += 80 * dt
    # else:
    #     platform.steering = 0
    # platform.steering = max(-platform.max_steering, min(platform.steering, platform.max_steering))

    platform.update()
    if platform.ball.is_touching(platform2):
        print('touch')


play.start_program()
