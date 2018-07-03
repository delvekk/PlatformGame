import pygame, os, platforms, constants, random, enemies, items, npcs

# -------------tło----------
BACKGROUND = pygame.image.load(os.path.join('png', 'background_01.png'))
BACKGROUND2 = pygame.image.load(os.path.join('png', 'background_02.png'))

# -------------grafika platforms---------------
GRASS_L = pygame.image.load(os.path.join('png', 'grass_L.png'))
GRASS_C = pygame.image.load(os.path.join('png', 'grass_C.png'))
GRASS_R = pygame.image.load(os.path.join('png', 'grass_R.png'))
GRASS_SINGLE = pygame.image.load(os.path.join('png', 'grass_single.png'))
METAL_L = pygame.image.load(os.path.join('png', 'metal_L.png'))
METAL_C = pygame.image.load(os.path.join('png', 'metal_C.png'))
METAL_R = pygame.image.load(os.path.join('png', 'metal_R.png'))
METAL_SINGLE = pygame.image.load(os.path.join('png', 'metal_single.png'))
WALL = pygame.image.load(os.path.join('png', 'wall.png'))
WALL_R = pygame.image.load(os.path.join('png', 'wall_right.png'))
WALL_L = pygame.image.load(os.path.join('png', 'wall_left.png'))
WALL_T = pygame.image.load(os.path.join('png', 'wall_top.png'))
WALL_B = pygame.image.load(os.path.join('png', 'wall_bottom.png'))
WALL_TR = pygame.image.load(os.path.join('png', 'wall_top_R.png'))
WALL_TL = pygame.image.load(os.path.join('png', 'wall_top_L.png'))
WALL_BR = pygame.image.load(os.path.join('png', 'wall_bottom_R.png'))
WALL_BL = pygame.image.load(os.path.join('png', 'wall_bottom_L.png'))
WALL_BRICK = pygame.image.load(os.path.join('png', 'wall_brick.png'))
WALL_INDUSTRIAL = pygame.image.load(os.path.join('png', 'wall_industrial.png'))
STONE = pygame.image.load(os.path.join('png', 'stone.png'))
LADDER = pygame.image.load(os.path.join('png', 'ladder.png'))
STONE_S = pygame.image.load(os.path.join('png', 'stone_single.png'))
STONE_C = pygame.image.load(os.path.join('png', 'stoneMid.png'))
STONE_L = pygame.image.load(os.path.join('png', 'stoneLeft.png'))
STONE_R = pygame.image.load(os.path.join('png', 'stoneRight.png'))
CAVE = pygame.image.load(os.path.join('png', 'stoneCaveSpikeBottom.png'))
BEAM = pygame.image.load(os.path.join('png', 'beam.png'))
GROUND_GRASS = pygame.image.load(os.path.join('png', 'ground_grass.png'))
DIRTY_C = pygame.image.load(os.path.join('png', 'dirtMid.png'))
DIRTY_S = pygame.image.load(os.path.join('png', 'dirt_single.png'))
DIRTY_L = pygame.image.load(os.path.join('png', 'dirtLeft.png'))
DIRTY_R = pygame.image.load(os.path.join('png', 'dirtRight.png'))

GRASS_LIST = [GRASS_SINGLE, GRASS_L, GRASS_C, GRASS_R]
METAL_LIST = [METAL_SINGLE, METAL_L, METAL_C, METAL_R]
WALL_LIST = [WALL, WALL_L, WALL_T, WALL_R, WALL_B]
WALL_CORNER_LIST = [WALL_TL, WALL_TR, WALL_BR, WALL_BL]
BEAM_LIST = [BEAM, BEAM, BEAM, BEAM]
STONE_GROUND_LIST = [STONE_S, STONE_L, STONE_C, STONE_R]
DIRTY_GROUND_LLST = [DIRTY_S, DIRTY_L, DIRTY_C, DIRTY_R]
INDUSTRIAL_LIST = [WALL_INDUSTRIAL, WALL_INDUSTRIAL, WALL_INDUSTRIAL, WALL_INDUSTRIAL, WALL_INDUSTRIAL]
INDUSTRIAL_CORNER_LIST = [WALL_INDUSTRIAL, WALL_INDUSTRIAL, WALL_INDUSTRIAL, WALL_INDUSTRIAL]
BRICK_LIST = [WALL_BRICK, WALL_BRICK, WALL_BRICK, WALL_BRICK]
STONE_LIST = [STONE, STONE, STONE, STONE]


# -----------grafika enemies-----------------
# ---------------ZOMBIE--------------
ZOMBIE_STAND_R = pygame.image.load(os.path.join('png', 'zombie_standR.png'))
ZOMBIE_WALK_R1 = pygame.image.load(os.path.join('png', 'zombie_walkR1.png'))
ZOMBIE_WALK_R2 = pygame.image.load(os.path.join('png', 'zombie_walkR2.png'))
ZOMBIE_WALK_L1 = pygame.image.load(os.path.join('png', 'zombie_walkL1.png'))
ZOMBIE_WALK_L2 = pygame.image.load(os.path.join('png', 'zombie_walkL2.png'))
ZOMBIE_DEAD_R = pygame.image.load(os.path.join('png', 'zombie_deadR.png'))
ZOMBIE_DEAD_L = pygame.image.load(os.path.join('png', 'zombie_deadL.png'))

ZOMBIE_WALK_R = [ZOMBIE_WALK_R1, ZOMBIE_WALK_R2]
ZOMBIE_WALK_L = [ZOMBIE_WALK_L1, ZOMBIE_WALK_L2]
ZOMBIE_DEAD_R = [ZOMBIE_DEAD_R, ZOMBIE_DEAD_R]
ZOMBIE_DEAD_L = [ZOMBIE_DEAD_L, ZOMBIE_DEAD_L]

