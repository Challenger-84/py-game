import pygame
from objects import RigidBody


class Platform(RigidBody, pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        RigidBody.__init__(self, affected_by_gravity=False)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, screen, scroll):
        self.rect.x += scroll

        if self.rect.left <= -self.rect.width:
            self.kill()

        pygame.draw.rect(screen, (255, 255, 255), self.rect)


class MovingPlatform(Platform):

    def __init__(self, x1, y1, x2, y2, width, height):
        Platform.__init__(self, x1, y1, width, height)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        # Checking whether to move right or left
        if self.x2 - self.x1 > 0:
            self.movingRight = True
        else:
            self.movingRight = False

    def update(self, screen, scroll):
        self.x1 += scroll
        self.x2 += scroll
        self.movebetween()

        if self.x2 < 0:
            self.kill()

        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    # this function moves the platform between the 2 pos
    def movebetween(self):

        if self.movingRight:
            self.rect.x += 8
            if self.rect.x >= self.x2:
                self.movingRight = False
        else:
            self.rect.x -= 8
            if self.rect.x <= self.x1:
                self.movingRight = True


class Lava(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, screen, scroll, player, gameoverfunc):
        self.rect.x += scroll

        if self.rect.left <= -self.rect.width:
            self.kill()

        if self.rect.colliderect(player.rect):
            gameoverfunc()

        pygame.draw.rect(screen, (255, 0, 0), self.rect)
