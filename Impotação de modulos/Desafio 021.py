# Desafio 21

import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('shots.mp3')
pygame.mixer.music.play()
input('Esta escutando?')
pygame.event.wait()
