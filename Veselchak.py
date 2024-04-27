import turtle
import random
import time
def viselchak0():
    turtle.right(90)
    turtle.forward(200)

def viselchak1():
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)

def viselchak2():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(100)

def viselchak3():
    turtle.right(90)
    turtle.forward(50)

def viselchak4():
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()

def viselchak5():
    turtle.forward(80)

def viselchak6():
    turtle.left(45)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(30)
    turtle.right(45)

def viselchak7():
    turtle.left(135)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(30)
    turtle.left(45)

def viselchak8():
    turtle.forward(60)
    turtle.right(135)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(30)
    turtle.right(45)

def viselchak9():
    turtle.left(135)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(30)
    turtle.left(45)
    while True:
        pass


def f1():
    slova = ["NALOGI", "PUTIN", "TRAMP", "UZBEKISTAN"]
    wrd = list(random.choice(slova))
    s = len(wrd)
    dlinna = list(s * "_")
    flag = 0
    while True:
        print("Назови букву(Большую)", *dlinna)
        answer = input()
        if answer in wrd:
            position = wrd.index(answer)
            dlinna[position] = answer

            if "_" not in dlinna:
                print("Ты свободен")
                break

        else:
            if flag == 0:
                viselchak0()
                flag += 1

            elif flag == 1:
                viselchak1()
                flag += 1

            elif flag == 2:
                viselchak2()
                flag += 1

            elif flag == 3:
                viselchak3()
                flag += 1

            elif flag == 4:
                viselchak4()
                flag += 1

            elif flag == 5:
                viselchak5()
                flag += 1

            elif flag == 6:
                viselchak6()
                flag += 1

            elif flag == 7:
                viselchak7()
                flag += 1

            elif flag == 8:
                viselchak8()
                flag += 1

            elif flag == 9:
                viselchak9()
                print("Поздравляю, тебя кастрировали")