# ---------------DUCH--------------
GHOST_STAND = pygame.image.load(os.path.join('png', 'ghost_stand.png'))
GHOST_WALK_L1 = pygame.image.load(os.path.join('png', 'ghost_normal_L.png'))
GHOST_WALK_R1 = pygame.image.load(os.path.join('png', 'ghost_normal_R.png'))
GHOST_WALK_L2 = pygame.image.load(os.path.join('png', 'ghost_walk_L.png'))
GHOST_WALK_R2 = pygame.image.load(os.path.join('png', 'ghost_walk_R.png'))
GHOST_DEAD_L = pygame.image.load(os.path.join('png', 'ghost_dead_L.png'))
GHOST_DEAD_R = pygame.image.load(os.path.join('png', 'ghost_dead_R.png'))

GHOST_WALK_L = [GHOST_WALK_L1, GHOST_WALK_L2]
GHOST_WALK_R = [GHOST_WALK_R1, GHOST_WALK_R2]
GHOST_DEAD_R = [GHOST_DEAD_R, GHOST_DEAD_R]
GHOST_DEAD_L = [GHOST_DEAD_L, GHOST_DEAD_L]

# ---------------SPINNER--------------
SPINNER_STAND = pygame.image.load(os.path.join('png', 'spinnerHalf.png'))
SPINNER_SPIN = pygame.image.load(os.path.join('png', 'spinnerHalf_spin.png'))
SPINNER_DEAD = pygame.image.load(os.path.join('png', 'spinnerHalf_dead.png'))

SPINNER_SPIN = [SPINNER_STAND, SPINNER_SPIN]
SPINNER_DEAD = [SPINNER_DEAD, SPINNER_DEAD]

# -----------------MYSZ--------------
MOUSE_STAND_L = pygame.image.load(os.path.join('png', 'mouse_left.png'))
MOUSE_STAND_R = pygame.image.load(os.path.join('png', 'mouse_right.png'))
MOUSE_DEAD_R = pygame.image.load(os.path.join('png', 'mouse_dead_right.png'))
MOUSE_DEAD_L = pygame.image.load(os.path.join('png', 'mouse_dead_left.png'))
MOUSE_WALK_L = pygame.image.load(os.path.join('png', 'mouse_walk_left.png'))
MOUSE_WALK_R = pygame.image.load(os.path.join('png', 'mouse_walk_right.png'))

MOUSE_WALK_L = [MOUSE_STAND_L, MOUSE_WALK_L]
MOUSE_WALK_R = [MOUSE_STAND_R, MOUSE_WALK_R]
MOUSE_DEAD_R = [MOUSE_DEAD_R, MOUSE_DEAD_R]
MOUSE_DEAD_L = [MOUSE_DEAD_L, MOUSE_DEAD_L]


# --------------------NIETOPERZ ------------
BAT_HANG = pygame.image.load(os.path.join('png', 'bat_hang.png'))
BAT_FLY_R1 = pygame.image.load(os.path.join('png', 'bat_flyR1.png'))
BAT_FLY_R2 = pygame.image.load(os.path.join('png', 'bat_flyR2.png'))
BAT_FLY_L1 = pygame.image.load(os.path.join('png', 'bat_flyL1.png'))
BAT_FLY_L2 = pygame.image.load(os.path.join('png', 'bat_flyL2.png'))
BAT_DEAD_L = pygame.image.load(os.path.join('png', 'bat_deadL.png'))
BAT_DEAD_R = pygame.image.load(os.path.join('png', 'bat_deadR.png'))

BAT_FLY_R_LIST = [BAT_FLY_R1, BAT_FLY_R2]
BAT_FLY_L_LIST = [BAT_FLY_L1, BAT_FLY_L2]
BAT_DEAD_R_LIST = [BAT_DEAD_R, BAT_DEAD_R]
BAT_DEAD_L_LIST = [BAT_DEAD_L, BAT_DEAD_L]

# ----------------------PAJĄK-------------
SPIDER_STAND_R = pygame.image.load(os.path.join('png', 'spider_standR.png'))
SPIDER_STAND_L = pygame.image.load(os.path.join('png', 'spider_standL.png'))
SPIDER_WALK_R1 = pygame.image.load(os.path.join('png', 'spider_walkR1.png'))
SPIDER_WALK_R2 = pygame.image.load(os.path.join('png', 'spider_walkR2.png'))
SPIDER_WALK_L1 = pygame.image.load(os.path.join('png', 'spider_walkL1.png'))
SPIDER_WALK_L2 = pygame.image.load(os.path.join('png', 'spider_walkL2.png'))
SPIDER_DEAD_L = pygame.image.load(os.path.join('png', 'spider_deadL.png'))
SPIDER_DEAD_R = pygame.image.load(os.path.join('png', 'spider_deadR.png'))
SPIDERWEB_R = pygame.image.load(os.path.join('png', 'spiderweb_R.png'))
SPIDERWEB_L = pygame.image.load(os.path.join('png', 'spiderweb_L.png'))



SPIDER_WALK_R_LIST = [SPIDER_WALK_R1, SPIDER_WALK_R2]
SPIDER_WALK_L_LIST = [SPIDER_WALK_L1, SPIDER_WALK_L2]
SPIDER_DEAD_R_LIST = [SPIDER_DEAD_R, SPIDER_DEAD_R]
SPIDER_DEAD_L_LIST = [SPIDER_DEAD_L, SPIDER_DEAD_L]

#--------------- CHMURA ------------
CLOUD_ENEMY = pygame.image.load(os.path.join('png', 'cloud_enemy.png'))


