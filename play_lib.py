import play

# ЭКРАН
play.set_backdrop('light blue')
# frames = 155 # частота кадров
# lose = play.new_text(words='YOU LOSE', font_size=100, color='red')
# win = play.new_text(words='YOU WIN', font_size=100, color='yellow')
# platform = play.new_box(color='brown', y=-250, width=150, height=15, angle=45)
ball = play.new_circle(color='green', y=-160, radius=15)

blocks = []


class Car(play.Box):
    # def __init__(self, color, y, width, height, angle):
    #     super().__init__(color=color, y=y, width=width, height=height, angle=angle)
    pass


class Radar(play.line):
    # def __init__(self, x, y, angle, length=100):
    #     super().__init__(x=x, y=y, angle=angle, length=length, transparency=50)
    pass


class Robot(Car, Radar):
    def __init__(self, color, x, y, width, height, angle_car, angle_line):
        super(Car).__init__(color='green')
        # super(Radar).__init__()
        # super(Radar).__init__(x, y, angle=angle_line)
        # self.car = Car(color, y, width, height, angle_car)(
        # self.radar = Radar(x, y, angle_line)


platform = Car(color='brown', y=-250, width=150, height=15, angle=5)
line1 = play.new_line(length=200, x=10, y=15, angle=45, thickness=10)
# robot = Robot('green', 12, 13, 20, 30, 45, 10)


@play.when_program_starts
def start():
    # платформа не поддается гравитации и управляется только с клавиатуры
    platform.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=1
    )
    line1.start_physics(stable=False, obeys_gravity=False, mass=100)
    # шарик не поддается гравитации, случайно перемещается по полю
    ball.start_physics(
        stable=False, x_speed=30, y_speed=30, obeys_gravity=False, bounciness=1, mass=10
    )

    # генерация блоков
    # for i in range(3):  # количество рядов
    #     while (block_x <= play.screen.right - 30):
    #         # for i in range(5):
    #         block = play.new_box(
    #             color='grey', x=block_x, y=block_y, width=110, height=30, border_color='dark grey', border_width=1
    #         )
    #         blocks.append(block)
    #         block_x = block_x + block.width
    #     block_x = play.screen.left + 75
    #     block_y = block.y - block.height

    line1.show()
    platform.show()
    # lose.hide()
    # win.hide()


@play.repeat_forever
def game():
    # перемещение платформы
    if play.key_is_pressed('a'):
        platform.physics.x_speed = -20
    elif play.key_is_pressed('d'):
        platform.physics.x_speed = 20
        # platform.physics.y_speed = 10
        # ball.physics.y_speed = 0
    elif play.key_is_pressed('w'):
        platform.physics.y_speed = 20
    elif play.key_is_pressed('s'):
        platform.physics.y_speed = -20
    # elif play.key_is_pressed('q'):
    #     platform.acceleration(l=True)
    # elif play.key_is_pressed('e'):
    #     platform.acceleration(r=True)

    else:
        platform.physics.x_speed = 0
        platform.physics.y_speed = 0

    # удаление блоков
    # for b in blocks:
    #     if b.is_touching(ball):
    #         ball.physics.x_speed = -1 * ball.physics.x_speed
    #         ball.physics.y_speed = -1 * ball.physics.y_speed
    #         b.hide()
    #         blocks.remove(b)

    # проигрыш
    # if ball.y <= platform.y:
    #     lose.show()
    # выигрыш
    # if len(blocks) == 0:
    #     win.show()
    # await play.timer(seconds=1 / frames)  # частота смены кадров (пауза раз в несколько кадров)


play.start_program()
