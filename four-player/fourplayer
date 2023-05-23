import turtle

window = turtle.Screen()
window.title("Ping Pong By HIMAKAR")                      # create window title
window.bgcolor("skyblue")                                 # set the color of the BG
window.setup(width=1000, height=800)                     # set window width and height
window.tracer(0)                                        # prevent auto update of the window

player1 = turtle.Turtle()
player1.speed(0)                                        # set the speed of player1 (the speed of drawing the pixels on the screen) => to be fast
player1.shape("square")                                 # set the shape of player1
player1.shapesize(stretch_wid=5, stretch_len=1)         # set the shape size of player1
player1.color("yellow")                                 # set the color of player1
player1.penup()                                         # to prevent drawing when moving
player1.goto(-370, 0)                                   # set the site of player1

player2 = turtle.Turtle()
player2.speed(0)                                        # set the speed of player2 (the speed of drawing the pixels on the screen) => to be fast
player2.shape("square")                                 # set the shape of player2
player2.shapesize(stretch_wid=5, stretch_len=1)         # set the shape size of player2
player2.color("red")                                    # set the color of player2
player2.penup()                                         # to prevent drawing when moving
player2.goto(370, 0)                                    # set the site of player2

player3 = turtle.Turtle()
player3.speed(0)                                        # set the speed of player3 (the speed of drawing the pixels on the screen) => to be fast
player3.shape("square")                                 # set the shape of player3
player3.shapesize(stretch_wid=1, stretch_len=5)         # set the shape size of player3
player3.color("red")                                    # set the color of player3
player3.penup()                                         # to prevent drawing when moving
player3.goto(0, 250)

player4 = turtle.Turtle()
player4.speed(0)                                        # set the speed of player4 (the speed of drawing the pixels on the screen) => to be fast
player4.shape("square")                                 # set the shape of player4
player4.shapesize(stretch_wid=1, stretch_len=5)         # set the shape size of player4
player4.color("red")                                    # set the color of player4
player4.penup()                                         # to prevent drawing when moving
player4.goto(0, -250)

# create the ball

ball = turtle.Turtle()
ball.speed(0)                                       # set the speed of the ball (the speed of drawing the pixels on the screen) => to be fast
ball.shape("circle")                                     # set the shape of the ball
ball.color("white")                                     # set the color of the ball
ball.penup()                                            # to prevent drawing when moving
ball.goto(0, 0)                                         # set the site of the ball
ball.dx = 4.5
ball.dy = 4.5

# create the score

score1 = 0
score2 = 0
sc3 = 0
sc4 = 0
score = turtle.Turtle()
score.speed(10)                                          # set the speed of the score (the speed of drawing the pixels on the screen) => to be fast
score.color("white")                                    # set the color of the score
score.penup()                                           # to prevent drawing when moving
score.hideturtle()
score.goto(0, 260)                                      # set the site of the score
score.write("player 1: 0 || player 2: 0 || player 3: 0 || player 4: 0", align = "center", font = ("Courier", 15, "normal"))

# game functions

# moving player 1 up
def player1_up():
    y = player1.ycor()                                  # current site of player1
    y += 30                                             # add 30 to the current y-axis
    player1.sety(y)                                     # set the new site of player1

# moving player 1 down
def player1_down():
    y = player1.ycor()                                  # current site of player1
    y -= 30                                             # minus 30 from the current y-axis
    player1.sety(y)                                     # set the new site of player1

# moving player 2 up
def player2_up():
    y = player2.ycor()                                  # current site of player2
    y += 30                                             # add 30 to the current y-axis
    player2.sety(y)                                     # set the new site of player2

# moving player 2 down
def player2_down():
    y = player2.ycor()                                  # current site of player2
    y -= 30                                             # minus 30 from the current y-axis
    player2.sety(y)                                     # set the new site of player2

def player3_up():
    x = player3.xcor()                                  # current site of player3
    x += 30                                             # add 30 to the current x-axis
    player3.setx(x)                                     # set the new site of player3

# moving player 3 down
def player3_down():
    x = player3.xcor()                                  # current site of player3
    x -= 30                                             # minus 30 from the current x-axis
    player3.setx(x)

