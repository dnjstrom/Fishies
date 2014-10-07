#!/usr/bin/python

import pygame
from random import randint
from vector import Vector

class Fish(pygame.sprite.Sprite):

  def __init__(self):
    self.image = pygame.image.load('img/fish.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.target = None # next position
    self.max_distance = 500 # movement window
    self.min_distance = 0
    self.speed = 10
    self.trueX = 100
    self.trueY = 100

  def set_target(self, target_x, target_y):
    self.target = (target_x, target_y)

  def randomize_target(self):
    '''
    Randomize a position within window and writes it to target position.
    '''
    dx = randint(self.min_distance, self.max_distance)
    dy = randint(self.min_distance, self.max_distance)
    self.target = (dx, dy)

  def get_direction(self, target):
    if self.target: #If we have a target.
      position = Vector(self.rect.centerx, self.rect.centery)
      target = Vector(target[0], target[1])
      self.dist = target - position

      direction = self.dist.normalize()
      return direction

  def distance_check(self, dist):
    '''
      Function:
        tests if the total distance from the
        sprite to the target is smaller than the
        ammount of distance that would be normal
        for the sprite to travel
        (this lets the sprite know if it needs
        to slow down. we want it to slow
        down before it gets to it's target)
      Returns:
        bool
      Parameters:
        - self
        - dist
          this is the total distance from the
          sprite to the target
          can be any x,y value pair in
          brackets [x,y]
          or parentheses (x,y)
    ''' 
    dist_x = dist[0] ** 2 #gets absolut value of the x distance
    dist_y = dist[1] ** 2
    t_dist = dist_x + dist_y
    speed = self.speed ** 2

    if t_dist < (speed):
      return True

  def update(self):
    self.dir = self.get_direction(self.target)
    if self.dir:
      
      if self.distance_check(self.dist):
        self.rect.center = self.target #center the sprite on the target

      else:
        self.trueX += (self.dir[0] * self.speed)
        self.trueY += (self.dir[1] * self.speed)
        self.rect.center = (round(self.trueX), round(self.trueY))



def test_fish():
    fish = Fish();

if __name__ == "__main__":
  # init pygame for test
  pygame.init()
  pygame.display.set_mode((640, 480))
  # run test
  test_fish()