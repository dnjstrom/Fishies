#!/usr/bin/python

import pygame
from random import randint

class Fish(pygame.sprite.Sprite):

  def __init__(self):
    self.image = pygame.image.load('img/fish.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.target = None
    self.max_distance = 100
    
    self.randomize_target()

  def set_target(self, target_x, target_y):
    self.target_x = target_x
    self.target_y = target_y

  def randomize_target(self):
    dx = randint(-self.max_distance, self.max_distance)
    dy = randint(-self.max_distance, self.max_distance)
    self.rect.topleft = (dx, dy)



def test_fish():
    fish = Fish();

if __name__ == "__main__":
  # init pygame for test
  pygame.init()
  pygame.display.set_mode((640, 480))
  # run test
  test_fish()