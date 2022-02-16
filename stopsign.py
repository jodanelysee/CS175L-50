import math
import turtle
glo = turtle.Turtle()
glo.shape('turtle')
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10
s = 100
x = 0
myColor = 'red'

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
diameter = s + 2 * x
s2 = x**2 + x**2
s2 = 2*x**2
x = s / math.sqrt(2)


glo.hideturtle()
glo.goto(-50,150)

glo.color(myColor)
glo.begin_fill()


for x in range (NUM_SIDES):
    glo.hideturtle()
    glo.forward(LENGTH)
    glo.right(ANGLE)

glo.end_fill()

glo.right(85)
glo.forward(50)
glo.backward(-90)
glo.color('white')
glo.write('STOP', font = ('Arial', 30, 'normal'))



    

