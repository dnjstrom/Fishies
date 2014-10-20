#!/usr/bin/python

import pygame
import math
import random

from vector import Vector

# debug
from pdb import set_trace

class Fish(pygame.sprite.Sprite):

  def __init__(self):
    self.unflipped = pygame.image.load('img/fish2.png').convert_alpha()
    self.flipped = pygame.transform.flip(self.unflipped, True, False)
    self.image = self.unflipped

    self.rect = self.image.get_rect()
    self.direction = Vector(3,1)
    self.position = Vector(0, 0)
    self.MAX_ANGLE = math.pi/16
    self.step_size = random.randint(1, 3)
    self.delay = 0

    self.randomize_direction()

  def set_direction(self, x, y):
    self.direction = Vector(x, y)

  def randomize_direction(self):
    random_angle = random.uniform(-self.MAX_ANGLE, self.MAX_ANGLE)
    self.direction = self.direction.rotate(random_angle).normalize()

  def move(self, dx, dy):
    self.position += Vector(dx, dy)

  def general_direction(self):
    deg = math.degrees(self.direction.angle)

    while deg < 0:
      deg += 360

    if deg > 90 and deg < 270:
      return Vector(-1, 0)
    else:
      return Vector(1, 0)


  def update(self, bounds):
    if bounds.height <= self.rect.height:
      self.direction = self.general_direction()
      self.position = self.position.set_y(bounds.bottom - self.rect.height)

    if self.delay != 0:
      self.delay -= 1
      return # Quit early
    else:
      direction_step = self.direction.normalize(self.step_size)
      self.position += direction_step
      self.rect.top = round(self.position.y)
      self.rect.left = round(self.position.x)


    # Check top bound
    if self.rect.top < bounds.top and bounds.height > self.rect.height:
      self.position = self.position.set_y(bounds.top)
      self.randomize_direction()
      self.direction = self.direction.set_y(abs(self.direction.y))

    # Check bottom bound
    if self.rect.bottom > bounds.bottom and bounds.height > self.rect.height:
      self.position = self.position.set_y(bounds.bottom - self.rect.height)
      self.direction = self.direction.set_y(-abs(self.direction.y))
      self.randomize_direction()

    # Check right and left bound
    if self.rect.left > bounds.right or self.rect.right < bounds.left:
      if bounds.height < self.rect.height:
        self.position = self.position.set_y(bounds.bottom - self.rect.height)
      else:
        self.position = self.position.set_y(random.randint(bounds.top, bounds.bottom - self.rect.height))

      self.position = self.position.set_x(random.choice([-self.rect.width, bounds.right]))

      # Flip direction depending on what edge we're at
      if self.position.x == -self.rect.width:
        self.direction = Vector(1, 0)
      else:
        self.direction = Vector(-1, 0)

      if bounds.height > self.rect.height:
        self.randomize_direction()

      self.step_size = random.randint(1, 3)
      self.delay = random.randint(15, 30*3)

      if self.general_direction() == Vector(1, 0):
        self.image = self.unflipped
      else:
        self.image = self.flipped




def test_fish():
    fish = Fish();

if __name__ == "__main__":
  # init pygame for test
  pygame.init()
  pygame.display.set_mode((640, 480))
  # run test
  test_fish()