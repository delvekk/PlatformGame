import pygame, constants, levels


# klasa przedmiotu
class Item(pygame.sprite.Sprite):
    def __init__(self, image, name):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name

# skała, reagująca na pozycje gracza
class Spike(Item):
    def __init__(self, image, name):
        super().__init__(image, name)
        self.player = None
        self.level = None
        self.movement_y = 0

    def update(self):
        colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        if colliding_platforms:
            self.kill()

        colliding_enemies = pygame.sprite.spritecollide(self, self.level.set_of_enemies, False)
        for enemy in colliding_enemies:
            enemy.kill()

        diff = self.rect.x - self.player.rect.x
        if diff < 200:
            self.movement_y = 15

        self.rect.y += self.movement_y

# drzewo
class Tree(Item):
    def __init__(self, image, name):
        super().__init__(image, name)


# klasa pocisku
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, direction):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.direction_of_movement = direction
        self.power = 1

    def update(self):
        if self.direction_of_movement == 'right':
            self.rect.x += 15
        else:
            self.rect.x -= 15

# pocisk przeciwnika
class EnemyBullet(Bullet):
    def __init__(self, image, direction):
        super().__init__(image, direction)

# pudło/skrzynia
class Box(Item):
    def __init__(self, image, name):
        super().__init__(image, name)
        self.lifes = 2
        self.level = None
        self.count = 0

    def update(self):
        if self.lifes <= 0:
            self.kill()

# przekładnia
class Lever(Item):
    def __init__(self, image, lever_mid, name):
        super().__init__(image, name)
        self.lever_left = image
        self.lever_mid = lever_mid
        self.status = 'left'

    def update(self):
        if self.status == 'left':
            self.image = self.lever_left
        if self.status == 'mid':
            self.image = self.lever_mid

# sprężyna
class Spring(Item):
    def __init__(self, image, spring_in, spring_out, name, height):
        super().__init__(image, name)
        self.spring = image
        self.spring_in = spring_in
        self.spring_out = spring_out
        self.status = 'normal'
        self.rect_normal = height
        self.rect_out = height - 30
        self.player = None

    def update(self):
        if self.status == 'in':
            self.rect.bottom = self.rect_normal
            self.image = self.spring_in
        if self.status == 'out':
            self.image = self.spring_out
            self.rect.bottom = self.rect_out

# pochodnia
class Torch(Item):
    def __init__(self, torch_off_image, torch_on_image, name):
        super().__init__(torch_off_image, name)
        self.torch_off_image = torch_off_image
        self.torch_on_image = torch_on_image
        self.status = 'off'

    def update(self):
        if self.status == 'off':
            self.image = self.torch_off_image
        if self.status == 'on':
            self.image = self.torch_on_image

# drabina
class Ladder(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, [self.rect.x, self.rect.y])
