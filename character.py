# Egg Bezos Hackdays 27 Project
import pygame
import pyglet

# Character class
class Character(pyglet.sprite.Sprite):
  def __init__(self, img, x, y, width, height):
    super.__init__(img=img, x=x, y=y)
    super.width = width
    super.height = height
    self.health = 100
    self.attackStrength = 1.0
    self.items = []
  def addItem(self, item):
    self.items.append(item)
  
