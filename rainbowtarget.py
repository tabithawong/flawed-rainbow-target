###################################
# Title: "Rainbow Target"         #
# Programmer: Tabitha Wong        #
# Last modified:  March 27, 2019  #     
###################################

from tkinter import *
from random import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()

#GRID LINES
spacing = 50
for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="yellow")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "yellow")

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="yellow")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "yellow")

#RINGS
d = 75
rx1 = 375
rx2 = rx1 + d
ry1 = 375
ry2 = ry1 + d
#pink = [
for rings in range(6):
    screen.create_oval(rx1, ry1, rx2, ry2, outline = "white", width = 2)
    rx1 = rx1 - d
    ry1 = ry1 - d
    rx2 = rx2 + d
    ry2 = ry2 + d

#BALL
diameter = 50
x1 = 400
y1 = 400
xSpeed = 11
ySpeed = -2
for a in range (1000):
    x1 = x1 + xSpeed  
    y1 = y1 + ySpeed
    
    x2 = x1 + diameter
    y2 = y1 + diameter


    if x1 <= 0:
        xSpeed = -1 * xSpeed

    if x2 >= 800:
        xSpeed = -1 * xSpeed

    if y1 <= 0:
        ySpeed = -1 * ySpeed

    if y2 >= 800:
        ySpeed = -1 * ySpeed

    #CENTRE OF BALL
    xm = (x1 + x2)/2
    ym = (y1 + y2)/2
    mid = (xm,ym)

    #COLOURS
    if 0 <= xm <= 800 and 0 <= ym <= 800:
        c = "red"
    if 75 <= xm <= 750 and 75 <= ym <= 750:
        c = "orange"
    if 150 <= xm <= 675 and 150 <= ym <= 675:
        c = "yellow"
    if 225 <= xm <= 600 and 225 <= ym <= 600:
        c = "green"
    if 300 <= xm <= 525 and 300 <= ym <= 525:
        c = "blue"
    if 375 <= xm <= 450 and 375 <= ym <= 450:
        c = "purple"
        
    #DRAW BALL        
    ball = screen.create_oval(x1,y1,x2,y2,outline = c, fill = c)
    screen.update()

    #SLOW DOWN ANIMATION
    sleep(0.03)

    #DELETE OLD FRAMES
    screen.delete(ball)
