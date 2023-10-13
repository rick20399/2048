# build 2048 in python using pygame!!
import pygame
import container
import helper

pygame.init()

# initial set up
screen = pygame.display.set_mode([container.WIDTH, container.HEIGHT])
pygame.display.set_caption(container.tittle)
timer = pygame.time.Clock()
font = pygame.font.Font(container.font, 24)

# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ''
score = 0
file = open(container.high_score_f, 'r')
init_high = int(file.readline())
file.close()
high_score = init_high

# main game loop
run = True
while run:
    timer.tick(container.fps)
    screen.fill('gray')
    helper.draw_board(score, high_score, screen, font)
    helper.draw_pieces(board_values, screen)
    if spawn_new or init_count < 2:
        board_values, game_over = helper.new_pieces(board_values)
        spawn_new = False
        init_count += 1
    if direction != '':
        board_values, score = helper.take_turn(direction, board_values, score)
        direction = ''
        spawn_new = True
    if game_over:
        helper.draw_over(screen, font)
        if high_score > init_high:
            file = open(container.high_score_f, 'w')
            file.write(f'{high_score}')
            file.close()
            init_high = high_score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

            if game_over:
                if event.key == pygame.K_RETURN:
                    board_values = [[0 for _ in range(4)] for _ in range(4)]
                    spawn_new = True
                    init_count = 0
                    score = 0
                    direction = ''
                    game_over = False

    if score > high_score:
        high_score = score

    pygame.display.flip()
pygame.quit()
