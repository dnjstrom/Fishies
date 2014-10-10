#!/usr/bin/python

import sys, pygame
import random

from vector import Vector
from fish import Fish

from pygame.locals import *

pygame.init()

brightBlue = pygame.Color(0, 0, 255)
darkBlue = pygame.Color(0, 0, 180)

def main():
  window = pygame.display.set_mode((300, 300))
  pygame.display.set_caption('Fishies')
  width, height = window.get_size()

  background = pygame.Surface(window.get_size()).convert()
  background.fill(brightBlue)

  water = pygame.Surface(window.get_size()).convert()
  water.fill(darkBlue)
  waterrect = water.get_rect()

  pygame.key.set_repeat(50, 50)

  clock = pygame.time.Clock()

  waterLevel = 1

  fish = Fish()

  running = True

  while running:
    clock.tick(30)

    for event in pygame.event.get(): 
      if event.type == QUIT: 
        sys.exit(0)
      elif event.type == KEYDOWN:
        if event.key == K_UP:
          if waterLevel < 1:
            waterLevel += 0.01
        elif event.key == K_DOWN:
          if waterLevel > 0:
            waterLevel -= 0.01
        else:
          print event

    # Draw background
    window.blit(background, (0,0))

    # Draw waterlevel
    waterrect.height = waterLevel*height
    waterrect.bottom = height
    window.blit(water, waterrect)

    # Draw fish
    fish.update(waterrect)
    window.blit(fish.image, fish.rect.topleft)

    # Actually draw it to the screen
    pygame.display.flip()

  pygame.quit()


if __name__ == "__main__":
  main()