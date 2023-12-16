from turtle import *
#cloud
def cloud(d, e):
    n = 0
    while n < 4:
        n += 1
        speed(0)
        up()
        home()
        down()
        up()
        goto(d + 35*n, e)
        down()
        begin_fill()
        color('white')
        circle(30)
        position()
        up()
        goto(d + 40 + 40*n, e)
        down()
        circle(35)
        position()
        up()
        goto(d + 80 + 35*n, e)
        down()
        circle(30)
        position()
        end_fill()

        up()
        home()
        down()
        up()
        goto(d + 600 + 40*n, e)
        down()
        begin_fill()
        color('white')
        circle(30)
        position()
        up()
        goto(d + 640 + 45*n, e)
        down()
        circle(35)
        position()
        up()
        goto(d + 680 + 40*n, e)
        down()
        circle(30)
        position()
        end_fill()

        up()
        home()
        down()
        up()
        goto(d + 200 + 50*n, e + 90)
        down()
        begin_fill()
        color('white')
        circle(30)
        position()
        up()
        goto(d + 240 + 55*n, e + 90)
        down()
        circle(35)
        position()
        up()
        goto(d + 280 + 50*n, e + 90)
        down()
        circle(30)
        position()
        end_fill()

