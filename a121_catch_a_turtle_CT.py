# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t

#-----game configuration----
shape = t.shape("triangle")
size = t.shapesize(10)
color = t.fillcolor("blue")



#-----initialize turtle-----
johnathan = t.Turtle()

#-----game functions--------
johnathan.shape(shape)
johnathan.shapesize(size)
johnathan.fillcolor(color)


#-----events----------------
wn = t.Screen()
wn.mainloop()