#!/usr/bin/python

import math

from pdb import set_trace

class Vector(object):
  """A very basic 2D vector class"""

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "(%s, %s)" % (self.x, self.y)

  def __neg__(self):
    return Vector(-self.x, -self.y)

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return self + (-other)

  def __getitem__(self, key):
    if key == 0:
      return self.x
    elif key == 1:
      return self.y
    else:
      raise IndexError("Index out of bounds: " + str(key))

  @classmethod
  def make(cls, angle, length):
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    return cls(x, y)

  @property
  def length(self):
    return math.sqrt(self.x**2 + self.y**2)

  @property
  def angle(self):
    if self.length == 0:
      return 0
    else:
      return math.atan2(self.y, self.x)

  def normalize(self, length=1):
    return Vector.make(self.angle, length)

  def get_point(self):
    return (self.x, self.y)

  def rotate(self, angle):
    if self.length == 0:
      return self.copy()
    else:
      return Vector.make(self.angle + angle, self.length)

  def copy(self):
    return Vector(self.x, self.y)

  def flipx(self):
    return Vector(-self.x, self.y)

  def flipy(self):
    return Vector(self.x, -self.y)


def test_vector():
  print "%s | %s" % (0,Vector(1,0).angle)
  print "%s | %s" % (math.pi*0.25,Vector(1,1).angle)
  print "%s | %s" % (math.pi*0.50,Vector(0,1).angle)
  print "%s | %s" % (math.pi*0.75,Vector(-1,1).angle)
  print "%s | %s" % (math.pi*1.00,Vector(-1,0).angle)
  print "%s | %s" % (math.pi*1.25,Vector(-1,-1).angle)
  print "%s | %s" % (math.pi*1.50,Vector(0,-1).angle)
  print "%s | %s" % (math.pi*1.75,Vector(1,-1).angle)

if __name__ == "__main__":
  test_vector()