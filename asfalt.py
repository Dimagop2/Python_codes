from turtle import *
#asfalt
def asfalt():
    penup()
    home()
    pendown()
    penup()
    goto(-2000,-500)
    pendown()    
    color('gray')
    begin_fill()
    fd(3000)
    lt(90)
    fd(70)
    lt(90)
    fd(3000)
    lt(90)
    fd(70)
    end_fill()

