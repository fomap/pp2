import pygame
import os

# Initialize pygame
pygame.init()

# Set up display (not used, but required for initializing mixer)
pygame.display.set_mode((100, 100))

# Set up mixer
pygame.mixer.init()

# Define the music directory
music_dir = "D:\\UNI\\pp2\\lab7\\songs"

# Get a list of all music files in the directory
music_files = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]

# Initialize variables
current_track_index = 0
playing = False

# Load the first track
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))

# Function to play the current track
def play_music():
    global playing
    pygame.mixer.music.play()
    playing = True

# Function to stop the music
def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False

# Function to play the next track
def next_track():
    global current_track_index
    if current_track_index < len(music_files) - 1:
        current_track_index += 1
    else:
        current_track_index = 0
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))
    play_music()

# Function to play the previous track
def previous_track():
    global current_track_index
    if current_track_index > 0:
        current_track_index -= 1
    else:
        current_track_index = len(music_files) - 1
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))
    play_music()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()
            elif event.key == pygame.K_q:
                stop_music()
                running = False

# Quit pygame
pygame.quit()
