import pygame


# klasa NPCta
class Npc(pygame.sprite.Sprite):
    def __init__(self, image_right, image_left, image_talk_right, image_talk_left, platform=None, movement_x=0,
                 movement_y=0):
        super().__init__()
        self.image = image_right
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.platform = platform
        self.image_right = image_right
        self.image_left = image_left
        self.image_talk_right = image_talk_right
        self.image_talk_left = image_talk_left
        self.player = None
        self.level = None
        self.name = ""
        self.talking = False
        self.count = 0
        self.already_talked = False
        self.dialog = "Szeregowy!! Porwano twoją siostrę. URATUJ JĄ!!"

    def update(self):
        # zachowanie w zależności czy gadamy z postacią czy nie
        if not self.talking:
            if self.rect.left > self.player.rect.right:
                self.image = self.image_left
            if self.player.rect.left > self.rect.right:
                self.image = self.image_right
        else:
            if self.rect.left > self.player.rect.right:
                self.image = self.image_talk_left
            if self.player.rect.left > self.rect.right:
                self.image = self.image_talk_right
            self.count += 1

        if self.count > 100:
            self.talking = False
            self.count = 0
