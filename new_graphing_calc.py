import turtle as t
t.speed(0)

def hash_marks():
  for i in range (40):
    t.forward(10)
    t.left(90)
    t.forward(5)
    t.backward(10)
    t.forward(5)
    t.right(90)

hash_marks()
t.penup()
t.setposition(0, 0)
t.right(180)
t.pendown()
hash_marks()
t.penup()
t.setposition(0, 0)
t.right(90)
t.pendown()
hash_marks()
t.penup()
t.setposition(0, 0)
t.right(180)
t.pendown()
hash_marks()

x = (input("Enter an equation in the form y=mx+b: ")
y = x[6]
