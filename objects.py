# Importing dependacies
import pygame


class RigidBody:

    def __init__(self , affected_by_gravity=True):
        self.affected_by_gravity = affected_by_gravity

    def apply_gravity(self, gravitational_acc, isGrounded, current_vel ,y):
        # Apply gravity to the body
        time = 2
        if self.affected_by_gravity:
            if not isGrounded:
                final_vel = current_vel + gravitational_acc * time
                disp = ( current_vel*time + 0.5 * gravitational_acc * (time**2) ) * (1 / 1 + pygame.time.Clock().get_time())
                new_y = y + disp
                return new_y, final_vel
        
        new_y = y
        final_vel = current_vel
        return new_y, final_vel

# Making marker class


class Marker:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
    
    def update(self, screen, scroll):
        self.rect.x += scroll
