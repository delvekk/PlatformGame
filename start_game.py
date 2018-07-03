import pygame, os, player, constants, text, levels,menu_elements

# centrowanie okna
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
#-----------------------DŹWIĘK-------------------------------
pygame.mixer.init(44100, 16, 2, 4096)
pygame.mixer.music.set_volume(0.7)
menu_song = pygame.mixer.music.load(os.path.join('sounds', 'menu.mp3'))
foot_sound1 = pygame.mixer.Sound(os.path.join('sounds', 'footstep04.ogg'))
foot_sound2 = pygame.mixer.Sound(os.path.join('sounds', 'footstep04.ogg'))
take_item_sound = pygame.mixer.Sound(os.path.join('sounds', 'handleCoins2.ogg'))
shoot_sound =pygame.mixer.Sound(os.path.join('sounds', 'shot_sound.ogg'))
laser_shoot_sound =pygame.mixer.Sound(os.path.join('sounds', 'laser_shot.ogg'))
talking_npc = pygame.mixer.Sound(os.path.join('sounds', 'talking.ogg'))
special_attack = pygame.mixer.Sound(os.path.join('sounds', 'special_attack.ogg'))

sound_list_player = []
sound_list_player.append(foot_sound1)
sound_list_player.append(foot_sound2)
sound_list_player.append(take_item_sound)
sound_list_player.append(shoot_sound)
sound_list_player.append(laser_shoot_sound)
sound_list_player.append(talking_npc)
sound_list_player.append(special_attack)
#-----------------------------------------------------
## ustawienia ekranu i gry
SIZESCREEN = WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode(SIZESCREEN)
pygame.display.set_caption('Platform game...')
clock = pygame.time.Clock()

# konkretyzacja obiektów
player = player.Player(player.STAND_R, sound_list_player)

# lista leveli
level_list = []
level_list.append(levels.Level_1(player))
level_list.append(levels.Level_2(player))
level_list.append(levels.Level_3(player))
# nr aktualnego levelu
current_level_no = 0
# aktualny level
current_level = level_list[current_level_no]

player.level = current_level
player.rect.x = 70
player.rect.y = HEIGHT - 250
finish_text = text.Text('KONIEC GRY', constants.DARKRED)
start_button = menu_elements.Button("START/WZNÓW", 100, 40, constants.LIGHTBLUE, constants.DARKRED, constants.WIDTH//2, constants.HEIGHT//2)
exit_button = menu_elements.Button("WYJŚCIE", 100, 40, constants.LIGHTBLUE, constants.DARKRED, constants.WIDTH//2, constants.HEIGHT//2 + 200)
# głowna pętla gry
window_open = True
active_game = False
pygame.mixer.music.play(-1)
while window_open:
    screen.fill(constants.LIGHTBLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = True
                active_game = False
                break
        elif event.type == pygame.QUIT:
            window_open = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                active_game = True
                pygame.time.delay(500)
                background_song = pygame.mixer.music.load(os.path.join('sounds', 'background_music.mp3'))
                pygame.mixer.music.play(-1)
            if exit_button.rect.collidepoint(pygame.mouse.get_pos()):
                window_open = False
                info = False
                pygame.time.delay(500)
        if active_game:
            player.get_event(event)
    if active_game:
        if not player.lifes:
            active_game = False
            pygame.time.delay(500)
            screen.fill(constants.LIGHTRED)
            finish_text.rect.center = WIDTH // 2, HEIGHT // 2
            finish_text.draw(screen)
            pygame.display.flip()
            pygame.time.delay(2000)
            menu_song = pygame.mixer.music.load(os.path.join('sounds', 'menu.mp3'))
            pygame.mixer.music.play(-1)
            player.items.clear()
            player.lifes = 2
            level_list = []
            level_list.append(levels.Level_1(player))
            level_list.append(levels.Level_2(player))
            level_list.append(levels.Level_3(player))
            current_level_no = 0
            current_level = level_list[current_level_no]
            player.level = current_level


        # aktualna pozycja gracza
        current_position = player.rect.x + current_level.world_shift
        # jeśli aktualna pozycja < level limit i wszyscy wrogowie zabici to....
        if current_position < current_level.level_limit and len(current_level.set_of_enemies) == 0:
            player.rect.x = 50
            player.rect.y = 500
            # przejdz do nastepnego levela jesli taki jest
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        #rysowanie i aktualizacja obiektów
        current_level.draw(screen)
        player.update()
        player.draw(screen)
        current_level.update()
    else:
        screen.blit(constants.MENU.convert(), constants.BLACK)
        #screen.fill(constants.LIGHTBLUE)
        start_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()

    #aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(45)




pygame.quit()
