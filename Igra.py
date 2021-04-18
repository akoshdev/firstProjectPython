from turtle import Turtle, Screen

oyna = Screen()

oyna.title('My merror')

chiziq = Turtle()
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.hideturtle()
chiziq.pensize(5)
chiziq.color('red')
chiziq.speed(0)
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

koptok = Turtle()
koptok.shape('circle')
koptok.color('blue')
koptok.up()

koptok.goto(0, 0)

# quti = Turtle()
# quti.up()
# quti.goto(-300,-240)
# quti.down()
# quti.goto(-240,-240)
# quti.down()
# qiti.goto(-240,-300)
# # quti.goto(-250,-150)

ch = Turtle()
ch.color('green')
ch.pensize(6)
ch.speed(0)
ch.hideturtle()
ch.up()
ch.speed(0)
ch.goto(-50, -260)
ch.down()
ch.goto(-260, -260)
ch.goto(-260, -50)
ch.goto(-50, -50)
ch.goto(-50, -260)

# step_x = 3
# step_y = 2
#
# while True:
#     x , y = koptok.position()
#
#     if x + step_x >= 300 or x + step_x <= -300:
#         step_x = -step_x
#
#     if y + step_y >= 300 or y + step_y <= -300:
#         step_y = -step_y
#
#     koptok.goto(x + step_x,y + step_y)

step_x = 3  # 6
step_y = 2

step_x = 4
step_y = 3
while True:
    x, y = koptok.position()
    if x + step_x > 260 or x + step_x < -260:
        step_x = -step_x
    if y + step_y > 260 or y + step_y < -260:
        step_y = -step_y
    if x + step_x == -50 or x + step_x == -260:
        break
    if y + step_y == -50 or y + step_y == -260:
        break
    koptok.goto(x + step_x, y + step_y)

oyna.mainloop()
