# Importing dependancies
import pygame
from objects import RigidBody


class Player(pygame.sprite.Sprite, RigidBody):

    def __init__(self, x, y, gravity):
        pygame.sprite.Sprite.__init__(self, self.containers)
        RigidBody.__init__(self)

        # Assigning all the player variable and initial setup
        self.width = 50
        self.height = 50
        self.vel_x = 15
        self.vel_y = 0
        self.gravity = gravity
        self.grounded = False

        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update(self, screen, platformsGroup, scroll, gameOverfunc):
        # This function is called once a frame
        self.rect.y, self.vel_y = self.apply_gravity(self.gravity, self.grounded, self.vel_y, self.rect.y)

        # Checking if the player is outside the screen or dies
        if self.rect.top > screen.get_height() + 100 or self.rect.left < 0:
            gameOverfunc()

        # temp variable to see if grounded
        ground_check = None
        moved_hitbox = self.rect
        moved_hitbox.y = moved_hitbox.y + 2

        for platform in platformsGroup:
            if moved_hitbox.colliderect(platform.rect):
                ground_check = True
                self.rect.bottom = platform.rect.top
                break
            else:
                ground_check = False

        self.grounded = ground_check

        # Drawing the player
        self.rect.x += scroll
        pygame.draw.rect(screen, (100, 100, 223), self.rect)

    def move(self, horizontal_move):
        self.rect.x += self.vel_x * horizontal_move

    def jump(self, initial_vel):
        # Jump function
        self.vel_y = -initial_vel
        self.grounded = False