def player4_up():
    x = player4.xcor()                                  # current site of player4
    x += 30                                             # add 30 to the current x-axis
    player4.setx(x)                                     # set the new site of player4

# moving player 4 down
def player4_down():
    x = player4.xcor()                                  # current site of player4
    x -= 30                                             # minus 30 from the current x-axis
    player4.setx(x)


# keyboard binding

window.listen()
window.onkeypress(player1_up, "q")                      # apply player1_up function when I press on "w"
window.onkeypress(player1_down, "w")                    # apply player1_down function when I press on "s"
window.onkeypress(player2_up, "Up")                     # apply player2_up function when I press on "up arrow"
window.onkeypress(player2_down, "Down")                 # apply player2_down function when I press on "down arrow"
window.onkeypress(player3_up, "a")                     # apply player3_up function when I press on "up arrow"
window.onkeypress(player3_down, "s")                 # apply player3_down function when I press on "down arrow"
window.onkeypress(player4_up, "z")                     # apply player4_up function when I press on "up arrow"
window.onkeypress(player4_down, "x")                 # apply player4_down function when I press on "down arrow"


# main game loop

while True:

    window.update()                                     # update the screen every time the loop runs

    ball.setx(ball.xcor() + ball.dx)                    # movement of the ball along x-axis
    ball.sety(ball.ycor() + ball.dy)                    # movement of the ball along y-axis

    if ball.ycor() > 250:                               # if the ball touched the upper boarder of the window (upper boarder of the window at 300 px and the ball is 20 px)

        ball.goto(0, 0)  # return the ball again to the center
        ball.dy *= -1

        sc3 -= 1
        score.clear()  # to clear the old score and update it
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align="center", font=("Courier", 15, "normal"))

    if ball.ycor() < -250:                              # if the ball touched the lower boarder of the window (lower boarder of the window at -300 px and the ball is 20 px)

        ball.goto(0, 0)  # return the ball again to the center
        ball.dy *= -1

        sc4 -= 1
        score.clear()  # to clear the old score and update it
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align="center", font=("Courier", 15, "normal"))

    if ball.xcor() > 390:                               # if the ball touched the right boarder of the window (right boarder of the window at 400 px and the ball is 20 px)

        ball.goto(0, 0)                                 # return the ball again to the center
        ball.dx *= -1                                   # and multiply ball.dx by -1 to become -0.3, so the movement will be in the opposite side

        score1 -= 1
        score.clear()                                   # to update the old score
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align = "center", font = ("Courier", 15, "normal"))


    if ball.xcor() < -390:                              # if the ball touched the left boarder of the window (left boarder of the window at -400 px and the ball is 20 px)

        ball.goto(0, 0)                                 # return the ball again to the center
        ball.dx *= -1                                   # and multiply ball.dx by -1 to become -0.3, so the movement will be in the opposite side

        score2 -= 1
        score.clear()                                   # to update the old score
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align = "center", font = ("Courier", 15, "normal"))

    # collision of player 1 with the ball
    if (ball.xcor() < -340 and ball.xcor() > -350) and (player1.ycor() + 40 > ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        score2 += 1
        score.clear()  # to update the old score
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align="center", font=("Courier", 15, "normal"))

    # collision of player 2 with the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (player2.ycor() + 40 > ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        score2 += 1
        score.clear()  # to update the old score
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align="center",font=("Courier", 15, "normal"))

    if (ball.ycor() < 250 and ball.ycor() > 240) and (ball.xcor() < player3.xcor() + 40 and ball.xcor() > player3.xcor() - 40):
        ball.sety(240)
        ball.dy *= -1
        sc3 += 1
        score.clear()  # to update the old score
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align="center", font=("Courier", 15, "normal"))

        # collision of player 4 with the ball
    if (ball.ycor() > -250 and ball.ycor() < -240) and (ball.xcor() < player4.xcor() + 40 and ball.xcor() > player4.xcor() - 40):
        ball.sety(-240)
        ball.dy *= -1
        sc4 += 1
        score.clear()  # to update the old score
        score.write(f"player 1: {score1} || player 2: {score2} || player 3: {sc3} || player 4: {sc4}", align="center", font=("Courier", 15, "normal"))
