import pygame
import time
import random
pygame.init()
white = (255, 255, 255)
background = (17, 24, 39)
grid_color = (28, 38, 55)
panel_color = (31, 41, 59)
snake_head_color = (134, 239, 172)
snake_body_color = (34, 197, 94)
food_color = (251, 113, 133)
border_color = (71, 85, 105)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
small_font = pygame.font.SysFont("bahnschrift", 18)
title_font = pygame.font.SysFont("bahnschrift", 36, bold=True)


def draw_background():
    dis.fill(background)
    for x in range(0, dis_width, 20):
        pygame.draw.line(dis, grid_color, (x, 0), (x, dis_height))
    for y in range(0, dis_height, 20):
        pygame.draw.line(dis, grid_color, (0, y), (dis_width, y))
    pygame.draw.rect(dis, border_color, [
                     1, 1, dis_width - 2, dis_height - 2], 2)


def display_score(score):
    pygame.draw.rect(dis, panel_color, [12, 12, 194, 42], border_radius=10)
    label = small_font.render("SCORE", True, (148, 163, 184))
    value = font_style.render(str(score), True, white)
    dis.blit(label, [24, 21])
    dis.blit(value, [112, 17])
    pygame.draw.circle(dis, (250, 204, 21), (181, 33), 12)
    pygame.draw.circle(dis, (31, 41, 59), (177, 30), 1)
    pygame.draw.circle(dis, (31, 41, 59), (185, 30), 1)
    pygame.draw.arc(dis, (31, 41, 59), [176, 31, 10, 8], 3.14, 6.28, 2)


def draw_food(foodx, foody):
    center = (int(foodx + snake_block / 2), int(foody + snake_block / 2))
    pygame.draw.circle(dis, (136, 55, 75), center, 8)
    pygame.draw.circle(dis, food_color, center, 5)
    pygame.draw.circle(dis, (255, 210, 218), (center[0] - 1, center[1] - 2), 1)


def draw_snake(snake_block, snake_list):
    for index, segment in enumerate(snake_list):
        color = snake_head_color if index == len(
            snake_list) - 1 else snake_body_color
        pygame.draw.rect(
            dis,
            color,
            [int(segment[0]), int(segment[1]), snake_block, snake_block],
            border_radius=3,
        )


def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close:
            draw_background()
            pygame.draw.rect(dis, panel_color, [
                             120, 190, 560, 210], border_radius=18)
            message = title_font.render("Game Over", True, food_color)
            dis.blit(message, message.get_rect(center=(dis_width / 2, 245)))
            hint = small_font.render(
                "Press C to play again  |  Q to quit", True, white)
            dis.blit(hint, hint.get_rect(center=(dis_width / 2, 300)))
            display_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        direction_changed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_LEFT
                    and not direction_changed
                    and x1_change != snake_block
                ):
                    x1_change = -snake_block
                    y1_change = 0
                    direction_changed = True
                elif (
                    event.key == pygame.K_RIGHT
                    and not direction_changed
                    and x1_change != -snake_block
                ):
                    x1_change = snake_block
                    y1_change = 0
                    direction_changed = True
                elif (
                    event.key == pygame.K_UP
                    and not direction_changed
                    and y1_change != snake_block
                ):
                    y1_change = -snake_block
                    x1_change = 0
                    direction_changed = True
                elif (
                    event.key == pygame.K_DOWN
                    and not direction_changed
                    and y1_change != -snake_block
                ):
                    y1_change = snake_block
                    x1_change = 0
                    direction_changed = True
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        draw_background()
        draw_food(foodx, foody)
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
