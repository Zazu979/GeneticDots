#! python3

import array as arr
import random

from army import Army

from tkinter import Tk, Canvas, W


def move(window, army):
   army.move()
   window.after(10, move, window, army)

def main():
   window = Tk()
   canvas = Canvas(window, bg="white", height=500, width=500)
   canvas.grid(row=0, column=0, sticky=W)

   wall1_coords = [0,100,300,150]
   wall1 = canvas.create_rectangle(wall1_coords, outline="purple", fill="purple")

   wall2_coords = [150,300,500,350]
   wall2 = canvas.create_rectangle(wall2_coords, outline="purple", fill="purple")


   goal_coords = [250-10,450-10,250+10,450+10]
   goal = canvas.create_oval(goal_coords, outline="blue",fill="blue")

   army = Army(window, canvas, 250, 50, goal_coords)

   move(window, army)

   canvas.pack()
   window.mainloop()

if __name__ == "__main__":
   main()