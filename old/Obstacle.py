import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 125, 125))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass


class Road(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

    def update(self):
        pass
        self.rect = pygame.draw.aaline(self.screen, (255, 255, 255),
                                       [10, 70],
                                       [290, 500])


# class Road(pygame.sprite.Sprite):
#     def __init__(self, screen, points):
#         pygame.sprite.Sprite.__init__(self)
#         self.screen = screen
#         self.points = points
#
#     def update(self):
#         pass
#         self.rect = pygame.draw.aalines(self.screen, (255, 255, 255), True,
#                                         self.points)