#-----FIREBALL BOSS -----------
BARNACLE_STAND = pygame.image.load(os.path.join('png', 'barnacle.png'))
BARNACLE_SHOOT = pygame.image.load(os.path.join('png', 'barnacle_bite.png'))
BARNACLE_DEAD = pygame.image.load(os.path.join('png', 'barnacle_dead.png'))

BARNACLE_WALK_R_LIST = [BARNACLE_STAND, BARNACLE_STAND]
BARNACLE_WALK_L_LIST = [BARNACLE_STAND, BARNACLE_STAND]
BARNACLE_DEAD_R_LIST = [BARNACLE_DEAD, BARNACLE_DEAD]
BARNACLE_DEAD_L_LIST = [BARNACLE_DEAD, BARNACLE_DEAD]

FIREBALL_LEFT = pygame.image.load(os.path.join('png', 'fireball_left.png'))
FIREBALL_RIGHT = pygame.image.load(os.path.join('png', 'fireball_right.png'))


# ----------------------grafika NPC------------------------
# ----------------------SOLIDER---------------------------
SOLDIER_STAND_R = pygame.image.load(os.path.join('png', 'soldier_stand_R.png'))
SOLDIER_TALK_R = pygame.image.load(os.path.join('png', 'soldier_talk_R.png'))
SOLDIER_STAND_L = pygame.image.load(os.path.join('png', 'soldier_stand_L.png'))
SOLDIER_TALK_L = pygame.image.load(os.path.join('png', 'soldier_talk_L.png'))

# ----------------------SIOSTRA---------------------------
FEMALE_STAND_R = pygame.image.load(os.path.join('png', 'female_stand_R.png'))
FEMALE_TALK_R = pygame.image.load(os.path.join('png', 'female_talk_R.png'))
FEMALE_STAND_L = pygame.image.load(os.path.join('png', 'female_stand_L.png'))
FEMALE_TALK_L = pygame.image.load(os.path.join('png', 'female_talk_L.png'))


# -----------------GRAFIKA ITEMS----------------------------
SHOTGUN = pygame.image.load(os.path.join('png', 'shotgun.png'))
LASER_GUN = pygame.image.load(os.path.join('png', 'raygunBig.png'))
POWER_UP = pygame.image.load(os.path.join('png', 'powerup_bubble.png'))
HEART = pygame.image.load(os.path.join('png', 'heart.png'))
PU_ICON = pygame.image.load(os.path.join('png', 'swirl_blue.png'))
KEY_YELLOW = pygame.image.load(os.path.join('png', 'keyYellow.png'))
LOCK_YELLOW = pygame.image.load(os.path.join('png', 'lockYellow.png'))
LEVER_MID = pygame.image.load(os.path.join('png', 'leverMid.png'))
LEVER_LEFT = pygame.image.load(os.path.join('png', 'leverLeft.png'))
BOX = pygame.image.load(os.path.join('png', 'box.png'))
SPECIAL_BOX = pygame.image.load(os.path.join('png', 'special_box.png'))
LASER_BULLET = pygame.image.load(os.path.join('png','laserPurple.png'))
STEM = pygame.image.load(os.path.join('png', 'stem.png'))
STEM_BASE = pygame.image.load(os.path.join('png', 'stemBaseAlt.png'))
STEM_TOP = pygame.image.load(os.path.join('png', 'stemTop.png'))
BUSH = pygame.image.load(os.path.join('png', 'bush.png'))
BUSH_REVERSE = pygame.image.load(os.path.join('png', 'bush_reverse.png'))
SPIKE_BOTTOM = pygame.image.load(os.path.join('png', 'spike_bottom.png'))
TORCH_OFF = pygame.image.load(os.path.join('png', 'torchOff.png'))
TORCH_ON = pygame.image.load(os.path.join('png', 'torchOn.png'))
LOCK_BLUE = pygame.image.load(os.path.join('png', 'lockBlue.png'))
KEY_BLUE = pygame.image.load(os.path.join('png', 'keyBlue.png'))
DOORS_CLOSED_MID = pygame.image.load(os.path.join('png', 'doorOpen_mid.png'))
DOORS_CLOSED_TOP = pygame.image.load(os.path.join('png', 'doorOpen_mid.png'))
SPRING = pygame.image.load(os.path.join('png', 'spring.png'))
SPRING_IN = pygame.image.load(os.path.join('png', 'spring_in.png'))
SPRING_OUT = pygame.image.load(os.path.join('png', 'spring_out.png'))

