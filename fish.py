#!/usr/bin/python

import pygame
import math
import random

from vector import Vector

# debug
from pdb import set_trace

class Fish(pygame.sprite.Sprite):

  def __init__(self):
    self.image = pygame.image.load('img/fish.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.target = Vector(0,0)
    self.max_distance = 200
    self.min_distance = 50
    self.max_angle = math.pi/4
    self.speed = 3
    
    self.randomize_target()

  @property
  def position(self):
    return Vector(self.rect.centerx, self.rect.centery)

  @position.setter
  def position(self, v):
    self.rect.center = (v.x, v.y)

  def set_target(self, x, y):
    self.target = Vector(x, y)

  def get_position(self):
    return Vector(self.rect.centerx, self.rect.centery)

  def randomize_target(self):
    '''
    Randomize a position within window and writes it to target position.
    '''
    length = random.randint(self.min_distance, self.max_distance)
    angle = random.uniform(-self.max_angle, self.max_angle)
    self.target += Vector.make(self.target.angle(), length).rotate(angle)

  def get_direction(self, target):
    position = Vector(self.rect.centerx, self.rect.centery)
    dist = target - position
    return dist.normalize()

  def distance_to_target(self):
    return (self.target - self.get_position()).length()

  def move(self, dx, dy):
    self.position += Vector(dx, dy)

  def update(self):
    self.dir = self.get_direction(self.target)
    if self.dir:
      if self.distance_to_target() < self.speed:
        self.position = self.target
        self.randomize_target()
      else:
        dx = (self.dir[0] * self.speed)
        dy = (self.dir[1] * self.speed)
        self.move(dx, dy)


def test_fish():
    fish = Fish();

if __name__ == "__main__":
  # init pygame for test
  pygame.init()
  pygame.display.set_mode((640, 480))
  # run test
  test_fish()