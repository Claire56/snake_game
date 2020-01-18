import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor('purple')
wn.title('Claire_codes Snake game')
wn.setup(height=600, width=600)
wn.tracer(0) #turns off animation on the screen and updates

delay =0.3
score= 0
high_score =0
tails=[]

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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


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
    if snake.distance(food)<=20:
        food.goto(random.randint(-290,290), random.randint(-290,290))

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        tails.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

    # Move the end tails first in reverse order
    for index in range(len(tails)-1, 0, -1):
        x = tails[index-1].xcor()
        y = tails[index-1].ycor()
        tails[index].goto(x, y) #current tail is moved to the prev tail location

    # Move segment 0 to where the snahe head  is
    if len(tails) > 0:
        x = snake.xcor()
        y = snake.ycor()
        tails[0].goto(x,y)
    move()
    time.sleep(delay)


wn.mainloop()
