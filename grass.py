from turtle import *
#grass
def grass():
    speed(0)
    penup()
    home()
    pendown()
    penup()
    goto(-2000,-430)
    pendown()    
    color('green')
    begin_fill()
    fd(3000)
    lt(90)
    fd(60)
    lt(90)
    fd(3000)
    lt(90)
    fd(60)
    end_fill()

