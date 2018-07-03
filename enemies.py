import pygame,  random, items, levels, constants, platforms, player


# ogólna klasa wroga
class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0):
        super().__init__()
        self.image = start_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.direction_of_movement = 'left'
        self.platform = platform
        self.image_right = image_right
        self.image_left = image_left
        self.image_dead_right = image_dead_right
        self.image_dead_left = image_dead_left
        self.lifes = 2
        self.count = 0
        self.player = None
        self.level = None

        if self.platform:
            self.rect.bottom = self.platform.rect.top
            self.rect.centerx = random.randint(
                self.platform.rect.left + self.rect.width,
                self.platform.rect.right - self.rect.width)

    def update(self):
        if self.lifes <= 0 and self.count > 7:
            self.kill()

        if self.level != None:
            colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
            for platform in colliding_platforms:
                if isinstance(platform, platforms.CavePlatform):
                    self.kill()

        self.rect.x += self.movement_x
        self.rect.y += self.movement_y

        # animacje
        if self.lifes:
            if self.movement_x > 0:
                self._move(self.image_right)
            if self.movement_x < 0:
                self._move(self.image_left)
        else:
            if self.direction_of_movement == 'right':
                self._move(self.image_dead_right)
            else:
                self._move(self.image_dead_left)

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count = 0
        else:
            self.count += 1


class Cloud_Enemy(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left,boundary_left, boundary_right, platform=None, movement_x=0, movement_y=0):
        super().__init__(start_image, image_right, image_left, image_dead_right,
                         image_dead_left, platform, movement_x, movement_y)
        self.boundary_left = boundary_left
        self.boundary_right = boundary_right


    def update(self):
        position = self.rect.x - self.level.world_shift
        if position < self.boundary_left or position > self.boundary_right:
            self.movement_x *= -1

        self.rect.x += self.movement_x


class Platform_Enemy(Enemy):
    def update(self):
        super().update()
        if self.rect.left < self.platform.rect.left or \
                        self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0 and self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'

        if self.movement_x < 0 and self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'

class Spinner_Enemy(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0, start_x = None, start_y=None):
        super().__init__(start_image,image_right, image_left, image_dead_right,
                 image_dead_left, platform, movement_x, movement_y)
        self.rect.x = start_x
        self.rect.y = start_y

    def _gravitation(self):
            if self.movement_y == 0:
                self.movement_y = 4
            else:
                self.movement_y += 0.35

    def update(self):
        super().update()
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)

        colliding_items = pygame.sprite.spritecollide(
            self, self.level.set_of_items, False)

        if self.rect.top > constants.HEIGHT:
            self.kill()

        for element in colliding_items:
            if element.name == 'box':
                element.kill()

        for element in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = element.rect.left
            if self.movement_x < 0:
                self.rect.left = element.rect.right

        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)
        self.rect.y += -2

        if not colliding_platforms:
            self._gravitation()


        diff = self.rect.left - self.player.rect.right
        if diff < 400:
            if self.rect.x <= self.player.rect.x and diff < -200:
                self.movement_x = 6
            elif self.rect.x > self.player.rect.x and diff > 200:
                self.movement_x = -6
        else:
            self.movement_x = 0





class Zombie_Enemy(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0, start_x = None, start_y=None):
        super().__init__(start_image,image_right, image_left, image_dead_right,
                 image_dead_left, platform, movement_x, movement_y)
        self.rect.x = start_x
        self.rect.y = start_y



    def update(self):
        super().update()
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)

        colliding_items = pygame.sprite.spritecollide(
            self, self.level.set_of_items, False)

        for element in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = element.rect.left
            if self.movement_x < 0:
                self.rect.left = element.rect.right

        for element in colliding_items:
            if element.name == 'box':
                if self.movement_x > 0:
                    self.rect.right = element.rect.left
                if self.movement_x < 0:
                    self.rect.left = element.rect.right

        if self.rect.x < self.player.rect.x:
            self.movement_x = random.choice([1,2,3])
        elif self.rect.x > self.player.rect.x:
            self.movement_x = random.choice([-1,-2,-3])
        else:
            self.movement_x = 0


class Ghost_Boss(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0, start_x = None, start_y=None):
        super().__init__(start_image,image_right, image_left, image_dead_right,
                 image_dead_left, platform, movement_x, movement_y)
        self.lifes = 60
        self.rect.x = start_x
        self.rect.y = start_y


    def update(self):
        super().update()
        if self.lifes <= 0 and self.count > 7:
            heart = items.Item(levels.HEART, 'heart')
            heart.rect.x = self.rect.x
            heart.rect.bottom = self.rect.y
            self.level.set_of_items.add(heart)
        diff = self.rect.left - self.player.rect.right
        diff2 = self.rect.centery - self.player.rect.centery
        if diff < 500:
            if diff2 > 0:
                self.movement_y = -1
            elif diff2 < 0:
                self.movement_y = 1
            else:
                self.movement_y = 0
            if self.rect.x <= self.player.rect.x:
                self.movement_x = 3
            elif self.rect.x > self.player.rect.x:
                self.movement_x = -3
        else:
            self.movement_x = 0
            self.movement_y = 0


