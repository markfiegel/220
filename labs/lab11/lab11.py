"""
Mark Fiegel
lab11.py
I put together a game with random doors. I know it looks kinda janky but I didnt do too well on
the last lab.
I certify that this assignment is entirely my own work.
"""
from lab10.door import Door
from lab10.button import Button
from graphics import GraphWin, Rectangle, Text, Point, Line
from random import randint
def main():
    win  = GraphWin('win',800,550)
    win.setBackground('light blue')
    button = Button(Rectangle(Point(600,25),Point(750,100)),'Quit')
    door1 = Door(Rectangle(Point(100,150),Point(200,500)),'Door 1')
    rect1 = Rectangle(Point(0,0),Point(120,60))
    line = Line(Point(50,0),Point(50,60))
    line.draw(win)
    rect1.draw(win)
    door1.draw(win)
    door1.set_label()
    door2 = Door(Rectangle(Point(300, 150), Point(400, 500)), 'Door 2')
    door2.draw(win)
    door2.set_label()
    door3 = Door(Rectangle(Point(505, 150), Point(600, 500)), 'Door 3')
    door3.draw(win)
    door3.set_label()
    button.draw(win)
    secret = Text(Point(400,100),"It's a Secret!")
    you_win = Text(Point(400,100),"You Win!")
    you_lose = Text(Point(400,100),"You Lose!")
    door_pick = randint(1, 3)
    wins_losses = Text(Point(60,20),"Wins      Losses")
    play_again = Text(Point(400,525),"Click to play again!")
    wins = 0
    losses = 0
    game_on = True
    wins_losses.draw(win)
    while game_on == True:
        win_stat = Text(Point(20, 40), wins)
        loss_stat = Text(Point(85,40),losses)
        door1.color_door('brown')
        door2.color_door('brown')
        door3.color_door('brown')
        win_stat.draw(win)
        loss_stat.draw(win)
        secret.draw(win)
        point = win.getMouse()
        if button.is_clicked(point):
            break
        if door_pick == 1:
            door1.secret = True
        elif door_pick ==2:
            door2.secret = True
        elif door_pick ==3:
            door3.secret = True
        if (door1.is_clicked(point)and door1.is_secret()):
            secret.undraw()
            door1.color_door('green')
            you_win.draw(win)
            wins = wins+1
            play_again.draw(win)
            if door1.is_secret() == True:
                door1.color_door('green')
            elif door2.is_secret() == True:
                door2.color_door('green')
            elif door3.is_secret() == True:
                door3.color_door('green')
        elif door1.is_clicked(point)and not door1.is_secret():
            secret.undraw()
            door1.color_door('red')
            you_lose.draw(win)
            losses = losses +1
            play_again.draw(win)
            if door1.is_secret() == True:
                door1.color_door('green')
            elif door2.is_secret() == True:
                door2.color_door('green')
            elif door3.is_secret() == True:
                door3.color_door('green')
        elif door2.is_clicked(point)and door2.is_secret():
            secret.undraw()
            you_win.draw(win)
            wins = wins +1
            play_again.draw(win)
            door2.color_door('green')
            if door1.is_secret() == True:
                door1.color_door('green')
            elif door2.is_secret() == True:
                door2.color_door('green')
            elif door3.is_secret() == True:
                door3.color_door('green')

        elif door2.is_clicked(point)and not door2.is_secret():
            secret.undraw()
            door2.color_door('red')
            you_lose.draw(win)
            losses = losses +1
            play_again.draw(win)
            if door1.is_secret() == True:
                door1.color_door('green')
            elif door2.is_secret() == True:
                door2.color_door('green')
            elif door3.is_secret() == True:
                door3.color_door('green')
        elif door3.is_clicked(point) and door3.is_secret():
            secret.undraw()
            door3.color_door('green')
            wins = wins +1
            play_again.draw(win)
            you_win.draw(win)
            if door1.is_secret() == True:
                door1.color_door('green')
            elif door2.is_secret() == True:
                door2.color_door('green')
            elif door3.is_secret() == True:
                door3.color_door('green')

        elif door3.is_clicked(point) and not door3.is_secret():
            secret.undraw()
            door3.color_door('red')
            you_lose.draw(win)
            losses = losses + 1
            play_again.draw(win)
            if door1.is_secret() == True:
                door1.color_door('green')
            elif door2.is_secret() == True:
                door2.color_door('green')
            elif door3.is_secret() == True:
                door3.color_door('green')
        if button.is_clicked(win.getMouse()):
            break
        door1.secret = False
        door2.secret = False
        door3.secret = False
        you_lose.undraw()
        you_win.undraw()
        play_again.undraw()
        win_stat.undraw()
        loss_stat.undraw()
        secret.undraw()
        door_pick = randint(1,3)
main()