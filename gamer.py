import pygame
import sys


##8008153

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

###um yes
while True:


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  screen.fill((225, 0, 0)) ### Screen is actually Red
  pygame.display.update()

###Gamer Moments