class Mouse_Enemy(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0, start_x = None, start_y=None):
        super().__init__(start_image,image_right, image_left, image_dead_right,
                 image_dead_left, platform, movement_x, movement_y)
        self.lifes = 2
        self.rect.x = start_x
        self.rect.y = start_y



    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 4
        else:
            self.movement_y += 0.35

    def jump(self):
        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        self.rect.y -= 2

        if colliding_platforms:
            self.movement_y = -7

        self.rect.y += 2
        colliding_items = pygame.sprite.spritecollide(
            self, self.level.set_of_items, False)
        self.rect.y -= 2

        if colliding_items:
            self.movement_y = -7

    def update(self):
        super().update()
        self._gravitation()
        diff = self.rect.left - self.player.rect.right
        if diff < 300:
            if self.rect.x <= self.player.rect.x:
                self.movement_x = 3
            elif self.rect.x > self.player.rect.x:
                self.movement_x = -3
        else:
            self.movement_x = 0

        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)
        for p in colliding_platforms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top

            self.movement_y = 0

        if self.player.rect.bottom < self.rect.top:
            self.jump()


class Bat_Enemy(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0):
        super().__init__(start_image, image_right, image_left, image_dead_right,
                         image_dead_left, platform, movement_x, movement_y)

        self.boundary_right = 0
        self.boundary_left = 0
        self.boundary_bottom = 0
        self.boundary_top = 0
        self.level = None
        self.sleep = True

    def update(self):
        if self.sleep:
            if self.rect.left - self.level.player.rect.right < 400:
                self.sleep = False
        else:
            super().update()
            self.rect.x += self.movement_x
            self.rect.y += self.movement_y
            position = self.rect.x - self.level.world_shift
            if position < self.boundary_left or \
                                    position + self.rect.width > self.boundary_right:
                self.movement_x *= -1
            if self.rect.top < self.boundary_top or \
                            self.rect.bottom > self.boundary_bottom:
                self.movement_y *= -1

            if self.movement_x > 0 and self.direction_of_movement == 'left':
                self.direction_of_movement = 'right'

            if self.movement_x < 0 and self.direction_of_movement == 'right':
                self.direction_of_movement = 'left'

class Spider_Enemy(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0, start_x = None, start_y=None):
        super().__init__(start_image,image_right, image_left, image_dead_right,
                 image_dead_left, platform, movement_x, movement_y)
        self.rect.x = start_x
        self.rect.y = start_y
        self.lifes = 5

    def shoot(self):
        bullet = items.EnemyBullet(levels.SPIDERWEB_R, self.direction_of_movement)
        if self.direction_of_movement == 'left':
            bullet.image = levels.SPIDERWEB_L
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.centery = self.rect.centery - 10
        if pygame.sprite.spritecollide(
            bullet, self.level.set_of_enemy_bullets, False):
            bullet.kill()
        else:
            self.level.set_of_enemy_bullets.add(bullet)


    def jump(self):
        if self._on_platform:
            self.movement_y = -5


    def update(self):
        super().update()
        if self.lifes <= 0 and self.count > 7:
            heart = items.Item(levels.HEART, 'heart')
            heart.rect.x = self.rect.x
            heart.rect.bottom = self.rect.y
            self.level.set_of_items.add(heart)
        self._gravitation()



        if self.rect.top > constants.HEIGHT:
            self.kill()

        self.rect.x += self.movement_x
        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)

        for p in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
                self.movement_x *= -1
            else:
                self.movement_x *= -1
                self.rect.left = p.rect.right

        if self.movement_x > 0:
            self.direction_of_movement = 'right'

        if self.movement_x < 0:
            self.direction_of_movement = 'left'

        # sprawdzamy czy wróg jest na platformie
        self.rect.y += 4
        if pygame.sprite.spritecollide(
                self, self.level.set_of_platforms, False):
            self._on_platform = True
        else:
            self._on_platform = False
        self.rect.y -= 4

        # zmiana grafiki tylko gdy spada lub skacze
        if not self._on_platform:
            if self.movement_y > 0:
                if self.direction_of_movement == 'left':
                    self.image = levels.SPIDER_STAND_L
                else:
                    self.image = levels.SPIDER_STAND_R
            if self.movement_y < 0:
                if self.direction_of_movement == 'left':
                    self.image = levels.SPIDER_STAND_L
                else:
                    self.image = levels.SPIDER_STAND_R

        if not random.randint(1, 100) % 41:
            self.jump()
        if not random.randint(1, 100) % 33:
            self.shoot()

        self.rect.y += self.movement_y
        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)
        for p in colliding_platforms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0

            # obiekt jedzie razem z platformą
            if isinstance(p, platforms.MovingPlatform) and self.movement_x == 0:
                self.rect.x += p.movement_x

    # metoda prywatna - grawitacja
    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 2
        else:
            self.movement_y += 0.35



class Barnacle_Enemy(Enemy):
    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0):
        super().__init__(start_image,image_right, image_left, image_dead_right,
                 image_dead_left, platform, movement_x, movement_y)
        self.lifes = 30
        self.player = None
        self.shooting = False

    def shoot(self):
        self.shooting = True
        bullet = items.EnemyBullet(levels.FIREBALL_RIGHT, self.direction_of_movement)
        if self.direction_of_movement == 'left':
            bullet.image = levels.FIREBALL_LEFT
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.centery = self.rect.centery - 10
        if pygame.sprite.spritecollide(
            bullet, self.level.set_of_enemy_bullets, False):
            bullet.kill()
        else:
            self.level.set_of_enemy_bullets.add(bullet)

    def update(self):
        super().update()
        if self.lifes <= 0:
            self.kill()
        if self.shooting:
            self.image = levels.BARNACLE_SHOOT
        else:
            self.image = levels.BARNACLE_STAND


        if self.player.rect.x >= self.rect.x:
            self.direction_of_movement = 'right'
        else:
            self.direction_of_movement = 'left'

        if not random.randint(1, 100) % 33:
            if random.randint(1, 100) % 2:
                self.shooting = True
                self.shoot()
        else:
            self.shooting = False


