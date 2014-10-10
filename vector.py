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

  def length(self):
    return math.sqrt(self.x**2 + self.y**2)

  def angle(self):
    if self.length() == 0:
      return 0
    else:
      return math.asin(self.y / self.length())

  def normalize(self):
    l = self.length()
    if l == 0:
      return None # throw error instead?
    else:
      return Vector(self.x / l, self.y / l)

  def get_point(self):
    return (self.x, self.y)

  def rotate(self, angle):
    l = self.length()
    if l == 0:
      return self.copy()
    else:
      a = self.angle() + angle
      x = l * math.cos(a)
      y = l * math.sin(a)
      return Vector(x, y)

  def copy(self):
    return Vector(self.x, self.y)


def test_vector():
  v = Vector(3,4)
  print v
  print v.x
  print v.angle()
  print "#####"
  w = Vector(1,2)
  print v+w
  print v-w
  print v.length()
  print v.normalize().length()
  print w.normalize().length()
  print w.angle()
  print "#####"
  y = Vector(1,0)
  print y
  print y.rotate(math.pi/2)
  print Vector.make(math.pi, 5)
  print y.angle()
  print "#####"
  u = Vector(0,1)
  print u.angle()

if __name__ == "__main__":
  test_vector()