class Level:
    def __init__(self, player=None):
        self.set_of_platforms = set()
        self.set_of_bullets = pygame.sprite.Group()
        self.set_of_items = pygame.sprite.Group()
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_enemy_bullets = pygame.sprite.Group()
        self.set_of_undead_enemies = pygame.sprite.Group()
        self.set_of_npcs = pygame.sprite.Group()
        self.set_of_ladders = set()
        self.set_of_walls = set()
        self.player = player
        self.world_shift = 0
        self.objective = ""

    def update(self):
        for platform in self.set_of_platforms:
            platform.update()

        self.set_of_bullets.update()
        self.set_of_enemy_bullets.update()
        self.set_of_enemies.update()
        self.set_of_npcs.update()
        self.set_of_undead_enemies.update()
        for ladder in self.set_of_ladders:
            ladder.update()

        self._delete_bullets()
        self.set_of_items.update()


        # przesunięcie ekranu gdy gracz jest blisko prawej krawędzi
        if self.player.rect.right >= 600:
            diff = self.player.rect.right - 600
            self.player.rect.right = 600
            self._shift_world(-diff)

        # przesunięcie ekranu gdy gracz jest blisko lewej krawędzi
        if self.player.rect.left <= 150:
            diff = 150 - self.player.rect.left
            self.player.rect.left = 150
            self._shift_world(diff)

    def draw(self, surface):

        self.set_of_npcs.draw(surface)
        self.set_of_bullets.draw(surface)
        self.set_of_enemy_bullets.draw(surface)
        self.set_of_items.draw(surface)
        self.set_of_enemies.draw(surface)
        self.set_of_undead_enemies.draw(surface)


        for platform in self.set_of_platforms:
            platform.draw(surface)

        for ladder in self.set_of_ladders:
            ladder.draw(surface)

        self._text(surface)

    def _shift_world(self, shift_x):
        self.world_shift += shift_x

        for platform in self.set_of_platforms | self.set_of_walls:
            platform.rect.x += shift_x

        for bullet in self.set_of_bullets:
            bullet.rect.x += shift_x

        for bullet in self.set_of_enemy_bullets:
            bullet.rect.x += shift_x

        for item in self.set_of_items:
            item.rect.x += shift_x

        for enemy in self.set_of_enemies:
            enemy.rect.x += shift_x

        for enemy in self.set_of_undead_enemies:
            enemy.rect.x += shift_x

        for ladder in self.set_of_ladders:
            ladder.rect.x += shift_x

        for npc in self.set_of_npcs:
            npc.rect.x += shift_x

    def _delete_bullets(self):
        pygame.sprite.groupcollide(
            self.set_of_bullets, self.set_of_enemy_bullets, True,True)
        pygame.sprite.groupcollide(
            self.set_of_bullets, self.set_of_platforms,True,False)
        pygame.sprite.groupcollide(
            self.set_of_enemy_bullets, self.set_of_platforms,True,False)
        bullets = set(self.set_of_bullets) | set(self.set_of_enemy_bullets)

        for bullet in bullets:
            ##            # sprawdzamy kolizję z platformami i usuwamy pociski
            ##            if pygame.sprite.spritecollide(bullet, self.set_of_platforms):
            ##                bullet.kill()
            # sprawdzamy czy pocisk wyleciał poza plnszę i usuwamy go
            if bullet.rect.right > constants.WIDTH or bullet.rect.left < 0:
                bullet.kill()

            # sprawdzamy czy pocisk trafił we wroga i usuwamy obiekty
            if not isinstance(bullet, items.EnemyBullet):
                coliding_enemise = pygame.sprite.spritecollide(bullet,
                                                               self.set_of_enemies, False)
                for enemy in coliding_enemise:
                    bullet.kill()
                    if enemy.lifes:
                        enemy.lifes -= 1 * bullet.power
                        if not enemy.lifes:
                            enemy.count = 0

            coliding_items = pygame.sprite.spritecollide(bullet, self.set_of_items, False)
            for item in coliding_items:
                if item.name == 'box':
                    if not bullet.power >= 5:
                        bullet.kill()
                        if item.lifes:
                            item.lifes -= 1 * bullet.power

    def _text(self, surface):
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("monospace", 15)
        # render text
        label = myfont.render(self.objective, 1, (255, 255, 0))
        surface.blit(label, (0, 65))

        # npc dialog
        for npc in self.set_of_npcs:
            if npc.talking:
                label = myfont.render(npc.dialog, 1, (0, 0, 255))
                surface.blit(label, (npc.rect.x - 100, npc.rect.y))

        # player życia
        if self.player.lifes:
            for i in range(self.player.lifes):
                surface.blit(HEART, [30 * i, 5])



        # aktualna broń
        for item in self.player.items:
            if item.name == 'yellow key':
                surface.blit(KEY_YELLOW, [940, 40])
            if item.name == 'blue key':
                surface.blit(KEY_BLUE, [940, 40])
            if item.name == self.player.actual_weapon:
                if item.name == 'laser gun':
                    label = myfont.render(str(self.player.ammo), 1, (255, 255, 0))
                    surface.blit(label, [915, 5])
                surface.blit(item.image, [930, 5])


        # specjany atak icon
        for i in range(self.player.power):
            surface.blit(PU_ICON, (30 * i, 30))


