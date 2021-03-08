import turtle
          
turtle.shape('turtle')
turtle.setup(800,600)
window = turtle.Screen()
turtle.hideturtle()

turtle.penup()
turtle.setposition(-70,0)
turtle.pendown()
turtle.setposition(-70,200)
turtle.penup()
turtle.setposition(30,0)
turtle.pendown()
turtle.setposition(30,200)
turtle.penup()
turtle.setposition(-120,70)
turtle.pendown()
turtle.setposition(100,70)
turtle.penup()
turtle.setposition(-120,140)
turtle.pendown()
turtle.setposition(100,140)
turtle.penup()

def O(x,y):
    turtle.penup()
 #   turtle.setheading(270)
 #   turtle.forward(30)
    turtle.pendown()
 #   turtle.setheading(0)
    turtle.circle(30)
    
    


def X(x,y):
    
    turtle.penup()
    turtle.setposition(-40,0)
    turtle.pendown()
    turtle.setposition(0,40)    
    turtle.penup()
    turtle.setposition(-40,40)
    turtle.pendown()
    turtle.setposition(0,-2)




    


window.onclick(O)
