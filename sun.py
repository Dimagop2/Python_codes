from turtle import *
#sun
def sun():
    up()
    home()
    down()
    up()
    goto(510, 410)
    down()
    begin_fill()
    pensize(3)
    color('yellow')
    for i in range(18):
        fd(60)
        rt(100)
    end_fill()
