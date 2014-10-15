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
    self.direction = Vector(3,1)
    self.position = Vector(0, 0)
    self.MAX_ANGLE = math.pi/8
    self.step_size = 10

    self.randomize_direction()

  def set_direction(self, x, y):
    self.direction = Vector(x, y)

  def randomize_direction(self):
    '''
    Randomize a position within window and writes it to direction position.
    '''
    component_y = random.uniform(-self.MAX_ANGLE, self.MAX_ANGLE)
    self.direction = self.direction.set_y(component_y).normalize()

  def move(self, dx, dy):
    self.position += Vector(dx, dy)

  def update(self, bounds):
    # Check top bound
    if self.rect.top < bounds.top:
      self.position = self.position.set_y(bounds.top)
      self.direction = self.direction.set_y(abs(self.direction.y))

      #self.direction = self.direction.rotate(random.uniform(-self.MAX_ANGLE, self.MAX_ANGLE))

    # Check right bound
    if self.rect.left > bounds.right:
      self.position = self.position.set_x(bounds.right)
      self.direction = self.direction.flipx()
      self.randomize_direction()
      self.position = self.position.set_y(random.randint(bounds.top, bounds.bottom - self.rect.height))
      self.position = self.position.set_x(random.choice([0-self.rect.width, bounds.right]))
      self.speed = random.randint(2, 5)


    # Check bottom bound
    if self.rect.bottom > bounds.bottom:
      self.position = self.position.set_y(bounds.bottom - self.rect.height)
      self.direction = self.direction.set_y(-abs(self.direction.y))
      #self.direction = self.direction.rotate(random.uniform(-self.MAX_ANGLE, self.MAX_ANGLE))

    # Check left bound
    if self.rect.right < bounds.left:
      self.position = self.position.set_x(bounds.left)
      self.direction = self.direction.flipx()
      self.randomize_direction()
      self.position = self.position.set_y(random.randint(bounds.top, bounds.bottom - self.rect.height))
      self.position = self.position.set_x(random.choice([0-self.rect.width, bounds.right]))
      self.speed = random.randint(2, 5)


    # Choose new direction if close enough
   # if self.distance_to_direction() < self.step_size :
    #  self.randomize_direction()

    # Update position
    #direction_step = self.get_direction().normalize(self.step_size)
    direction_step = self.direction.normalize(self.step_size)
    print "step: %s" % direction_step
    print "pos:  %s" % self.position
    self.position += direction_step

    self.rect.top = round(self.position.y)
    self.rect.left = round(self.position.x)


def test_fish():
    fish = Fish();

if __name__ == "__main__":
  # init pygame for test
  pygame.init()
  pygame.display.set_mode((640, 480))
  # run test
  test_fish()