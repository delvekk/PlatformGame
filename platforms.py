import pygame, os


# klasa platformy
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.image_list = None

    def draw(self, surface):
        if self.image_list != None:
            if self.width == 70:
                surface.blit(self.image_list[0], self.rect)
            else:
                surface.blit(self.image_list[1], self.rect)
                for i in range(70, self.width - 70, 70):
                    surface.blit(self.image_list[2], [self.rect.x + i, self.rect.y])
                surface.blit(self.image_list[3], [self.rect.x + self.width - 70, self.rect.y])


# platforma która zabija gracza
class CavePlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)

    def draw(self, surface):
        for i in range(0, self.width, 70):
            surface.blit(self.image_list, [self.rect.x + i, self.rect.y])
        surface.blit(self.image_list, [self.rect.x + self.width - 70, self.rect.y])


# platforma kostkowa
class BrickPlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)

    def draw(self, surface):
        for i in range(0, self.width, 56):
            surface.blit(self.image_list, [self.rect.x + i, self.rect.y])
        surface.blit(self.image_list, [self.rect.x + self.width - 56, self.rect.y])


# platforma trawiasta
class GrassPlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)

    def draw(self, surface):
        for i in range(0, self.width, 280):
            surface.blit(self.image_list, [self.rect.x + i, self.rect.y])
        surface.blit(self.image_list, [self.rect.x + self.width - 280, self.rect.y])


# platforma z kamienia
class StonePlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)

    def draw(self, surface):
        for i in range(0, self.width, 70):
            surface.blit(self.image_list, [self.rect.x + i, self.rect.y])
        surface.blit(self.image_list, [self.rect.x + self.width - 70, self.rect.y])


# ruchoma platforma
class MovingPlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)
        self.movement_x = 0
        self.movement_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.player = None
        self.level = None

    def update(self):
        # ruch prawo/lewo
        self.rect.x += self.movement_x
        # sprawdzamy kontakt z graczem
        if pygame.sprite.collide_rect(self, self.player):
            if self.movement_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        # ruch góra/dół
        self.rect.y += self.movement_y
        # sprawdzamy kontakt z graczem
        if pygame.sprite.collide_rect(self, self.player):
            if self.movement_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # sprawdzamy granice i decydujemy o zmianie kierunku
        if self.rect.bottom > self.boundary_bottom \
                or self.rect.top < self.boundary_top:
            self.movement_y *= -1

        position = self.rect.x - self.level.world_shift
        if position < self.boundary_left or position > self.boundary_right:
            self.movement_x *= -1


# platforma połączona z przekładnią
class MovingLeverPlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)
        self.movement_x = 0
        self.movement_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.player = None
        self.level = None
        self.lever = None

    def update(self):
        # zmiana położenia platformy
        if self.lever.status == 'mid':
            if self.rect.bottom < self.boundary_bottom:
                self.movement_y = 4
            else:
                self.movement_y = 0
        elif self.lever.status == 'left':
            if self.rect.top > self.boundary_top:
                self.movement_y = -4
            else:
                self.movement_y = 0

        # ruch góra/dół
        self.rect.y += self.movement_y

    def draw(self, surface):
        for i in range(0, self.width, 56):
            surface.blit(self.image_list, [self.rect.x + i, self.rect.y])
        surface.blit(self.image_list, [self.rect.x + self.width - 56, self.rect.y])


# platforma reagująca na obecność gracza
class MovingStandPlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)
        self.movement_x = 0
        self.movement_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.player = None
        self.level = None
        self.one_el = False

    def update(self):
        # sprawdzamy kolizje z graczem
        self.rect.y -= 1
        colliding_player = pygame.sprite.collide_rect(self, self.player)
        self.rect.y += 1
        # jeśli jest kolizja zmień położenie
        if colliding_player:
            if self.rect.bottom < self.boundary_bottom:
                self.movement_y = 7
            else:
                self.movement_y = 0
        else:
            if self.rect.top > self.boundary_top:
                self.movement_y = -2
            else:
                self.movement_y = 0

        # ruch góra/dół
        self.rect.y += self.movement_y

    def draw(self, surface):
        if not self.one_el:
            for i in range(0, self.width, 56):
                surface.blit(self.image_list, [self.rect.x + i, self.rect.y])
            surface.blit(self.image_list, [self.rect.x + self.width - 56, self.rect.y])
        else:
            surface.blit(self.image_list, [self.rect.x, self.rect.y])


# platforma reagującac na status pochodnii
class MovingTorchPlatform(Platform):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)
        self.movement_x = 0
        self.movement_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.player = None
        self.level = None
        self.torches = []
        self.status = False

    def update(self):
        # jeżeli wszystkie pochodnie są zapalone zmień status
        for torch in self.torches:
            if torch.status == 'on':
                self.status = True
            else:
                self.status = False
                break

        if self.status:
            if self.rect.bottom < self.boundary_bottom:
                self.movement_y = 4
            else:
                self.movement_y = 0
        else:
            if self.rect.top > self.boundary_top:
                self.movement_y = -4
            else:
                self.movement_y = 0

        # ruch góra/dół
        self.rect.y += self.movement_y

    def draw(self, surface):
        for row in range(0, self.height, 56):
            surface.blit(self.image_list, [self.rect.x, self.rect.y + row])

        for i in range(0, self.width, 56):
            surface.blit(self.image_list, [self.rect.x + i, self.rect.y])
        surface.blit(self.image_list, [self.rect.x + self.width - 56, self.rect.y])


# ściana
class Wall(Platform):
    def draw(self, surface, image_list_wall, image_list_wall_corner):
        for row in range(0, self.height, 70):
            if row == 0:
                surface.blit(image_list_wall_corner[0], self.rect)
                for column in range(70, self.width - 70, 70):
                    surface.blit(
                        image_list_wall[2], [self.rect.x + column, self.rect.y])
                surface.blit(image_list_wall_corner[1],
                             [self.rect.x + self.width - 70, self.rect.y])

            elif row == self.height - 70:
                surface.blit(image_list_wall_corner[3],
                             [self.rect.x, self.rect.y + row])
                for column in range(70, self.width - 70, 70):
                    surface.blit(
                        image_list_wall[4],
                        [self.rect.x + column, self.rect.y + row])
                surface.blit(image_list_wall_corner[2],
                             [self.rect.x + self.width - 70, self.rect.y + row])

            else:
                surface.blit(image_list_wall[1],
                             [self.rect.x, self.rect.y + row])
                for column in range(70, self.width - 70, 70):
                    surface.blit(
                        image_list_wall[0],
                        [self.rect.x + column, self.rect.y + row])
                surface.blit(image_list_wall[3],
                             [self.rect.x + self.width - 70, self.rect.y + row])
