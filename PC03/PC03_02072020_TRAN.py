#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# PC03 Generative Art

#

# TRAN

#

# 02/19/2020

# Description - snow falling generative art- this is inspired by the randomness of snow fall
with "snow" being drawn at random locations, colors, and widths- so every time you run this program
it's different and unique!
@author: Michelle
"""
#import necessities
from turtle import *
from random import *
import turtle, random 

#make screen tings
win = Screen()
win.bgcolor("black")
win.update()

#name turtle
jj = Turtle()

for j in range(25):
    colors  = ["#9381FF","#B8B8FF","#F8F7FF","#FFEEDD","#BFDBF7","#E4FF1A","#FBFBFF","#FF958C","#FF5376"] 
    jj.width(random.randint(1, 4)) #changes width
    jj.speed("fastest") #make speed fast
    
    length = 7 #set length
    
    jj.shape('turtle')
    jj.penup() #picks the pen up 
    jj.goto((randint(-300,300)),(randint(-300,300))) #rando location on win
    jj.pendown() #puts pen down to draw
        
    
    for count in range(28):
        color = random.choice(colors) #pics rando colors from list above
        jj.forward(length)
        jj.right(135)
        jj.color(color)
        length = length + 5 #increase by 5 everytime
    
    jj.forward(48)
    jj.hideturtle()
    
done()
        
        
