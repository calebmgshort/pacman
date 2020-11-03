import pygame
import constants
import public_vars
import objects
import init
import time
from ghost_algorithms import *

# Initialize pygame
pygame.init()
# Initialize text
pygame.font.init()

# Create the screen
public_vars.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

# Title
pygame.display.set_caption("Pacman")

def should_super_points_blink() -> bool: 
    current_time = time.time()
    time_dif = current_time - public_vars.start_time
    time_dif %= 2.0
    return time_dif < 1

def resume_play_mode():
    public_vars.start_time = time.time()
    public_vars.game_mode = constants.GameMode.PLAY

def restart_play_mode():
    init.initialize_game_data()
    resume_play_mode()    

def win_mode():
    public_vars.screen.fill(constants.BLACK)
    title_font = pygame.font.Font('freesansbold.ttf', 40)
    title_surface = title_font.render('You Win! What a champion!', False, constants.GREEN)
    title_rect = title_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3))
    public_vars.screen.blit(title_surface, title_rect)
    score_surface = title_font.render('Score: {}'.format(public_vars.score), False, constants.GREEN)
    score_rect = title_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3 + 40))
    public_vars.screen.blit(score_surface, score_rect)
    subtitle_font = pygame.font.Font('freesansbold.ttf', 20)
    subtitle_surface = subtitle_font.render('press spacebar to play again, or q to return to the homescreen', False, constants.GREEN)
    subtitle_rect = subtitle_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3 + 80))
    public_vars.screen.blit(subtitle_surface, subtitle_rect)
    pygame.display.update()
    while True:
        switch_to_play_mode = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    switch_to_play_mode = True
                if event.key == pygame.K_q:
                    public_vars.game_mode = constants.GameMode.HOME_SCREEN
                    return
        if switch_to_play_mode:
            restart_play_mode()
            return 

def game_over_mode():
    public_vars.screen.fill(constants.BLACK)
    title_font = pygame.font.Font('freesansbold.ttf', 40)
    title_surface = title_font.render('GAME OVER!', False, constants.RED)
    title_rect = title_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3))
    public_vars.screen.blit(title_surface, title_rect)
    score_surface = title_font.render('Score: {}'.format(public_vars.score), False, constants.RED)
    score_rect = title_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3 + 40))
    public_vars.screen.blit(score_surface, score_rect)
    subtitle_font = pygame.font.Font('freesansbold.ttf', 20)
    subtitle_surface = subtitle_font.render('press spacebar to play again, or q to return to the homescreen', False, constants.RED)
    subtitle_rect = subtitle_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3 + 80))
    public_vars.screen.blit(subtitle_surface, subtitle_rect)
    pygame.display.update()
    while True:
        switch_to_play_mode = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    switch_to_play_mode = True
                if event.key == pygame.K_q:
                    public_vars.game_mode = constants.GameMode.HOME_SCREEN
                    return
        if switch_to_play_mode:
            restart_play_mode()
            return 

def pause_mode():
    pause_button = pygame.Rect(0, 0, 300, 150)
    pause_button.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    font = pygame.font.SysFont('freesansbold.ttf', 30)
    text_surface = font.render('Game Paused', False, constants.WHITE)
    text_rect = text_surface.get_rect(center=pause_button.center)
    subfont = pygame.font.SysFont('freesansbold.ttf', 15)
    subtext_surface = subfont.render("press spacebar or 'p' to resume", False, constants.WHITE)
    subtext_rect = text_surface.get_rect(center=(pause_button.center[0], pause_button.center[1]+30))
    pygame.draw.rect(public_vars.screen, DARK_GRAY, pause_button)
    public_vars.screen.blit(text_surface, text_rect) 
    public_vars.screen.blit(subtext_surface, subtext_rect) 
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    public_vars.game_mode = constants.GameMode.PLAY
                    return 
                elif event.key == pygame.K_q:
                    # TODO: diplay a "are you sure you want to quit" button
                    public_vars.game_mode = constants.GameMode.HOME_SCREEN
                    return  

