import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['black', 'orange', 'yellow', 'green', 'cyan', 'purple', 'pink', 'brown', 'blue', 'red']


def get_number_of_turtles():
  while True:
    nb_turtles = input("Enter the number of turtles that will be racing(2-10): ")
    if nb_turtles.isdigit():
      nb_turtles = int(nb_turtles)
      if 2 <= nb_turtles <= 10:
        break
      else:
        print("\nNumber of turtles must be between 2 and 10")

    else:
      print("\nEnter a valid number")
  return nb_turtles

def setting_screen():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title ('Turtle Racing!')
  
def creating_racers(colors):
  racers = [] 
  spacingx = WIDTH // (len(colors) + 1)
  for i, color in enumerate(colors):
    racer = turtle.Turtle()
    #racer.speed(1)
    racer.shape('turtle')
    racer.color(color)
    racer.left(90)
    racer.penup()
    racer.setpos(-WIDTH // 2 + (i +1) * spacingx, -WIDTH // 2 + 20)
    racer.pendown()
    racers.append(racer)
  return racers

def race(colors):
  turtles = creating_racers(colors)
  while True:
    for turtle in turtles:
      distance = random.randint(1, 10)
      turtle.forward(distance)
      x,y = turtle.pos()
      if y >= WIDTH // 2 - 20:
        return colors[turtles.index(turtle)]

def main():
  nb_turtles = get_number_of_turtles()
  
  random.shuffle(COLORS)
  colors = COLORS[: nb_turtles]

  screen = setting_screen()

  winner = race(colors)
  print("The winner is :", winner)
  time.sleep(2)

  
  
main()