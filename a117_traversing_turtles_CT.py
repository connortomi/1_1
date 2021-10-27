#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)
  new_color = turtle_colors.pop()

#  set starting position
startx = 0
starty = 0

# create each branch 
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()

  t.right(45)     
  t.forward(50)
  t.start_x = t.xcor()
  t.start_y = t.ycor()
  new_color = turtle_colors.pop()


#	go back to the starting position
# change starting position by 50 pixels on the x and y axis
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()