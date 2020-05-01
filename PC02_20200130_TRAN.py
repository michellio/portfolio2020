#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# PC02 

# MICHELLE TRAN

#

# 02/05/2020

# Description - This draws a lily pad and then a rainbow flower

@author: Michelle
"""

from turtle import *
dow = Screen() #name screen dow
dow.bgcolor("blue") #changes screen to blue represents water

lit = Turtle()
lit.speed(-10) #sets speed
lit.shape("circle")#makes lilypad a circle

#green part of animation *ABSTRACT LEAF/lilypad
lit.color(57.0/255,255.0/255,20/255.0) #set lilypad outline color
for i in range(50):
    lit.fillcolor(3.0/255,125.0/255,80/255.0) #set inside lilypad color
    lit.begin_fill() #fill lilypad with color
    lit.circle(3*i) #makes lily pad grow/ increases radius of circle
    lit.circle(-3*i)
    lit.left(i)
    lit.end_fill()
    lit.hideturtle()
    
#Lotus flower from top RED
bit = Turtle()
bit.shape("circle")
bit.speed(-10)
bit.color("red")
for i in range(25):
    bit.fillcolor("red")
    bit.begin_fill()
    bit.circle(200,70) #makes circle not circle but petal shape
    bit.left(110)
    bit.circle(200,70)
    bit.end_fill()
    bit.hideturtle()
    
#flower orange yellow,green
hit = Turtle()
hit.speed(-10)
hit.color("white")
colors = ["#FF7F00","#FFFF00","#00FF00"]
for x in range(15):
    hit.fillcolor(colors[x % 3]) #rotate between colors above
    hit.begin_fill()
    hit.circle(200,70)
    hit.left(110)
    hit.circle(200,70)
    hit.end_fill()
    hit.hideturtle()
    
#flower blue indigo violet
kit = Turtle()
kit.speed(-6)
kit.color("white")
colors = ["#0000FF","#4B0082","#9400D3"]
for x in range(6):
    kit.fillcolor(colors[x % 3]) #rotate between color above
    kit.begin_fill()
    kit.circle(200,70)
    kit.left(110)
    kit.circle(200,70)
    kit.end_fill()
    kit.hideturtle()
    
done()

        

    
    



