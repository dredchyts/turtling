from turtle import *

width(3)
shape('turtle')
speed(1)

color('blue')
up()
goto(-110,-25)
down()
circle(45)

color('black')
up()
goto(0,-25)
down()
circle(45)

color('red')
up()
goto(110,-25)
down()
circle(45)

color('yellow')
up()
goto(-55,-75)
down()
circle(45)

color('green')
up()
goto(55,-75)
down()
circle(45)

color('red')
up()
goto(0,80)
down()

write('Редчиць Ганна', False, 'center', ('Arial', 20, 'bold'))
hideturtle()
