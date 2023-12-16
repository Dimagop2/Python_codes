from turtle import *
#tree
def tree(a, b):
    n = 0
    while n < 9:
        n += 1
        speed(0)
        up()
        home()
        down()
        up()
        goto(a + 100*n, b)
        down()
        begin_fill()
        color('brown')
        circle(5, 630)
        position()
        fd(35)
        circle(5, 540)
        fd(35)
        circle(5, 630)
        end_fill()
        begin_fill()
        color('green')
        circle(30)
        end_fill()
