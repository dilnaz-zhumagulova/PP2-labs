import pygame
import sys
import os

pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Music Player")

play_img = pygame.image.load("images/play.png").convert_alpha()
stop_img = pygame.image.load("images/stop.png").convert_alpha()
next_img = pygame.image.load("images/next.png").convert_alpha()
prev_img = pygame.image.load("images/prev.png").convert_alpha()

play_button_rect = pygame.Rect(260, 250, 50, 50)
stop_button_rect = pygame.Rect(320, 250, 50, 50)
next_button_rect = pygame.Rect(380, 250, 50, 50)
prev_button_rect = pygame.Rect(200, 250, 50, 50)

music_dir = "music"
music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

if not music_files:
    print("No music files found.")
    pygame.quit()
    sys.exit()

pygame.mixer.init()
i = 0
playing = False
volume = 1.0
pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))

def play_music():
    global playing
    pygame.mixer.music.play()
    playing = True

def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_song():
    global i
    i = (i + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
    play_music()

def prev_song():
    global i
    i = (i - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
    play_music()

while True:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                play_music()
            elif event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()
            elif event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if play_button_rect.collidepoint(pos):
                play_music()
            elif stop_button_rect.collidepoint(pos):
                stop_music()
            elif next_button_rect.collidepoint(pos):
                next_song()
            elif prev_button_rect.collidepoint(pos):
                prev_song()
    
    screen.blit(prev_img, prev_button_rect.topleft)
    screen.blit(play_img if not playing else stop_img, play_button_rect.topleft)
    screen.blit(next_img, next_button_rect.topleft)
    
    pygame.display.flip()