import pygame
import constants
import public_vars
from objects import *
import init
import time
import threading 

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
    time_dif = current_time - public_vars.render_start_time
    time_dif %= 2.0
    return time_dif < 1

def restart_play_mode(play_mode: constants.GameMode):
    if play_mode == constants.GameMode.SINGLE_PLAY:
        init.initialize_single_game_data()
        public_vars.game_mode = constants.GameMode.SINGLE_PLAY
    elif play_mode == constants.GameMode.MULTI_PLAY:
        init.initialize_multi_game_data()
        public_vars.game_mode = constants.GameMode.MULTI_PLAY
    else:
        raise ValueError("Game mode in valid")

def end_game_loop(play_mode: constants.GameMode):
    switch_to_play_mode = False
    while True:
        time.sleep(0.020)
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
            restart_play_mode(play_mode)
            return 

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
    end_game_loop(constants.GameMode.SINGLE_PLAY)

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
    end_game_loop(constants.GameMode.SINGLE_PLAY)

def multi_end_mode():
    public_vars.screen.fill(constants.BLACK)
    title_font = pygame.font.Font('freesansbold.ttf', 40)
    main_text = "Player 1 wins!"
    if len(public_vars.p1_pacmen) == 0:
        main_text = "Player 2 wins!"
    title_surface = title_font.render(main_text, False, constants.YELLOW)
    title_rect = title_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3))
    public_vars.screen.blit(title_surface, title_rect)
    subtitle_font = pygame.font.Font('freesansbold.ttf', 20)
    subtitle_surface = subtitle_font.render('press spacebar to play again, or q to return to the homescreen', False, constants.YELLOW)
    subtitle_rect = subtitle_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3 + 40))
    public_vars.screen.blit(subtitle_surface, subtitle_rect)
    pygame.display.update()
    end_game_loop(constants.GameMode.MULTI_PLAY)

def pause_mode(play_mode: constants.GameMode):
    pause_button = pygame.Rect(0, 0, 300, 150)
    pause_button.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) 
    font = pygame.font.Font('freesansbold.ttf', 30)
    text_surface = font.render('Game Paused', False, constants.WHITE)
    text_rect = text_surface.get_rect(center=pause_button.center)
    subfont = pygame.font.Font('freesansbold.ttf', 15)
    subtext_surface = subfont.render("press spacebar or 'p' to resume", False, constants.WHITE)
    subtext_rect = text_surface.get_rect(center=(pause_button.center[0], pause_button.center[1]+30))
    subtext_surface2 = subfont.render("or 'q' to return to the homescreen", False, constants.WHITE)
    subtext_rect2 = text_surface.get_rect(center=(pause_button.center[0], pause_button.center[1]+50))
    pygame.draw.rect(public_vars.screen, constants.DARK_GRAY, pause_button)
    public_vars.screen.blit(text_surface, text_rect) 
    public_vars.screen.blit(subtext_surface, subtext_rect) 
    public_vars.screen.blit(subtext_surface2, subtext_rect2) 
    pygame.display.update()
    while True:
        time.sleep(0.020)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    public_vars.game_mode = play_mode
                    return 
                elif event.key == pygame.K_q:
                    public_vars.game_mode = constants.GameMode.HOME_SCREEN
                    return  

def calculate_and_switch_ghost_mode(ghost: Ghost, start_scared_mode_time: float, total_pause_mode_time: float):
    if ghost.mode != Ghost.GhostMode.SCARED:
        return
    total_scared_time = time.time() - start_scared_mode_time - total_pause_mode_time
    if total_scared_time > 10: 
        ghost.set_submode(Ghost.GhostSubmode.NORMAL)
        ghost.mode = Ghost.GhostMode.NORMAL
        return
    if total_scared_time > 7:
        ghost.set_submode(Ghost.GhostSubmode.ABOUT_TO_SWITCH)

class StopThread:
    def __init__(self):
        self.should_stop = False

def play_mode_render(stop_render: StopThread):
    score_font = pygame.font.Font('freesansbold.ttf', 30)
    info_font = pygame.font.Font('freesansbold.ttf', 15)
    info_textsurface = info_font.render("Press spacebar or 'p' to pause, or 'q' to return to the homescreen", True, constants.WHITE)
    while True:
        time.sleep(0.020)
        if stop_render.should_stop:
            return
        if public_vars.game_mode != constants.GameMode.SINGLE_PLAY and public_vars.game_mode != constants.GameMode.MULTI_PLAY:
            continue
        public_vars.screen.fill(constants.BLACK)

        if public_vars.game_mode == constants.GameMode.MULTI_PLAY:
            for pacman in public_vars.p1_pacmen:
                pacman.render(public_vars.p1_scared)
            for pacman in public_vars.p2_pacmen:
                pacman.render(not public_vars.p1_scared)
        if public_vars.game_mode == constants.GameMode.SINGLE_PLAY:
            public_vars.pacman.render(None)
            for point in public_vars.points:
                point.render()
            if should_super_points_blink():
                for super_point in public_vars.super_points:
                    super_point.render()
            for ghost in public_vars.ghosts:
                ghost.render()
            score_textsurface = score_font.render('Score: {}'.format(public_vars.score), True, constants.WHITE)
            public_vars.screen.blit(score_textsurface, (constants.SCREEN_WIDTH/2,0))

        for wall in public_vars.walls:
            wall.render()
        public_vars.screen.blit(info_textsurface, (constants.WALL_LONGITUDE_1, constants.WALL_LATITUDE_11+constants.THIN_WALL_THICKNESS))
        pygame.display.update()

