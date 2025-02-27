import pygame
import random

def display_score():
    current_score = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = font.render(f'{current_score}',False, 'black')
    score_rect = score_surf.get_rect(center = (500, 50))
    screen.blit(score_surf,score_rect)
    return current_score

pygame.init()
screen = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()
pygame.display.set_caption("JUMPER")
font = pygame.font.Font('Jumper\Game\Font\Font.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('Jumper\Game\sky\sky.jpg').convert_alpha()
ground_surface = pygame.image.load('Jumper\Game\Ground\Aground.webp').convert_alpha()

monster1 = pygame.image.load('Jumper\Game\obs\monster1.png').convert_alpha()
monster1_rect = monster1.get_rect(topleft = (1000,265))

character_suface = pygame.image.load('Jumper\Game\Char\smash-straight1.png').convert_alpha()
character_rectangle = character_suface.get_rect(midbottom = (100, 300))

character_stand = pygame.transform.rotozoom(pygame.image.load('Jumper\Game\Char\static1.png').convert_alpha(),0, 3)
character_stand_rect = character_stand.get_rect(center = (500,250))



gravity = 0
difficulty = 6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and character_rectangle.bottom == 300:
                    gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                monster1_rect.left = 1100
                start_time = pygame.time.get_ticks()
                difficulty = 6
                game_active = True
            
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        screen.blit(ground_surface, (600,300))
        monster1_rect.left -= difficulty
        score = display_score()
        
        if monster1_rect.right < 0:
            monster1_rect.left = random.randint(1000,1300)
            difficulty += 1
            
        screen.blit(monster1,monster1_rect)
        gravity += 1
        character_rectangle.y += gravity
        if character_rectangle.bottom >= 300:
            character_rectangle.bottom = 300
        screen.blit(character_suface, character_rectangle)

        if monster1_rect.colliderect(character_rectangle):
            game_active = False
    else:
        mm_score = font.render("SCORE: " + str(score), False, 'black')
        mm_score_rect = mm_score.get_rect(center = (500, 450))
        screen.fill('#2efe77')
        screen.blit(character_stand, character_stand_rect)
        main_menu = font.render("HIT SPACE TO START THE GAME", False, 'black')
        main_menu_rect = main_menu.get_rect(center = (500, 50))
        screen.blit(main_menu, main_menu_rect)
        screen.blit(mm_score,mm_score_rect)
        
    pygame.display.update()
    clock.tick(60)