#!/usr/bin/python

import sys, pygame
import time

from vector import Vector
from fish import Fish

from pygame.locals import *

pygame.init()

brightBlue = pygame.Color(0, 0, 255)
darkBlue = pygame.Color(0, 0, 180)

def main():
  window = pygame.display.set_mode((700, 700))
  pygame.display.set_caption('Fishies')
  width, height = window.get_size()

  background = pygame.Surface(window.get_size()).convert()
  background.fill(brightBlue)

  pygame.key.set_repeat(50, 50)

  clock = pygame.time.Clock()

  waterLevel = 0

  fish = Fish()


  running = True
  timer = 60

  while running:
    clock.tick(30)
    timer -= 1

    if timer <= 0:
      fish.randomize_target()
      timer = 60


    for event in pygame.event.get(): 
      if event.type == QUIT: 
        sys.exit(0)
      elif event.type == KEYDOWN:
        if event.key == K_UP:
          if waterLevel > 0:
            waterLevel -= 0.01
        elif event.key == K_DOWN:
          if waterLevel < 1:
            waterLevel += 0.01
        elif event.key == K_SPACE:
          fish.randomize_target()
        else:
          print event

    # Draw background
    fish.update()
    window.blit(background, (0,0))

    # Draw waterlevel
    pygame.draw.rect(window, darkBlue, (0, (waterLevel*height), width, height))

    # Draw fish
    window.blit(fish.image, fish.rect.topleft)

    # Actually draw it to the screen
    pygame.display.flip()

  pygame.quit()


if __name__ == "__main__":
  main()