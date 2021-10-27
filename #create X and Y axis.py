#group members: Zach, Connor, Anvit
import turtle as t

#asks the user for equation
b = int(input("what should b be: "))

t.hideturtle()
#t.setup(1000,500 )
t.title('Rounded Rectangle - Pythont.Academy')
t.speed(0)
t.up()
t.hideturtle()

#creates calculator GUI
def round_rectangle(center_x,center_y,width,height,cornersize):
    t.fillcolor("yellow")
    t.begin_fill()
    t.up()
    t.goto(center_x-width/2+cornersize,center_y-height/2)
    t.down()
    for _ in range(2):
        t.fd(width-2*cornersize)
        t.circle(cornersize,90)
        t.fd(height-2*cornersize)
        t.circle(cornersize,90)
    t.end_fill()

round_rectangle(0,0,300,300,20)    

#create X and Y axis
t.fillcolor("white")
t.begin_fill()
t.pencolor("black")
t.penup()
t.setposition(0,20)
t.pendown()
for i in range(4):
  t.forward(100)
  t.left(90)
  t.forward(100)
t.end_fill()
t.setposition(0, 120)
t.forward(100)
t.backward(200)
t.penup()
t.setposition(0, 220)
t.pendown()
t.setposition(0,120)
t.pencolor("light grey")
t.penup()
t.speed(0)
t.setposition(-100, 120)
t.pendown()
for i in range(20):
  t.forward(10)
  t.left(90)
  t.forward(100)
  t.backward(200)
  t.forward(100)
  t.right(90)
t.penup()
t.setposition(-100, 220)
t.pendown()
for i in range(10):
  t.forward(200)
  t.right(90)
  t.forward(10)
  t.right(90)
  t.forward(200)
  t.left(90)
  t.forward(10)
  t.left(90)
t.penup()
t.setposition(0, 120)
t.pendown()
t.pencolor("black")
t.forward(100)
t.backward(200)
t.penup()
t.setposition(0, 220)
t.pendown()
t.setposition(0, 20)

#creates the graph 
t.penup()
t.setposition(0, (b+120))
t.pendown()
t.forward(20)

time.sleep(0)