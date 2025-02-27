import pygame
import random

def display_score():
    current_score = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = font.render(f'{current_score}',False, 'black')
    score_rect = score_surf.get_rect(center = (1000, 100))
    screen.blit(score_surf,score_rect)
    return current_score
def obs_movement(obs_list):
    if obs_list:
        for obs_rect in obs_list:
            obs_rect.x -= 12
            screen.blit(monster1, obs_rect)
            return obs_list
    else: return []

pygame.init()
screen = pygame.display.set_mode((2000,1000))
clock = pygame.time.Clock()
pygame.display.set_caption("JUMPER")
font = pygame.font.Font('Game/Font/Font.ttf', 100)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.transform.rotozoom(pygame.image.load('Game/sky/sky.jpg').convert_alpha(),0,2)
ground_surface = pygame.image.load('Game/Ground/Aground.webp').convert_alpha()

monster1 = pygame.transform.rotozoom(pygame.image.load('Game/obs/monster1.png').convert_alpha(),0,2)
monster1_rect = monster1.get_rect(bottomleft = (2000,800))

obs_rect_list = []

character_suface = pygame.transform.rotozoom(pygame.image.load('Game/Char/smash-straight1.png').convert_alpha(),0,2)
character_rectangle = character_suface.get_rect(midbottom = (200, 800))

character_stand = pygame.transform.rotozoom(pygame.image.load('Game/Char/static1.png').convert_alpha(),0, 6)
character_stand_rect = character_stand.get_rect(center = (1000,500))

obs_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obs_timer,1500)

gravity = 0
difficulty = 12

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and character_rectangle.bottom == 800:
                    gravity = -25
            if event.type == obs_timer:
                obs_rect_list.append(monster1.get_rect(bottomleft = (random.randint(2100,2500),800)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                monster1_rect.left = 2200
                start_time = pygame.time.get_ticks()
                difficulty = 12
                game_active = True
            
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,800))
        screen.blit(ground_surface, (700,800))
        screen.blit(ground_surface, (1400,800))
        monster1_rect.left -= difficulty

        score = display_score()
        obs_rect_list = obs_movement(obs_rect_list)
        
        # if monster1_rect.right < 0:
        #     monster1_rect.left = random.randint(2000,2600)
        #     difficulty += 2
            
        screen.blit(monster1,monster1_rect)
        gravity += 1
        character_rectangle.y += gravity
        if character_rectangle.bottom >= 800:
            character_rectangle.bottom = 800
        screen.blit(character_suface, character_rectangle)

        if monster1_rect.colliderect(character_rectangle):
            game_active = False
    else:
        mm_score = font.render("SCORE: " + str(score), False, 'black')
        mm_score_rect = mm_score.get_rect(center = (1000, 900))
        screen.fill('#2efe77')
        screen.blit(character_stand, character_stand_rect)
        main_menu = font.render("HIT SPACE TO START THE GAME", False, 'black')
        main_menu_rect = main_menu.get_rect(center = (1000, 100))
        screen.blit(main_menu, main_menu_rect)
        screen.blit(mm_score,mm_score_rect)
        
    pygame.display.update()
    clock.tick(60)