def play_mode():
    font = pygame.font.Font('freesansbold.ttf', 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    public_vars.pacman.desired_direction = constants.Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    public_vars.pacman.desired_direction = constants.Direction.RIGHT
                elif event.key == pygame.K_UP:
                    public_vars.pacman.desired_direction = constants.Direction.UP
                elif event.key == pygame.K_DOWN:
                    public_vars.pacman.desired_direction = constants.Direction.DOWN
                elif event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    public_vars.game_mode = constants.GameMode.PAUSE
                    pause_mode()
                    if public_vars.game_mode != constants.GameMode.PLAY:
                        return
                elif event.key == pygame.K_q:
                    # TODO: diplay a "are you sure you want to quit" button
                    public_vars.game_mode = constants.GameMode.HOME_SCREEN
                    return 
        public_vars.pacman.move()
        for point in public_vars.points:
            if(public_vars.pacman.collides(point)):
                public_vars.score += 10
                public_vars.points.remove(point)
        for super_point in public_vars.super_points:
            if(public_vars.pacman.collides(super_point)):
                public_vars.score += 40
                public_vars.super_points.remove(super_point)
                for ghost in public_vars.ghosts:
                    ghost.mode = constants.GhostMode.SCARED
        for ghost in public_vars.ghosts:
            ghost.move()
        for ghost in public_vars.ghosts:
            if public_vars.pacman.collides(ghost):
                if ghost.mode == constants.GhostMode.SCARED:
                    public_vars.score += 100
                    ghost.mode = constants.GhostMode.RESPAWN
                elif ghost.mode == constants.GhostMode.RESPAWN:
                    pass
                else:
                    public_vars.game_mode = constants.GameMode.GAME_OVER
                    return
            if ghost.in_center():
                ghost.mode = constants.GhostMode.NORMAL
        if len(public_vars.points) == 0:
            public_vars.game_mode = constants.GameMode.WIN
            return
        public_vars.screen.fill(constants.BLACK)
        public_vars.pacman.render()
        for point in public_vars.points:
            point.render()
        if should_super_points_blink():
            for super_point in public_vars.super_points:
                super_point.render()
        for ghost in public_vars.ghosts:
            ghost.render()
        for wall in public_vars.walls:
            wall.render()
        textsurface = font.render('Score: {}'.format(public_vars.score), True, constants.WHITE)
        public_vars.screen.blit(textsurface, (constants.SCREEN_WIDTH/2,0))
        pygame.display.update()

def home_screen_mode():
    public_vars.screen.fill(constants.BLACK)
    title_font = pygame.font.Font('freesansbold.ttf', 40)
    title_surface = title_font.render('Welcome to Pacman!', False, constants.YELLOW)
    title_rect = title_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3))
    public_vars.screen.blit(title_surface, title_rect)
    subtitle_font = pygame.font.Font('freesansbold.ttf', 20)
    subtitle_surface = subtitle_font.render('(press spacebar or click anywhere to play)', False, constants.YELLOW)
    subtitle_rect = subtitle_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3 + 40))
    public_vars.screen.blit(subtitle_surface, subtitle_rect)
    pygame.display.update()
    while True:
        switch_to_play_mode = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    switch_to_play_mode = True
            if pygame.mouse.get_pressed()[0]:
                switch_to_play_mode = True
        if switch_to_play_mode:
            restart_play_mode()
            return 

# Game loop
public_vars.game_mode = constants.GameMode.HOME_SCREEN
while True:
    if public_vars.game_mode == constants.GameMode.HOME_SCREEN:
        home_screen_mode()
    elif public_vars.game_mode == constants.GameMode.PLAY:
        play_mode()
    elif public_vars.game_mode == constants.GameMode.WIN:
        win_mode()
    elif public_vars.game_mode == constants.GameMode.GAME_OVER:
        game_over_mode()
    elif public_vars.game_mode == constants.GameMode.CLOSE_WINDOW:
        break
    else:
        raise ValueError("The game mode is invalid")    
