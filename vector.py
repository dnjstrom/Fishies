#!/usr/bin/python

from math import sqrt

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


  def length(self):
    return sqrt(self.x**2 + self.y**2)

  def normalize(self):
    l = self.length()
    if l == 0:
      return None
    else:
      return Vector(self.x / l, self.y / l)


def test_vector():
  v = Vector(3,4)
  print v
  print v.x
  w = Vector(1,2)
  print v+w
  print v-w
  print v.length()
  print v.normalize().length()
  print w.normalize().length()

if __name__ == "__main__":
  test_vector()