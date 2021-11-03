# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand

#-----game configuration----
shape = "triangle"
size = 10
color = "blue"
score = 0
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
johnathan = t.Turtle()
score_writer = t.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(300, 280)

#-----game functions--------
johnathan.shape(shape)
johnathan.shapesize(size)
johnathan.fillcolor(color)
def johnathan_clicked(x,y):
  update_score()
  change_position()
def change_position():
  new_xpos = rand.randint(0, 400)
  new_ypos = rand.randint(0, 300)
  johnathan.penup()
  johnathan.hideturtle()
  johnathan.goto(new_xpos, new_ypos)
  johnathan.showturtle()
  johnathan.pendown()
def update_score():
  score_writer.clear()
  global score 
  score = score + 1
  score_writer.write(score, font=font_setup)
  

#-----events----------------
wn = t.Screen()
johnathan.onclick(johnathan_clicked)
wn.mainloop()