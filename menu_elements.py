import pygame, constants
class Button:
    def __init__(self, text, width, height, background_colour, text_colour, x, y):
        self.text = text
        self.width = width
        self.height = height
        self.background_colour =  background_colour
        self.text_colour = text_colour
        self.font = pygame.font.SysFont(None, 72)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = [x, y]
        self.set()

    def set(self):
        self.image = self.font.render(
            self.text,1, self.text_colour, self.background_colour)
        self.rect_image = self.image.get_rect()
        self.rect_image.center = self.rect.center

    def draw(self, surface):
        surface.fill(self.background_colour, self.rect)
        surface.blit(self.image, self.rect_image)