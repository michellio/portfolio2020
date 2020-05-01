#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# PC01 - GRAFFITI 

# Tran

# 01/24/2020

# 

# Description - Turtle draws a crown on a billboard to graffiti, then runs away once it's done.
# for this program you will need the "billboard.gif" file.

"""
#Code for background from canvas
from turtle import * #fetches turtle commands

dow = Screen() #create one canvas for all of your turtles. 

dow.screensize(591,591)
dow.bgpic("billboard.gif") #replace the text within the quotes with the name
#of your background file. Note: this ONLY takes gifs!
dow.update() #updates to draw any changes made to the canvas

#Now you have your canvas and background and are ready to draw!
#Create a turtle by setting the name equal to the command Turtle, like so:
Murdle = Turtle()
Murdle.shape("turtle")


#Crown body
Murdle.color("yellow")
Murdle.fillcolor("yellow")
Murdle.begin_fill()
Murdle.forward(100)
Murdle.left(80)
Murdle.forward(60)
Murdle.left(145)
Murdle.forward(30)
Murdle.left(-125)
Murdle.forward(50)
Murdle.left(145)
Murdle.forward(50)
Murdle.left(-125)
Murdle.forward(60)
Murdle.left(145)
Murdle.forward(50)
Murdle.left(-125)
Murdle.forward(50)
Murdle.left(140)
Murdle.forward(80)
Murdle.end_fill()

#Crown Balls orange left ball
Murdle.fillcolor("orange")
Murdle.color("orange")
Murdle.up()
Murdle.backward(80)
Murdle.left(90)
Murdle.backward(5)
Murdle.down()
Murdle.begin_fill()
Murdle.circle(10)
Murdle.end_fill()

#Crown balls orange 2nd left
Murdle.up()
Murdle.forward(59)
Murdle.left(90)
Murdle.forward(18)
Murdle.down()
Murdle.begin_fill()
Murdle.circle(10)
Murdle.end_fill()

#Crown balls 3
Murdle.up()
Murdle.right(90)
Murdle.forward(34)
Murdle.right(90)
Murdle.forward(15)
Murdle.down()
Murdle.begin_fill()
Murdle.circle(10)
Murdle.end_fill()

#Crown Ball 4
Murdle.up()
Murdle.forward(42)
Murdle.left(90)
Murdle.forward(37)
Murdle.down()
Murdle.begin_fill()
Murdle.circle(10)
Murdle.end_fill()
Murdle.up()
Murdle.forward(50)

#Diamond
Murdle.color("blue")
Murdle.fillcolor("blue")
Murdle.up()
Murdle.backward(125)
Murdle.right(90)
Murdle.forward(25)
Murdle.down()
Murdle.begin_fill()
Murdle.left(45)
Murdle.forward(15)
Murdle.left(90)
Murdle.forward(15)
Murdle.left(90)
Murdle.forward(15)
Murdle.left(90)
Murdle.forward(15)
Murdle.up()
Murdle.forward(15)
Murdle.end_fill()

#Murdle runs away because he's caught doing graffiti
Murdle.forward(500)
Murdle.hideturtle()


#stops waiting for new commands and allows you to close out the window
done()
