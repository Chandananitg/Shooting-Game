from turtle import Screen
from graphics import Stars
from player import Player
import time
from scoreboard import Scoreboard
from bullet import Bullet
from bots import Bots, speed_bot

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STAR_COUNT = 100
BULLET_COLLISION_DIST = 20
BOT_COLLISION_DIST = 25
BOT_LOWER_BOUND = -280
SLEEP_TIME = 2
SCORE_INTERVAL = 10
TIME_DECREASE = 0.09
BOT_INTERVAL = 10

screen = Screen()
screen.title("Turtle Shooting")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("gray10")
screen.tracer(0)
scoreboard = Scoreboard()
game_is_on = True
bot_list = []
bullet_list = []

for _ in range(STAR_COUNT):
    stars = Stars()


def fire():
    global player, bullet_list
    bullet = Bullet((player.xcor(), player.ycor()))
    bullet_list.append(bullet)


def stop():
    global game_is_on
    game_is_on = False


player = Player()
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(fire, "space")
screen.onkey(stop, "x")
no_of_iterations = 1

while game_is_on:
    time.sleep(0.05)
    screen.update()
    for bot in bot_list:
        bot.move()
    for bull in bullet_list:
        bull.movebull()
        if bull.ycor() > 300:
            bull.hide_bull()
            bull_index = bullet_list.index(bull)
            pop_bull = bullet_list.pop(bull_index)
    for bul in bullet_list:
        for but in bot_list:
            if bul.distance(but.xcor(), but.ycor()) < BULLET_COLLISION_DIST:
                scoreboard.score_up()
                bul.hideturtle()
                but.hideturtle()
                but_index = bot_list.index(but)
                bul_index = bullet_list.index(bul)
                pop_bul = bullet_list.pop(bul_index)
                pop_but = bot_list.pop(but_index)
                if scoreboard.score % SCORE_INTERVAL == 0 and bot_list != []:
                    speed_bot()

    for bot in bot_list:
        if bot.distance(player) < BOT_COLLISION_DIST:
            scoreboard.game_over()
            time.sleep(SLEEP_TIME)
            game_is_on = False
    for but in bot_list:
        if but.ycor() < BOT_LOWER_BOUND:
            scoreboard.game_over()
            time.sleep(SLEEP_TIME)
            game_is_on = False

    if no_of_iterations % BOT_INTERVAL == 0:
        bot = Bots()
        bot_list.append(bot)
        no_of_iterations = 1

    no_of_iterations += 1

screen.exitonclick()
