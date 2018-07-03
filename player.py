import pygame, items, os, platforms, constants, levels, enemies, random
from random import randint

# -----------------------------PLAYER GRAFIKA -------------------
STAND_R = pygame.image.load(os.path.join('png', 'player_standR.png'))
WALK_R1 = pygame.image.load(os.path.join('png', 'player_walkR1.png'))
WALK_R2 = pygame.image.load(os.path.join('png', 'player_walkR2.png'))
STAND_L = pygame.image.load(os.path.join('png', 'player_standL.png'))
WALK_L1 = pygame.image.load(os.path.join('png', 'player_walkL1.png'))
WALK_L2 = pygame.image.load(os.path.join('png', 'player_walkL2.png'))
FALL_L = pygame.image.load(os.path.join('png', 'player_fallL.png'))
FALL_R = pygame.image.load(os.path.join('png', 'player_fallR.png'))
JUMP_L = pygame.image.load(os.path.join('png', 'player_jumpL.png'))
JUMP_R = pygame.image.load(os.path.join('png', 'player_jumpR.png'))
CLIMB_1 = pygame.image.load(os.path.join('png', 'player_climb1.png'))
CLIMB_2 = pygame.image.load(os.path.join('png', 'player_climb2.png'))
SLIDE_L = pygame.image.load(os.path.join('png', 'player_slide_L.png'))
SLIDE_R = pygame.image.load(os.path.join('png', 'player_slide_R.png'))
TALK_R = pygame.image.load(os.path.join('png', 'player_talk_R.png'))
TALK_L = pygame.image.load(os.path.join('png', 'player_talk_L.png'))
CHEER_R1 = pygame.image.load(os.path.join('png', 'player_cheerR1.png'))
CHEER_R2 = pygame.image.load(os.path.join('png', 'player_cheerR2.png'))
CHEER_L1 = pygame.image.load(os.path.join('png', 'player_cheerL2.png'))
CHEER_L2 = pygame.image.load(os.path.join('png', 'player_cheerL1.png'))
image_right = [WALK_R1, WALK_R2]
image_left = [WALK_L1, WALK_L2]
climb_list = [CLIMB_1, CLIMB_2]
cheer_right = [CHEER_R1, CHEER_R2]
cheer_left = [CHEER_L1, CHEER_L2]

# ----------------------- DŹWIĘK PLAYER -----------------

# -------------------------------- ITEMKI GRAFIKA -----------------------
BULLET_R = pygame.image.load(os.path.join('png', 'bullet_R.png'))
BULLET_L = pygame.image.load(os.path.join('png', 'bullet_L.png'))
LASER_BULLET = pygame.image.load(os.path.join('png', 'laserPurple.png'))
SPECIAL_BULLET = pygame.image.load(os.path.join('png', 'swirl_blue.png'))
HEART = pygame.image.load(os.path.join('png', 'heart.png'))


## klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image, sound_list):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = set()
        self.items_count = 0
        self.ammo = 0
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.power = 0
        self.lifes = 2
        self.level = None
        self.direction_of_movement = 'right'
        self.actual_weapon = None
        self.climbing = False
        self.slide = False
        self.crouch = False
        self.cheering = False
        self.sounds = sound_list

        special_attack = items.Item(SPECIAL_BULLET, 'special attack')
        self.items.add(special_attack)

    # idź w prawo
    def turn_right(self):
        self.slide = False
        if self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'
        self.movement_x = 6

    # idź w lewo
    def turn_left(self):
        self.slide = False
        if self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'
        self.movement_x = -6

    # ślizgaj sie w prawo
    def slide_right(self):
        self.movement_x = 4
        self.image = STAND_R

    # ślizgaj sie w lewo
    def slide_left(self):
        self.movement_x = -4
        self.image = STAND_L

    # metoda odpowiadając za skok
    # jeśli sie wspina inna prędkość ruchu
    # jeśli znajduje sie na sprężynie inna prędkość ruchu
    def jump(self):
        if self.climbing:
            self.movement_y = -5
        else:
            self.rect.y += 8
            colliding_platforms = pygame.sprite.spritecollide(
                self, self.level.set_of_platforms, False)
            self.rect.y -= 8

            if colliding_platforms:
                self.movement_y = -11

            self.rect.y += 8
            colliding_items = pygame.sprite.spritecollide(
                self, self.level.set_of_items, False)
            self.rect.y -= 8

            for item in colliding_items:
                if item.name == 'spring':
                    self.movement_y = -20
                    item.status = 'out'
                else:
                    self.movement_y = -11

    # gdy schodzi z drabiny
    def go_down(self):
        if self.climbing:
            self.movement_y = 5

    # strzelanie
    def shoot(self):
        # jeśli aktualna broń to strzelba
        if self.actual_weapon == 'gun' and len(self.level.set_of_bullets) < 2:
            self.sounds[3].play()
            bullet = items.Bullet(BULLET_R, self.direction_of_movement)
            bullet.power = 1
            if self.direction_of_movement == 'left':
                bullet.image = BULLET_L
            if self.crouch:
                bullet.rect.centery = self.rect.centery + 30
            else:
                bullet.rect.centery = self.rect.centery + 15
            bullet.rect.centerx = self.rect.centerx
            if pygame.sprite.spritecollide(bullet, self.level.set_of_bullets, False):
                bullet.kill()
            else:
                self.level.set_of_bullets.add(bullet)
        # jeśli aktualna broń to karabin laserowy i ma amunicje!
        elif self.actual_weapon == 'laser gun' and len(self.level.set_of_bullets) < 4 and self.ammo > 0:
            self.sounds[4].play()
            bullet = items.Bullet(LASER_BULLET, self.direction_of_movement)
            bullet.power = 3
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.centery = self.rect.centery + 15
            if pygame.sprite.spritecollide(bullet, self.level.set_of_bullets, False):
                bullet.kill()
            else:
                self.level.set_of_bullets.add(bullet)
            self.ammo -= 1
        # atak specjalny
        elif self.actual_weapon == 'special attack' and len(self.level.set_of_bullets) < 4:
            self.sounds[6].play()
            bullet = items.Bullet(SPECIAL_BULLET, self.direction_of_movement)
            power = 5 * self.power
            bullet.power = power
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.centery = self.rect.centery + 15
            self.level.set_of_bullets.add(bullet)
            self.power = 0
            self.actual_weapon = None

    # metoda prywatna - grawitacja
    # grawitacja nie działa jeśli postać jest na drabinie
    def _gravitation(self):
        if self.climbing:
            pass
        else:
            if self.movement_y == 0:
                self.movement_y = 7
            else:
                self.movement_y += 0.37

    def stop_x(self):
        self.movement_x = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    # funkcja odpowiadająca za interakcje z postaciami oraz przedmiotami
    def talk(self):
        colliding_npcs = pygame.sprite.spritecollide(self, self.level.set_of_npcs, False)
        colliding_items = pygame.sprite.spritecollide(self, self.level.set_of_items, False)
        # jeśli npc nazywa się Solider, to gadaj z nim
        # Solider rzuca broń, chyba że juz z nim gadaliśmy wcześniej
        for npc in colliding_npcs:
            if self.direction_of_movement == 'left':
                self.image = TALK_L
            elif self.direction_of_movement == 'right':
                self.image = TALK_R
            if npc.name == "Soldier":
                self.sounds[5].play()
                npc.talking = True
                self.level.objective = "Weź broń i oczyść miasto z potworów"
                if not npc.already_talked:
                    gun = items.Item(levels.SHOTGUN, 'gun')
                    gun.rect.x = 800
                    gun.rect.bottom = constants.HEIGHT - 100
                    self.level.set_of_items.add(gun)
                npc.already_talked = True
            if npc.name == "Sister":
                self.sounds[5].play()
                npc.talking = True
                self.cheering = True
                self.level.objective = "GRATULACJE, UKOŃCZYŁEŚ GRĘ"
                if not npc.already_talked:
                    pass
                npc.already_talked = True
        # itemki
        for item in colliding_items:
            # jeżeli item to skrzynia, i masz klucz do tej skrzyni
            # to otwórz skrzynie i dropnij itemka
            if item.name == "lock box1":
                for check_item in self.items:
                    if check_item.name == 'yellow key':
                        item.kill()
                        self.items.remove(check_item)
                        self.cheering = True
                        gun = items.Item(levels.LASER_GUN, 'laser gun')
                        gun.rect.x = 85
                        gun.rect.bottom = constants.HEIGHT - 500
                        self.level.set_of_items.add(gun)
                        break

            # podobnie jak wyżej
            if item.name == "lock box2":
                for check_item in self.items:
                    if check_item.name == 'blue key':
                        item.kill()
                        self.items.remove(check_item)
                        self.cheering = True
                        ammo = items.Item(LASER_BULLET, 'laser ammo')
                        ammo.rect.x = 120
                        ammo.rect.bottom = 200
                        self.level.set_of_items.add(ammo)
                        power_up = items.Item(levels.POWER_UP, 'power up')
                        power_up.rect.x = 120
                        power_up.rect.bottom = 200
                        self.level.set_of_items.add(power_up)
                        break

            # obsługa przekładni
            if item.name == 'lever':
                if item.status == 'left':
                    item.status = 'mid'
                elif item.status == 'mid':
                    item.status = 'left'
                break
            # obsługa pochodnii
            if item.name == 'torch':
                if item.status == 'off':
                    item.status = 'on'
                elif item.status == 'on':
                    item.status = 'off'

    # funkcja prywatna odpowiada za ruch(animacje)
    def _move(self, image_list):
        if not self.slide:
            if self._count < 4:
                self.image = image_list[0]
            elif self._count < 8:
                self.image = image_list[1]
            if self._count >= 8:
                self._count = 0
            else:
                self._count += 1

    def update(self):
        self._gravitation()
        # --------------ruch w poziomie---------------
        self.rect.x += self.movement_x
        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)
        colliding_items = pygame.sprite.spritecollide(self, self.level.set_of_items, False)

        # sprawdzamy kolizje z platformami
        for p in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right

        # sprawdzamy kolizje z przedmiotami
        for item in colliding_items:
            if item.name == 'box' and not self.slide:
                if self.movement_x > 0:
                    self.rect.right = item.rect.left
                if self.movement_x < 0:
                    self.rect.left = item.rect.right

            if item.name == 'spring':
                if self.movement_x > 0:
                    self.rect.right = item.rect.left
                if self.movement_x < 0:
                    self.rect.left = item.rect.right

        # animacje
        if self.movement_x > 0:
            self.cheering = False
            if self.slide:
                self.image = SLIDE_R
            else:
                self._move(image_right)
        if self.movement_x < 0:
            self.cheering = False
            if self.slide:
                self.image = SLIDE_L
            else:
                self._move(image_left)

        # --------------ruch w pionie---------------
        self.rect.y += self.movement_y
        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)
        colliding_npcs = pygame.sprite.spritecollide(self, self.level.set_of_npcs, False)
        colliding_items = pygame.sprite.spritecollide(self, self.level.set_of_items, False)

        self.interact_with = False
        # interakcja z przedmiotami
        for item in colliding_items:
            if item.name == 'box' and not self.slide or item.name == 'spring':
                if self.movement_y > 0:
                    self.rect.bottom = item.rect.top
                    if self.direction_of_movement == 'left' and self.movement_x == 0:
                        self.image = STAND_L
                    if self.direction_of_movement == 'right' and self.movement_x == 0:
                        self.image = STAND_R
                if self.movement_y < 0:
                    self.rect.top = item.rect.bottom
                self.movement_y = 0

            if item.name == 'lock box1' or item.name == 'lever' or item.name == 'torch' or item.name == 'lock box2':
                self.interact_with = True

            if item.name == 'spring':
                item.status = 'in'

        # kolizje z platformami
        for p in colliding_platforms:
            # kolizja z CavePlatform powoduje utratę życia
            if isinstance(p, platforms.CavePlatform):
                self.lifes -= 1
                pygame.time.delay(500)
                self.rect.left = 100 + self.level.world_shift
                self.rect.bottom = constants.HEIGHT - 200
                break
            self.climbing = False
            # jeśli poruszamy się w dół
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.direction_of_movement == 'left' and self.movement_x == 0:
                    if colliding_npcs or self.interact_with:
                        self.image = TALK_L
                    elif self.cheering:
                        self._move(cheer_right)
                    else:
                        self.image = STAND_L
                if self.direction_of_movement == 'right' and self.movement_x == 0:
                    if colliding_npcs or self.interact_with:
                        self.image = TALK_R
                    elif self.cheering:
                        self._move(cheer_left)
                    else:
                        self.image = STAND_R
            # jeśli poruszamy się w górę
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0

            # gracz jedzie razem z platformą
            if isinstance(p, platforms.MovingPlatform) and self.movement_x == 0:
                self.rect.x += p.movement_x
        # kolizje z drabinami
        colliding_ladders = pygame.sprite.spritecollide(self, self.level.set_of_ladders, False)
        if colliding_ladders:
            if self.movement_y != 0:
                self._move(climb_list)
            self.climbing = True
        else:
            self.climbing = False

        # zmiana grafiki gdy nie jedzie razem z platformą w dół
        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        self.rect.y -= 2
        # gdy brak kolizji animacja spadania
        if not colliding_platforms and not self.climbing and not colliding_items:
            if self.movement_y > 0:
                if self.direction_of_movement == 'left':
                    self.image = FALL_L
                else:
                    self.image = FALL_R
            if self.movement_y < 0:
                if self.direction_of_movement == 'left':
                    self.image = JUMP_L
                else:
                    self.image = JUMP_R

        # sprawdzamy kolizję z wrogami lub spadek w przepaść
        enemies_bullets = set(self.level.set_of_enemy_bullets) | set(self.level.set_of_enemies) | set(
            self.level.set_of_undead_enemies)
        colliding_enmies_bullets = pygame.sprite.spritecollide(
            self, enemies_bullets, False)
        # kolizje z pociskami przeciwnika
        for eb in colliding_enmies_bullets:
            if isinstance(eb, enemies.Enemy):
                if eb.lifes:
                    self.lifes -= 1
                    pygame.time.delay(500)
                    self.rect.left = 150 + self.level.world_shift
                    self.rect.bottom = constants.HEIGHT - 200
            else:
                eb.kill()
                self.lifes -= 1
                pygame.time.delay(500)
                self.rect.left = 150 + self.level.world_shift
                self.rect.bottom = constants.HEIGHT - 200
        # gdy postać spadnie w przepaść
        if self.rect.top > constants.HEIGHT:
            self.lifes -= 1
            pygame.time.delay(500)
            self.rect.left = 100 + self.level.world_shift
            self.rect.bottom = constants.HEIGHT - 200

        # sprawdzenie kolizji z przedmiotami
        colliding_items = pygame.sprite.spritecollide(
            self, self.level.set_of_items, False)
        for item in colliding_items:
            if item.name == 'gun':
                self.items.add(item)
                item.kill()
                self.actual_weapon = 'gun'
                self.sounds[2].play()

            if item.name == 'laser gun':
                self.items.add(item)
                self.ammo += randint(0, 3)
                item.kill()
                self.actual_weapon = 'laser gun'
                self.sounds[2].play()

            if item.name == 'laser ammo':
                self.ammo += randint(5, 15)
                item.kill()
                self.sounds[2].play()

            if item.name == 'box':
                if self.slide:
                    item.lifes -= 2

            if item.name == 'power up':
                self.cheering = True
                self.power += 1
                item.kill()
                self.sounds[2].play()

            if item.name == 'heart':
                self.lifes += 1
                item.kill()
                self.sounds[2].play()

            if item.name == 'yellow key' or item.name == 'blue key':
                self.items.add(item)
                item.kill()
                self.sounds[2].play()

            if item.name == 'spike':
                self.lifes -= 1
                item.kill()
                pygame.time.delay(500)
                self.rect.left = 150 + self.level.world_shift
                self.rect.bottom = constants.HEIGHT - 200

        if self.direction_of_movement == 'right' and self.movement_y == 0 and self.movement_x > 0:
            if self._count == 0:
                    self.sounds[1].play()
        if self.direction_of_movement == 'left' and self.movement_y == 0 and self.movement_x < 0:
            if self._count == 0:
                self.sounds[1].play()

    # funkcja odpowiadająća za eventy - użycie przycisków na klawiaturze
    def get_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if keys[pygame.K_s]:
                self.slide = True
                self.slide_right()
        if keys[pygame.K_a]:
            if keys[pygame.K_s]:
                self.slide = True
                self.slide_left()
        if keys[pygame.K_s]:
            if keys[pygame.K_SPACE]:
                self.crouch = True
                self.shoot()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.talk()
            if event.key == pygame.K_d:
                self.slide = False
                self.turn_right()
            if event.key == pygame.K_a:
                self.slide = False
                self.turn_left()
            if event.key == pygame.K_s:
                self.go_down()
            if event.key == pygame.K_w:
                self.up_down = "up"
                self.jump()
            if event.key == pygame.K_SPACE:
                if not self.crouch:
                    self.shoot()
                self.crouch = False
            if event.key == pygame.K_1:
                for item in self.items:
                    if item.name == 'gun':
                        self.actual_weapon = item.name
                        break
            if event.key == pygame.K_2:
                for item in self.items:
                    if item.name == 'laser gun':
                        self.actual_weapon = item.name
                        break
            if event.key == pygame.K_3:
                if self.power > 0:
                    self.actual_weapon = 'special attack'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s and self.slide:
                self.slide = False
            if event.key == pygame.K_a and self.slide:
                self.slide = False
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop_x()
                self.image = STAND_R
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop_x()
                self.image = STAND_L
