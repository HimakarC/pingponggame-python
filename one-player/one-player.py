import turtle

window = turtle.Screen()
window.title("Ping Pong By HIMAKAR")                      # create window title
window.bgcolor("skyblue")                                 # set the color of the BG
window.setup(width=1000, height=800)                     # set window width and height
window.tracer(0)                                        # prevent auto update of the window

player1 = turtle.Turtle()
player1.speed(0)                                        # set the speed of player1 (the speed of drawing the pixels on the screen) => to be fast
player1.shape("square")                                 # set the shape of player1
player1.shapesize(stretch_wid=1, stretch_len=5)         # set the shape size of player1
player1.color("red")                                    # set the color of player1
player1.penup()                                         # to prevent drawing when moving
player1.goto(0, -250)

# create the ball

ball = turtle.Turtle()
ball.speed(0)                                             # set the speed of the ball (the speed of drawing the pixels on the screen) => to be fast
ball.shape("circle")                                     # set the shape of the ball
ball.color("white")                                     # set the color of the ball
ball.penup()                                            # to prevent drawing when moving
ball.goto(0, 0)                                         # set the site of the ball
# You can increase the ball speed here
ball.dx = 4.5
ball.dy = 4.5

# create the score

sc4 = 0
score = turtle.Turtle()
score.speed(10)                                          # set the speed of the score (the speed of drawing the pixels on the screen) => to be fast
score.color("white")                                    # set the color of the score
score.penup()                                           # to prevent drawing when moving
score.hideturtle()
score.goto(0, 260)                                      # set the site of the score
score.write("player 1: 0", align = "center", font = ("Courier", 15, "normal"))

# game functions

# moving player 1 up

def player1_up():
    x = player1.xcor()                                  # current site of player4
    x += 30                                             # add 30 to the current x-axis
    player1.setx(x)                                     # set the new site of player4

# moving player 1 down
def player1_down():
    x = player1.xcor()                                  # current site of player4
    x -= 30                                             # minus 30 from the current x-axis
    player1.setx(x)


# keyboard binding

window.listen()
window.onkeypress(player1_up, "Right")                     # apply player1_up function when I press on "Right arrow"
window.onkeypress(player1_down, "Left")                 # apply player1_down function when I press on "Left arrow"


# main game loop

while True:

    window.update()                                     # update the screen every time the loop runs

    ball.setx(ball.xcor() + ball.dx)                    # movement of the ball along x-axis
    ball.sety(ball.ycor() + ball.dy)                    # movement of the ball along y-axis



    if ball.ycor() > 250:                              # if the ball touched the lower boarder of the window (lower boarder of the window at -250 px and the ball is 20 px)

        ball.sety(250)
        ball.dy *= -1

        score.clear()  # to clear the old score and update it
        score.write(f"player 1: {sc4}", align="center", font=("Courier", 15, "normal"))


    if ball.xcor() > 300:                               # if the ball touched the right boarder of the window (right boarder of the window at 300 px and the ball is 20 px)

        ball.setx(300)
        ball.dx *= -1

        score.clear()                                   # to update the old score
        score.write(f"player 1: {sc4}", align = "center", font = ("Courier", 15, "normal"))


    if ball.xcor() < -300:                              # if the ball touched the left boarder of the window (left boarder of the window at -300 px and the ball is 20 px)
        ball.setx(-300)
        ball.dx *= -1

        score.clear()                                   # to update the old score
        score.write(f"player 1: {sc4}", align = "center", font = ("Courier", 15, "normal"))

    # collision of player 1 with the ball
    if (ball.ycor() > -250 and ball.ycor() < -240) and (ball.xcor() < player1.xcor() + 40 and ball.xcor() > player1.xcor() - 40):
        ball.sety(-240)
        ball.dy *= -1
        sc4 += 1
        score.clear()  # to update the old score
        score.write(f"player 1: {sc4}", align="center", font=("Courier", 15, "normal"))

    if ball.ycor() < -250:                              # if the ball touched the lower boarder of the window (lower boarder of the window at -250 px and the ball is 20 px)

        ball.goto(0, 0)
        ball.dy *= -1

        sc4 -= 1
        score.clear()  # to clear the old score and update it
        score.write(f"player 1: {sc4}", align="center", font=("Courier", 15, "normal"))