class Level_1(Level):
    def __init__(self, player):
        super().__init__(player)
        self.level_limit = -4200
        self.background = BACKGROUND2.convert()
        self.wp = [[6000, 40, -0, constants.HEIGHT - 70]]
        self.wp2 = [[140, 56, 1800, constants.HEIGHT - 600]]
        self.wp3 = [[280, 70, 1285, constants.HEIGHT - 140],
                    [280, 70, 1285, constants.HEIGHT - 210],
                    [280, 70, 2500, constants.HEIGHT - 140],
                    [280, 70, 2500, constants.HEIGHT - 210]]
        self.objective = "Miasto jest w niebezpieczeństwie! Porozmawiaj z sierżantem"

        # -----------------------PLATFORMY---------------------------
        for p in self.wp:
            platform = platforms.Platform(*p)
            platform.image_list = STONE_GROUND_LIST
            self.set_of_platforms.add(platform)

        for p in self.wp2:
            platform = platforms.Platform(*p)
            platform.image_list = METAL_LIST
            self.set_of_platforms.add(platform)

        for p in self.wp3:
            platform = platforms.BrickPlatform(*p)
            platform.image_list = STONE
            self.set_of_platforms.add(platform)

        for i in range(1560, 2500, 40):
            platform = platforms.CavePlatform(70, 70, i, constants.HEIGHT - 140)
            platform.image_list = CAVE
            self.set_of_platforms.add(platform)

        # tworzymy ściany
        ws_walls = [[150, 980, -150, 0]]
        for el in ws_walls:
            object_W = platforms.Wall(*el)
            self.set_of_walls.add(object_W)

        # tworzymy ruchomą platformę (ruch w pionie)
        mp_y = platforms.MovingPlatform(70, 40, 1600, 300)
        mp_y.image_list = BEAM_LIST
        mp_y.boundary_top = 300
        mp_y.boundary_bottom = constants.HEIGHT - 170
        mp_y.movement_y = 1
        mp_y.player = self.player
        mp_y.level = self
        self.set_of_platforms.add(mp_y)

        # --------------------NPCS-----------------------------
        solider = npcs.Npc(SOLDIER_STAND_R, SOLDIER_STAND_L, SOLDIER_TALK_R, SOLDIER_TALK_L, None)
        solider.level = self
        solider.player = self.player
        solider.name = "Soldier"
        solider.rect.x = 600
        solider.rect.y = constants.HEIGHT - 180
        self.set_of_npcs.add(solider)

        # --------------------PRZECIWNICY ----------------------

        #------------------- spinner ---------------
        enemy = enemies.Spinner_Enemy(SPINNER_STAND, SPINNER_SPIN, SPINNER_SPIN,
                                      SPINNER_DEAD, SPINNER_DEAD, None, 0, 0, 3000, constants.HEIGHT - 100)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)

        # ------------------- mysz -----------------
        enemy = enemies.Mouse_Enemy(MOUSE_STAND_R, MOUSE_WALK_R, MOUSE_WALK_L,
                                    MOUSE_DEAD_R, MOUSE_DEAD_L, None,
                                    0, 0, 3500, constants.HEIGHT - 105)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)

        # ------------------- mysz -----------------
        enemy = enemies.Mouse_Enemy(MOUSE_STAND_R, MOUSE_WALK_R, MOUSE_WALK_L,
                                    MOUSE_DEAD_R, MOUSE_DEAD_L, None,
                                    0, 0, 3300, constants.HEIGHT - 105)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)

        # -------------------ITEMKI------------------

        ammo = items.Item(LASER_BULLET, 'laser ammo')
        ammo.rect.x = 1229
        ammo.rect.bottom = constants.HEIGHT - 70
        self.set_of_items.add(ammo)

        box = items.Box(BOX, 'box')
        box.level = self
        box.rect.x = 1229
        box.rect.bottom = constants.HEIGHT - 70
        self.set_of_items.add(box)

        box = items.Box(BOX, 'box')
        box.level = self
        box.rect.x = 1170
        box.rect.bottom = constants.HEIGHT - 70
        self.set_of_items.add(box)

        power_up = items.Item(POWER_UP, 'power up')
        power_up.rect.x = 3500
        power_up.rect.bottom = constants.HEIGHT - 100
        self.set_of_items.add(power_up)

        key = items.Item(KEY_YELLOW, 'yellow key')
        key.rect.x = 1850
        key.rect.y = constants.HEIGHT - 500
        self.set_of_items.add(key)


    def draw(self, surface):
        # ---------- TLO -----------------
        surface.fill(constants.LIGHTBLUE)
        surface.blit(self.background, (self.world_shift // 5, 0))
        for wall in self.set_of_walls:
            wall.draw(surface, INDUSTRIAL_LIST, INDUSTRIAL_CORNER_LIST)
        super().draw(surface)


class Level_2(Level):
    def __init__(self, player):
        super().__init__(player)
        self.level_limit = -4200
        self.background = BACKGROUND.convert()
        self.wp = [[6000, 40, -0, constants.HEIGHT - 80], [6000, 40, 0, constants.HEIGHT - 40]]
        self.wp2 = [[336, 56, 500, constants.HEIGHT - 180], [336, 56, 0, constants.HEIGHT - 500],
                    [336, 56, 520, constants.HEIGHT - 350], [336, 56, 500, constants.HEIGHT - 650],
                    [336, 56, 2600, constants.HEIGHT - 500]]
        self.objective = "Oczyść miasto z potworów i wyrusz dalej!"


        # ---------------------- PLATFORMY -----------------

        for p in self.wp:
            platform = platforms.Platform(*p)
            platform.image_list = METAL_LIST
            self.set_of_platforms.add(platform)

        for p in self.wp2:
            platform = platforms.BrickPlatform(*p)
            platform.image_list = WALL_BRICK
            self.set_of_platforms.add(platform)


        # ----------Platforma reagująca na gracza ------------
        mp_y = platforms.MovingStandPlatform(336, 56, 870, constants.HEIGHT - 600)
        mp_y.image_list = WALL_BRICK
        mp_y.boundary_top = constants.HEIGHT - 600
        mp_y.boundary_bottom = constants.HEIGHT - 170
        mp_y.player = self.player
        mp_y.level = self
        self.set_of_platforms.add(mp_y)

        # ---------Przekładnia do platformy -----------
        lever = items.Lever(LEVER_LEFT, LEVER_MID, 'lever')
        lever.rect.x = 2600
        lever.rect.bottom = constants.HEIGHT - 500
        self.set_of_items.add(lever)

        # ---------------Platforma z przekładnią ------------
        mp_y = platforms.MovingLeverPlatform(336,56, 3380, constants.HEIGHT - 650)
        mp_y.image_list = WALL_BRICK
        mp_y.boundary_top = constants.HEIGHT - 650
        mp_y.boundary_bottom = constants.HEIGHT - 400
        mp_y.player = self.player
        mp_y.level = self
        mp_y.lever = lever
        self.set_of_platforms.add(mp_y)

        # --------------- PLATFORMY Z WROGIEM -------------------
        ws_enemy_platform = [[342, 56, 1500, 200], [616, 56, 3180, constants.HEIGHT - 326]]
        for el in ws_enemy_platform:
            object_P = platforms.BrickPlatform(*el)
            object_P.image_list = WALL_BRICK
            self.set_of_platforms.add(object_P)
            platform_enemy = enemies.Platform_Enemy(ZOMBIE_STAND_R, ZOMBIE_WALK_R, ZOMBIE_WALK_L,
                                                    ZOMBIE_DEAD_R, ZOMBIE_DEAD_L, object_P,
                                                    random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)

        # ------------------- ściany ---------------------
        ws_walls = [[150, 980, -150, 0]]
        for el in ws_walls:
            object_W = platforms.Wall(*el)
            self.set_of_walls.add(object_W)


        # --------------------- WROGOWIE ---------------------

        # ---------------------------zombie------------------
        enemy = enemies.Zombie_Enemy(ZOMBIE_STAND_R, ZOMBIE_WALK_R, ZOMBIE_WALK_L,
                                     ZOMBIE_DEAD_R, ZOMBIE_DEAD_L, None,
                                     random.choice([-3, -2, -1, 1, 2, 3]), 0, 420, constants.HEIGHT - 190)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)

        enemy = enemies.Zombie_Enemy(ZOMBIE_STAND_R, ZOMBIE_WALK_R, ZOMBIE_WALK_L,
                                     ZOMBIE_DEAD_R, ZOMBIE_DEAD_L, None,
                                     random.choice([-2, -1, 1, 2]), 0, 3100, constants.HEIGHT - 190)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)

        # --------------------------boss DUCH -------------------------------
        enemy = enemies.Ghost_Boss(GHOST_STAND, GHOST_WALK_R, GHOST_WALK_L, GHOST_DEAD_R, GHOST_DEAD_L, None,
                                   3, 2, 3100, constants.HEIGHT - 190)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)


        # ------------------------------ITEMKI--------------------------------------


        # ----------------------------DRABINY---------------------------
        for i in range(170, 381, 70):
            ladder = items.Ladder(3100, constants.HEIGHT - i, LADDER)
            self.set_of_ladders.add(ladder)

        for i in range(170, 381, 70):
            ladder = items.Ladder(3800, constants.HEIGHT - i, LADDER)
            self.set_of_ladders.add(ladder)


        # --------------------------- boxy -------------------------------
        # ---------sejf-----------------
        box = items.Box(LOCK_YELLOW, 'lock box1')
        box.level = self
        box.rect.x = 0
        box.lifes = 10000
        box.rect.bottom = constants.HEIGHT - 500
        self.set_of_items.add(box)

        # ----------zwykłe pudła -----------------
        for i in range(45, 269,56):
            box = items.Box(BOX, 'box')
            box.level = self
            box.rect.x = i
            box.rect.bottom = constants.HEIGHT - 500
            self.set_of_items.add(box)


        for i in range(2600, 2768,56):
            box = items.Box(BOX, 'box')
            box.level = self
            box.rect.x = i
            box.rect.bottom = constants.HEIGHT - 500
            self.set_of_items.add(box)


        box = items.Box(BOX, 'box')
        box.level = self
        box.rect.x = 1400
        box.rect.bottom = constants.HEIGHT - 80
        self.set_of_items.add(box)

        for i in range(1, 8):
            box = items.Box(BOX, 'box')
            box.level = self
            box.rect.x = 1400
            box.rect.bottom = constants.HEIGHT - (56 * i) - 80
            self.set_of_items.add(box)


        # ---------------- powerup --------------------
        power_up = items.Item(POWER_UP, 'power up')
        power_up.rect.x = 1500
        power_up.rect.bottom = constants.HEIGHT - 100
        self.set_of_items.add(power_up)

        power_up = items.Item(POWER_UP, 'power up')
        power_up.rect.x = 3570
        power_up.rect.bottom = constants.HEIGHT - 700
        self.set_of_items.add(power_up)

    def draw(self, surface):
        surface.fill(constants.LIGHTBLUE)
        surface.blit(self.background, (self.world_shift // 5, 0))
        for wall in self.set_of_walls:
            wall.draw(surface, INDUSTRIAL_LIST, INDUSTRIAL_CORNER_LIST)
        super().draw(surface)


class Level_3(Level):
    def __init__(self, player=None):
        super().__init__(player)
        self.level_limit = -4500
        wp = [[2520, 40, 0, constants.HEIGHT - 70], [200, 40, 1600, constants.HEIGHT - 110],
              [2560, 40, 3640, constants.HEIGHT - 70]]
        wp2 = [[280, 65, 15, 420],[280,65, 0, 200], [280, 65, 400, 550], [280, 65, 850, 400],
                [280, 65, 3250, 550], [280, 65, 3250, 170]]
        self.objective = "Znajdź siostrę i ją uratuj"

        # ------------------------ PLATFORMY ----------------------
        # tworzymy platformy
        for p in wp:
            platform = platforms.Platform(*p)
            platform.image_list = DIRTY_GROUND_LLST
            self.set_of_platforms.add(platform)

        for p in wp2:
            platform = platforms.GrassPlatform(*p)
            platform.image_list = GROUND_GRASS
            self.set_of_platforms.add(platform)

        # ----------Platforma reagująca na gracza ------------
        mp_y = platforms.MovingStandPlatform(280, 65, 2100, constants.HEIGHT - 550)
        mp_y.image_list = GROUND_GRASS
        mp_y.one_el = True
        mp_y.boundary_top = constants.HEIGHT - 550
        mp_y.boundary_bottom = constants.HEIGHT - 170
        mp_y.player = self.player
        mp_y.level = self
        self.set_of_platforms.add(mp_y)

        ws_walls = [[280, 980, -280, 0], [2540, 70, 0, -60],
                    [700, 980, 5600, 0], [2560,70, 3640, -60]]
        # tworzymy ściany
        for el in ws_walls:
            object_W = platforms.Wall(*el)
            self.set_of_walls.add(object_W)

        # --------------------- POCHODNIE DO PLATFORMY ----------------
        torch1 = items.Torch(TORCH_OFF, TORCH_ON, 'torch')
        torch1.rect.x = 25
        torch1.status = 'off'
        torch1.rect.bottom = 430
        self.set_of_items.add(torch1)

        torch2 = items.Torch(TORCH_OFF, TORCH_ON, 'torch')
        torch2.rect.x = 1560
        torch2.status = 'off'
        torch2.rect.bottom = constants.HEIGHT - 60
        self.set_of_items.add(torch2)

        torch3 = items.Torch(TORCH_OFF, TORCH_ON, 'torch')
        torch3.rect.x = 1785
        torch3.status = 'on'
        torch3.rect.bottom = constants.HEIGHT - 60
        self.set_of_items.add(torch3)

        torch4 = items.Torch(TORCH_OFF, TORCH_ON, 'torch')
        torch4.rect.x = 2450
        torch4.status = 'off'
        torch4.rect.bottom = constants.HEIGHT - 60
        self.set_of_items.add(torch4)

        # ----------------- PLATFORMA Z POCHODNIAMI --------------------
        mp_y = platforms.MovingTorchPlatform(56,768, 2520, constants.HEIGHT - 800)
        mp_y.image_list = WALL_L
        mp_y.boundary_top = constants.HEIGHT - 800
        mp_y.boundary_bottom = 1000
        mp_y.player = self.player
        mp_y.level = self
        mp_y.torches.append(torch1)
        mp_y.torches.append(torch2)
        mp_y.torches.append(torch3)
        mp_y.torches.append(torch4)
        self.set_of_platforms.add(mp_y)


        # ruchoma platform (ruch w poziomie)
        mp_x = platforms.MovingPlatform(210, 40, 1270, 300)
        mp_x.image_list = METAL_LIST
        mp_x.boundary_left = 1270
        mp_x.boundary_right = 1700
        mp_x.movement_x = 2
        mp_x.player = self.player
        mp_x.level = self
        self.set_of_platforms.add(mp_x)

        # ruchoma platform (ruch w pionie)
        mp_y = platforms.MovingPlatform(280, 40, 2630, 600)
        mp_y.image_list = METAL_LIST
        mp_y.boundary_top = 300
        mp_y.boundary_bottom = constants.HEIGHT - 30
        mp_y.movement_y = 1
        mp_y.player = self.player
        mp_y.level = self
        self.set_of_platforms.add(mp_y)


        # ----------- platformy z wrogrami -----------
        ws_enemy_platform = [[280, 65, 400, 250]]
        for el in ws_enemy_platform:
            object_P = platforms.GrassPlatform(*el)
            object_P.image_list = GROUND_GRASS
            self.set_of_platforms.add(object_P)
            platform_enemy = enemies.Platform_Enemy(ZOMBIE_STAND_R, ZOMBIE_WALK_R, ZOMBIE_WALK_L,
                                                    ZOMBIE_DEAD_R, ZOMBIE_DEAD_L, object_P,
                                                    random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)


        # -------------------- WROGOWIE ---------------------------

        # --------------- NIETOPERZ ------------------------
        bat_enemy = enemies.Bat_Enemy(
            BAT_HANG, BAT_FLY_R_LIST, BAT_FLY_L_LIST,
            BAT_DEAD_R_LIST, BAT_DEAD_L_LIST,
            movement_x = random.choice([-3,-2,2,3]),
            movement_y = random.choice([-3,-2,-1,1,2,3]))
        bat_enemy.level = self
        bat_enemy.rect.x = 750
        bat_enemy.rect.top = constants.HEIGHT - 400
        bat_enemy.boundary_top = 70
        bat_enemy.boundary_bottom = constants.HEIGHT - 100
        bat_enemy.boundary_left = 500
        bat_enemy.boundary_right = 1000
        self.set_of_enemies.add(bat_enemy)


        # -------------------------- PAJĄK ------------------------
        spider_enemy = enemies.Spider_Enemy(SPIDER_STAND_R, SPIDER_WALK_R_LIST, SPIDER_WALK_L_LIST,
                                         SPIDER_DEAD_R_LIST, SPIDER_DEAD_L_LIST, None, 0,0, 1200, constants.HEIGHT - 120)
        spider_enemy.movement_x = random.choice([-2, 2])
        spider_enemy.player = self.player
        spider_enemy.level = self
        self.set_of_enemies.add(spider_enemy)

        # ------------------------- CHMURA -----------------------
        cloud_enemy = enemies.Cloud_Enemy(CLOUD_ENEMY,CLOUD_ENEMY, CLOUD_ENEMY, CLOUD_ENEMY, CLOUD_ENEMY, 2900, 3250)
        cloud_enemy.movement_x = 2
        cloud_enemy.rect.x = 2900
        cloud_enemy.rect.bottom = 400
        cloud_enemy.level = self
        self.set_of_undead_enemies.add(cloud_enemy)

        # --------------------------- MYSZ ---------------------------
        enemy = enemies.Mouse_Enemy(MOUSE_STAND_R, MOUSE_WALK_R, MOUSE_WALK_L,
                                    MOUSE_DEAD_R, MOUSE_DEAD_L, None,
                                    0, 0, 4000, constants.HEIGHT - 105)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)

        # -------------------------- MYSZ -------------------------------
        enemy = enemies.Mouse_Enemy(MOUSE_STAND_R, MOUSE_WALK_R, MOUSE_WALK_L,
                                    MOUSE_DEAD_R, MOUSE_DEAD_L, None,
                                    0, 0, 4200, constants.HEIGHT - 105)
        enemy.level = self
        enemy.player = self.player
        self.set_of_enemies.add(enemy)


        # ------------------------ FIREBALL BOSS ----------------------------------------
        enemy = enemies.Barnacle_Enemy(BARNACLE_STAND, BARNACLE_WALK_R_LIST, BARNACLE_WALK_L_LIST, BARNACLE_DEAD_R_LIST
                                       ,BARNACLE_DEAD_L_LIST)
        enemy.level = self
        enemy.player = self.player
        enemy.rect.x = 4700
        enemy.rect.bottom = constants.HEIGHT - 70
        self.set_of_enemies.add(enemy)

        # --------------------NPCS-----------------------------
        female = npcs.Npc(FEMALE_STAND_R, FEMALE_STAND_L, FEMALE_TALK_R, FEMALE_TALK_L, None)
        female.level = self
        female.player = self.player
        female.name = "Sister"
        female.rect.x = 5400
        female.dialog = "CAŁE SZCZĘŚCIE ŻE JESTEŚ, BAŁAM SIĘ ŻE JUŻ PO MNIE"
        female.rect.y = constants.HEIGHT - 180
        self.set_of_npcs.add(female)

        # --------------------------------- ITEMKI ------------------------------

        # ------ budowanie drzewa -----------------
        item = items.Tree(STEM_BASE, 'stem base')
        item.rect.x = 720
        item.rect.bottom = constants.HEIGHT - 70
        self.set_of_items.add(item)

        item = items.Tree(STEM, 'stem')
        item.rect.x = 720
        item.rect.bottom = constants.HEIGHT - 140
        self.set_of_items.add(item)

        item = items.Tree(STEM, 'stem')
        item.rect.x = 720
        item.rect.bottom = constants.HEIGHT - 210
        self.set_of_items.add(item)

        item = items.Tree(STEM_TOP, 'stem')
        item.rect.x = 720
        item.rect.bottom = constants.HEIGHT - 280
        self.set_of_items.add(item)

        item = items.Tree(BUSH, 'bush')
        item.rect.x = 660
        item.rect.bottom = constants.HEIGHT - 350
        self.set_of_items.add(item)

        item = items.Tree(BUSH_REVERSE, 'bush reverse')
        item.rect.x = 660
        item.rect.bottom = constants.HEIGHT - 278
        self.set_of_items.add(item)

        # -------------- spadająca skała -----------
        item = items.Spike(SPIKE_BOTTOM, 'spike')
        item.rect.x = 2000
        item.rect.top = 10
        item.player = self.player
        item.level = self
        self.set_of_items.add(item)

        # -------------- spadająca skała -----------
        item = items.Spike(SPIKE_BOTTOM, 'spike')
        item.rect.x = 3700
        item.rect.top = 10
        item.player = self.player
        item.level = self
        self.set_of_items.add(item)

        #------------ power up -----------------
        power_up = items.Item(POWER_UP, 'power up')
        power_up.rect.x = 2200
        power_up.rect.bottom = constants.HEIGHT - 600
        self.set_of_items.add(power_up)

        #------------- skrzynia ---------------
        box = items.Box(LOCK_BLUE, 'lock box2')
        box.level = self
        box.rect.x = 0
        box.lifes = 10000
        box.rect.bottom = 200
        self.set_of_items.add(box)

        # --------------- klucz --------------
        key = items.Item(KEY_BLUE, 'blue key')
        key.rect.x = 3300
        key.rect.y = 100
        self.set_of_items.add(key)

        # # ---------------- drzwi----------------
        # doors = items.Item(DOORS_CLOSED_MID, 'doors mid')
        # doors.rect.x = 5600
        # doors.rect.bottom = constants.HEIGHT - 70
        # self.set_of_items.add(doors)

        # ---------------- sprężyna --------------
        spring = items.Spring(SPRING, SPRING_IN, SPRING_OUT, 'spring', constants.HEIGHT - 50)
        spring.rect.x = 3800
        spring.rect.bottom = constants.HEIGHT - 50
        spring.player = self.player
        self.set_of_items.add(spring)

        # ----------------budowanie drzewa -----------------
        item = items.Tree(STEM_BASE, 'stem base')
        item.rect.x = 4200
        item.rect.bottom = constants.HEIGHT - 70
        self.set_of_items.add(item)
        item = items.Tree(STEM, 'stem')
        item.rect.x = 4200
        item.rect.bottom = constants.HEIGHT - 140
        self.set_of_items.add(item)

        item = items.Tree(STEM, 'stem')
        item.rect.x = 4200
        item.rect.bottom = constants.HEIGHT - 210
        self.set_of_items.add(item)

        item = items.Tree(STEM_TOP, 'stem')
        item.rect.x = 4200
        item.rect.bottom = constants.HEIGHT - 280
        self.set_of_items.add(item)

        item = items.Tree(BUSH, 'bush')
        item.rect.x = 4140
        item.rect.bottom = constants.HEIGHT - 350
        self.set_of_items.add(item)

        item = items.Tree(BUSH_REVERSE, 'bush reverse')
        item.rect.x = 4140
        item.rect.bottom = constants.HEIGHT - 278
        self.set_of_items.add(item)


    def draw(self, surface):
        for wall in self.set_of_walls:
            wall.draw(surface, WALL_LIST, WALL_CORNER_LIST)
        super().draw(surface)