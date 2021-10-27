#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 10
leg_length = 70
leg_distance = 380 / legs
spider.pensize(5)
leg_counter = 0
while (leg_counter < legs):
  spider.goto(0,0)
  spider.setheading(leg_distance*leg_counter)
  spider.forward(leg_length)
  leg_counter = leg_counter + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()