def stop_thread(thread: threading.Thread, thread_stopper: StopThread):
    thread_stopper.should_stop = True
    thread.join()

def play_mode(play_mode: constants.GameMode):
    stop_render = StopThread()
    play_mode_render_thread = threading.Thread(target=play_mode_render, args=(stop_render,)) 
    play_mode_render_thread.start()
    public_vars.render_start_time = time.time()
    total_pause_mode_time = 0
    start_scared_mode_time = None
    # Play initial sound
    mixer = pygame.mixer
    beginning_sound = mixer.Sound('resources/sounds/pacman_beginning.wav')
    beginning_sound_channel = beginning_sound.play()
    while(beginning_sound_channel.get_busy()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                stop_thread(play_mode_render_thread, stop_render)
                return
    chomp_sound = mixer.Sound('resources/sounds/pacman_chomp_short.wav')
    chomp_sound_channel = pygame.mixer.Channel(0)
    eat_ghost_sound = mixer.Sound('resources/sounds/pacman_eatghost.wav')
    eat_ghost_sound_channel = pygame.mixer.Channel(1)
    sound_channels = [chomp_sound_channel, eat_ghost_sound_channel]
    # Start loop
    while True:
        # Sleep so everything doesn't happen too fast
        time.sleep(0.0005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                stop_thread(play_mode_render_thread, stop_render)
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    for sound_channel in sound_channels:
                        sound_channel.pause()
                    public_vars.game_mode = constants.GameMode.PAUSE
                    last_pause_mode = time.time()
                    pause_mode(play_mode)
                    pause_mode_time = time.time() - last_pause_mode
                    total_pause_mode_time += pause_mode_time
                    if public_vars.game_mode != constants.GameMode.SINGLE_PLAY and public_vars.game_mode != constants.GameMode.MULTI_PLAY:
                        stop_thread(play_mode_render_thread, stop_render)
                        return
                    for sound_channel in sound_channels:
                        sound_channel.unpause()
                if event.key == pygame.K_q:
                    public_vars.game_mode = constants.GameMode.HOME_SCREEN
                    stop_thread(play_mode_render_thread, stop_render)
                    return
                if play_mode == constants.GameMode.SINGLE_PLAY:
                    if event.key == pygame.K_LEFT:
                        public_vars.pacman.desired_direction = constants.Direction.LEFT
                    if event.key == pygame.K_RIGHT:
                        public_vars.pacman.desired_direction = constants.Direction.RIGHT
                    if event.key == pygame.K_UP:
                        public_vars.pacman.desired_direction = constants.Direction.UP
                    if event.key == pygame.K_DOWN:
                        public_vars.pacman.desired_direction = constants.Direction.DOWN
                if play_mode == constants.GameMode.MULTI_PLAY:
                    if event.key == pygame.K_LEFT:
                        for pacman in public_vars.p1_pacmen:
                            pacman.desired_direction = constants.Direction.LEFT
                    if event.key == pygame.K_RIGHT:
                        for pacman in public_vars.p1_pacmen:
                            pacman.desired_direction = constants.Direction.RIGHT
                    if event.key == pygame.K_UP:
                        for pacman in public_vars.p1_pacmen:
                            pacman.desired_direction = constants.Direction.UP
                    if event.key == pygame.K_DOWN:
                        for pacman in public_vars.p1_pacmen:
                            pacman.desired_direction = constants.Direction.DOWN
                    if event.key == pygame.K_a:
                        for pacman in public_vars.p2_pacmen:
                            pacman.desired_direction = constants.Direction.LEFT
                    if event.key == pygame.K_d:
                        for pacman in public_vars.p2_pacmen:
                            pacman.desired_direction = constants.Direction.RIGHT
                    if event.key == pygame.K_w:
                        for pacman in public_vars.p2_pacmen:
                            pacman.desired_direction = constants.Direction.UP
                    if event.key == pygame.K_s:
                        for pacman in public_vars.p2_pacmen:
                            pacman.desired_direction = constants.Direction.DOWN
        
        if play_mode == constants.GameMode.MULTI_PLAY:
            for pacman in public_vars.p1_pacmen:
                pacman.move()
            for pacman in public_vars.p2_pacmen:
                pacman.move()
            for p1_pacman in public_vars.p1_pacmen[:]:
                for p2_pacman in public_vars.p2_pacmen[:]:
                    if p1_pacman.collides(p2_pacman):
                        if public_vars.p1_scared:
                            public_vars.p1_pacmen.remove(p1_pacman)
                        else:
                            public_vars.p2_pacmen.remove(p2_pacman)
            if len(public_vars.p1_pacmen) == 0 or len(public_vars.p2_pacmen) == 0:
                stop_thread(play_mode_render_thread, stop_render)
                public_vars.game_mode = constants.GameMode.MULTI_END
                return

        if play_mode == constants.GameMode.SINGLE_PLAY:
            public_vars.pacman.move()
            for point in public_vars.points:
                if(public_vars.pacman.collides(point)):
                    public_vars.score += 10
                    public_vars.points.remove(point)
                    if chomp_sound_channel.get_busy():
                        chomp_sound_channel.queue(chomp_sound)
                    else:
                        chomp_sound_channel.play(chomp_sound)    
            for super_point in public_vars.super_points:
                if(public_vars.pacman.collides(super_point)):
                    public_vars.score += 40
                    public_vars.super_points.remove(super_point)
                    for ghost in public_vars.ghosts:
                        ghost.mode = Ghost.GhostMode.SCARED
                    total_pause_mode_time = 0
                    start_scared_mode_time = time.time()
            for ghost in public_vars.ghosts:
                ghost.move()
                calculate_and_switch_ghost_mode(ghost, start_scared_mode_time, total_pause_mode_time)
                if public_vars.pacman.collides(ghost):
                    if ghost.mode == Ghost.GhostMode.SCARED:
                        public_vars.score += 100
                        ghost.mode = Ghost.GhostMode.RESPAWN
                        if eat_ghost_sound_channel.get_busy():
                            eat_ghost_sound_channel.stop()
                        eat_ghost_sound_channel.play(eat_ghost_sound)    
                    elif ghost.mode == Ghost.GhostMode.RESPAWN:
                        pass
                    else:
                        stop_thread(play_mode_render_thread, stop_render)
                        death_sound = mixer.Sound('resources/sounds/pacman_death.wav')
                        death_sound_channel = death_sound.play()
                        while(death_sound_channel.get_busy()):
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                                    stop_thread(play_mode_render_thread, stop_render)
                                    return
                        public_vars.game_mode = constants.GameMode.GAME_OVER
                        return
                if ghost.in_center():
                    ghost.mode = Ghost.GhostMode.NORMAL
            if len(public_vars.points) == 0:
                public_vars.game_mode = constants.GameMode.WIN
                stop_thread(play_mode_render_thread, stop_render)
                return

def home_screen_mode():
    public_vars.screen.fill(constants.BLACK)
    title_font = pygame.font.Font('freesansbold.ttf', 40)
    title_surface = title_font.render('Welcome to Pacman!', False, constants.YELLOW)
    title_rect = title_surface.get_rect(center=(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/3))
    public_vars.screen.blit(title_surface, title_rect)

    button_font = pygame.font.Font('freesansbold.ttf', 30)
    single_button = pygame.Rect(0, 0, 250, 150)
    single_button.center = (constants.SCREEN_WIDTH/4, constants.SCREEN_HEIGHT/2) 
    single_surface = button_font.render('Single Player', False, constants.BLACK)
    single_rect = single_surface.get_rect(center=single_button.center)
    pygame.draw.rect(public_vars.screen, constants.GREEN, single_button)
    public_vars.screen.blit(single_surface, single_rect) 

    multi_button = pygame.Rect(0, 0, 250, 150)
    multi_button.center = (constants.SCREEN_WIDTH*3/4, constants.SCREEN_HEIGHT/2) 
    multi_surface = button_font.render('Multi Player', False, constants.BLACK)
    multi_rect = multi_surface.get_rect(center=multi_button.center)
    pygame.draw.rect(public_vars.screen, constants.RED, multi_button)
    public_vars.screen.blit(multi_surface, multi_rect) 

    pygame.display.update()
    while True:
        time.sleep(0.020)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                public_vars.game_mode = constants.GameMode.CLOSE_WINDOW
                return
            if pygame.mouse.get_pressed()[0]:
                mouse_coordinates = pygame.mouse.get_pos()
                if single_button.collidepoint(mouse_coordinates):
                    restart_play_mode(constants.GameMode.SINGLE_PLAY)
                    return
                if multi_button.collidepoint(mouse_coordinates):
                    restart_play_mode(constants.GameMode.MULTI_PLAY)
                    return

# Game loop
public_vars.game_mode = constants.GameMode.HOME_SCREEN
while True:
    if public_vars.game_mode == constants.GameMode.HOME_SCREEN:
        home_screen_mode()
    elif public_vars.game_mode == constants.GameMode.SINGLE_PLAY:
        play_mode(constants.GameMode.SINGLE_PLAY)
    elif public_vars.game_mode == constants.GameMode.MULTI_PLAY:
        play_mode(constants.GameMode.MULTI_PLAY)
    elif public_vars.game_mode == constants.GameMode.MULTI_END:
        multi_end_mode()
    elif public_vars.game_mode == constants.GameMode.WIN:
        win_mode()
    elif public_vars.game_mode == constants.GameMode.GAME_OVER:
        game_over_mode()
    elif public_vars.game_mode == constants.GameMode.CLOSE_WINDOW:
        break
    else:
        raise ValueError("The game mode is invalid")    
