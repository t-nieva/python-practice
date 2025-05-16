from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BALL_DIAMETER = 20
BALL_RADIUS = BALL_DIAMETER / 2

PADDLE_WIDTH = 20  # Corresponds to stretch_len=1
PADDLE_HALF_WIDTH = PADDLE_WIDTH / 2

COLLISION_X_THRESHOLD = BALL_RADIUS + PADDLE_HALF_WIDTH
PADDLE_X_POS = 350

DASH_LENGTH = 20
GAP_LENGTH = 20

TOP_WALL = SCREEN_HEIGHT / 2
BOTTOM_WALL = -SCREEN_HEIGHT / 2

def draw_middle_line():
    bounce = Turtle(visible=False)
    bounce.color('white')
    bounce.pensize(5)
    bounce.penup()
    y = SCREEN_HEIGHT / 2
    while y > -(SCREEN_HEIGHT / 2):
        bounce.goto(0, y)
        bounce.pendown()
        y -= DASH_LENGTH
        bounce.goto(0, y)
        bounce.penup()
        y -= GAP_LENGTH

def is_collision(paddle: Paddle, tennis_ball: Ball) -> bool:
    paddle_top = paddle.ycor() + 50 # Based on stretch_wid=5
    paddle_bottom = paddle.ycor() - 50
    return (
            paddle_bottom <= tennis_ball.ycor() <= paddle_top and
            abs(tennis_ball.xcor() - paddle.xcor()) <= COLLISION_X_THRESHOLD
    )

# --- Screen setup ---
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.tracer(0)

draw_middle_line()

right_paddle = Paddle((PADDLE_X_POS, 0), TOP_WALL, BOTTOM_WALL)
left_paddle = Paddle((-PADDLE_X_POS, 0), TOP_WALL, BOTTOM_WALL)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up,'Up')
screen.onkey(right_paddle.down,'Down')
screen.onkey(left_paddle.up,'w')
screen.onkey(left_paddle.down,'s')


start_game = True

while start_game:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if (ball.ycor() > TOP_WALL - BALL_DIAMETER or
            ball.ycor() < BOTTOM_WALL + BALL_DIAMETER):
        ball.y_bounce()

    # Detect collision with paddle
    if (is_collision(right_paddle, ball) or
            is_collision(left_paddle, ball)):
        ball.x_bounce()

    # Detect when paddle misses
    if ball.xcor() > PADDLE_X_POS + BALL_RADIUS:
        ball.reset_position()
        scoreboard.left_point()
        ball.set_direction(-1)

    if ball.xcor() < -PADDLE_X_POS - BALL_RADIUS:
        ball.reset_position()
        scoreboard.right_point()
        ball.set_direction(1)

    if scoreboard.left_score == 5 or scoreboard.right_score == 5:
        scoreboard.game_over()
        start_game = False

screen.exitonclick()
