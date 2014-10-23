#!/usr/bin/python

"""
This program displays an aquarium visualization with moving fishes.

You start the program on the command line by: "pyghon fishies.py" or
simply "./fishies.py".
"""

import sys, pygame
import random

import time
import serial

from vector import Vector
from fish import Fish

from pygame.locals import *

from pdb import set_trace


pygame.init()

black = pygame.Color(0, 0, 0)
darkBlue = pygame.Color(0, 0, 180)

increment = 0.001
delay = 1000

def main():
  # Listen to arduino
  try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.001) 
  except Exception, e:
    print "Unable to open serial port!"
    ser = None

  window_size = pygame.display.list_modes()[0]
  print "Window size: %sx%s" % window_size
  window = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
  pygame.display.set_caption('Fishies')
  width, height = window_size

  background = pygame.Surface(window.get_size()).convert()
  background.fill(black)

  water = pygame.Surface(window.get_size()).convert()
  water.fill(darkBlue)
  waterrect = water.get_rect()

  pygame.key.set_repeat(25, 25)

  clock = pygame.time.Clock()

  waterlevel = 1
  waterwidth = 0.3

  fishies = []

  for x in xrange(1,35):
    fishies.append(Fish())

  running = True

  latest_message = 0

  while running:
    clock.tick(30)
    millis = int(round(time.time() * 1000))

    if ser is not None:
      for line in ser:
        waterlevel -= increment
        latest_message = millis

    if waterlevel < 1 and latest_message < millis - delay:
      waterlevel += increment

    for event in pygame.event.get(): 
      if event.type == QUIT: 
        sys.exit(0)
      elif event.type == KEYDOWN:
        if event.key == K_UP:
          waterlevel += increment*10
          latest_message = millis
        elif event.key == K_DOWN:
          waterlevel -= increment*10
          latest_message = millis
        elif event.key == K_LEFT:
          waterwidth -= increment
        elif event.key == K_RIGHT:
          waterwidth += increment
        elif event.key == K_ESCAPE:
          running = False
        elif event.key == K_SPACE:
          set_trace()
        else:
          print event


    if waterlevel > 1:
      waterlevel = 1
    elif waterlevel < 0:
      waterlevel = 0


    # Draw background
    window.blit(background, (0,0))

    # Draw waterlevel
    waterrect.height = waterlevel*height
    if waterrect.height < fishies[0].rect.height:
      waterrect.height = fishies[0].rect.height
      for fish in fishies:
        fish.dead = True
    else:
      for fish in fishies:
        fish.dead = False

    waterrect.bottom = height
    waterrect.width = width * waterwidth
    bgmod = pygame.transform.scale(water, (waterrect.width,waterrect.height))


    # Draw fish
    for fish in fishies:
      fish.update(waterrect)
      pos = fish.rect.copy()
      pos.left -= waterrect.left
      pos.top -= waterrect.top
      bgmod.blit(fish.image, pos.topleft)

    window.blit(bgmod, waterrect)

    # Actually draw it to the screen
    pygame.display.flip()

  pygame.quit()


if __name__ == "__main__":
  main()