import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor('purple')
wn.title('Claire_codes Snake game')
wn.setup(height=500, width=500)
wn.tracer(0) #turns off animation on the screen and updates
delay =0.3
score=o

#create snake
snake = turtle.Turtle()
snake.color('black')
snake.shape('square')
snake.penup()
snake.speed(0)
snake.goto(0,0) #snake should be placed at the center of tthe screen.helps move fast
snake.direction ='stop'

#create food
food = turtle.Turtle()
food.color('red')
food.shape('circle')
food.penup()
food.speed(0)
food.goto(random.randint(10,100), random.randint(10,100))


#Functions 
def move():
    if snake.direction=='up':
        y= snake.ycor() #get y cordinate name it y
        snake.sety(y + 20) #reset y cordinate 
    if snake.direction=='down':
        y= snake.ycor() #get y cordinate name it y
        snake.sety(y -20) #reset y cordinate

    if snake.direction=='left':
        x= snake.xcor() #get y cordinate name it y
        snake.setx( x - 20) #reset y cordinate

    if snake.direction=='right':
        x= snake.xcor() #get y cordinate name it y
        snake.setx(x +20) #reset y cordinate

def go_up():
    snake.direction = 'up'

def go_down():
    snake.direction = 'down'

def go_left():
    snake.direction = 'left'

def go_right():
    snake.direction = 'right'

#key board bindings
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_right,'d')
wn.onkeypress(go_left,'a')


while True:
    wn.update()
    move()
    time.sleep(delay)


wn.mainloop()
