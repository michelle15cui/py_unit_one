# remember to use comments!
#michelle
#9.24.2023
#drawing octagon project

import turtle



def drawOctagon(mycolor):
    turtle.color(mycolor)
    turtle.begin_fill()


    for x in range(8):
        turtle.forward(50)
        turtle.right(45)

    turtle.end_fill()



def moveapin(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.speed(0)
drawOctagon("red")
moveapin(200,200)

drawOctagon("yellow")
moveapin(200,0)

drawOctagon("blue")
moveapin(0,200)

drawOctagon("green")
moveapin(200,200)




turtle.exitonclick()