#! python3

import random
from tkinter import Tk, Canvas

class Dot:

   movement_speed = 20

   max_ticks = 500

   def __init__(self, circle, window, canvas, goal):
      self.circle = circle
      self.window = window
      self.canvas = canvas
      self.dead = False

      self.goal = goal
      self.reached_goal = False

      self.updateCoods()

      self.movements = []

      self.tick = 0
      self.movement_length = 0

   def isActive(self):
      return not self.dead and not self.reached_goal

   def move(self):
      if self.isActive():

         if self.tick >= self.movement_length:
            x_vel = random.randint(-self.movement_speed,self.movement_speed)
            y_vel = random.randint(-self.movement_speed,self.movement_speed)
            self.movements.append([x_vel, y_vel])
         else:
            x_vel = self.movements[self.tick][0]
            y_vel = self.movements[self.tick][1]

         self.tick = self.tick +1 
         self.canvas.move(self.circle, x_vel, y_vel)
         self.updateCoods()

         self.checkCollision()

         if self.tick > self.max_ticks:
            self.dead = True

   def checkCollision(self):
      if self.x < 0 or self.x > 490 or self.y < 0 or self.y > 490:
         self.dead = True
      elif self.x in range(0,300) and self.y in range(100,150):
         self.dead = True
      elif self.x in range(150,500) and self.y in range(300,350):
         self.dead = True
      elif self.x in range(self.goal[0], self.goal[2]) and self.y in range(self.goal[1], self.goal[3]):
         self.reached_goal = True

   def updateCoods(self):
      coords = self.canvas.coords(self.circle)

      self.x = coords[0]
      self.y = coords[1]

   def destroy(self):
      self.canvas.delete(self.circle)

   def mutate(self):
      for move in self.movements:
         for i in range(2):
            roll = random.randint(0,99)
            if roll < 70:
               # Do nothing
               pass
            elif roll < 85:
               # slight change
               move[i] = move[i] + random.randint(-self.movement_speed/10,self.movement_speed/10)
            elif roll < 90:
               # slight change
               move[i] = move[i] + random.randint(-self.movement_speed/5,self.movement_speed/5)
            elif roll < 95:
               move[i] = random.randint(-self.movement_speed,self.movement_speed)
            elif roll < 100:
               move[i] = -move[i]
            else:
               print("Something darn messed up")

            if move[i] < -self.movement_speed:
               move[i] = -self.movement_speed
            if move[i] > self.movement_speed:
               move[i] = self.movement_speed

