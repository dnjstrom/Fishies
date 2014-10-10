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
    self.step_size = 3

    self.randomize_target()

  @property
  def position(self):
    return Vector(self.rect.left, self.rect.top)

  @position.setter
  def position(self, v):
    self.rect.topleft = (v.x, v.y)

  def set_target(self, x, y):
    self.target = Vector(x, y)

  def randomize_target(self):
    '''
    Randomize a position within window and writes it to target position.
    '''
    length = random.randint(self.min_distance, self.max_distance)
    angle = random.uniform(-self.max_angle, self.max_angle)
    self.target += Vector.make(self.get_direction().angle, length).rotate(angle)

  def get_direction(self):
    return self.target - self.position

  def distance_to_target(self):
    return self.get_direction().length

  def move(self, dx, dy):
    self.position += Vector(dx, dy)

  def update(self, bounds):
    # Check top bound
    if self.rect.top < bounds.top:
      self.rect.top = bounds.top
      self.target = self.position + self.get_direction().flipy()

    # Check right bound
    if self.rect.right > bounds.right:
      self.rect.right = bounds.right
      self.target = self.position + self.get_direction().flipx()

    # Check bottom bound
    if self.rect.bottom > bounds.bottom:
      self.rect.bottom = bounds.bottom
      self.target = self.position + self.get_direction().flipy()

    # Check left bound
    if self.rect.left < bounds.left:
      self.rect.left = bounds.left
      self.target = self.position + self.get_direction().flipx()

    # Choose new target if close enough
    if self.distance_to_target() < self.step_size :
      self.randomize_target()

    # Update position
    target_step = self.get_direction().normalize(self.step_size)
    self.position += target_step


def test_fish():
    fish = Fish();

if __name__ == "__main__":
  # init pygame for test
  pygame.init()
  pygame.display.set_mode((640, 480))
  # run test
  test_fish()