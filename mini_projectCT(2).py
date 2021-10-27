import turtle as trtl
t = trtl

color = input("What is your favorite color? ")

t.speed(0)

def create_drawing():
  x = 1
  while x > 0:
    t.pencolor(color)
    t.circle(50)
    x = x + -1

for i in range(9):
  create_drawing()
  t.right(40)
  
wn = trtl.Screen()
wn.mainloop()

