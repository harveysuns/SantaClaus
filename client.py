#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :  client.py    
@Contact    :  
@License    :  (C)Copyright 2020-2021
-------------------------------------
@Modify Time:  2023/12/25 08:36
@Author     :  
@Version    :  1.0
@Description :  None
"""
import turtle

# Create the canvas
canvas = turtle.Screen()
canvas.bgcolor("white")

# Create Santa Claus
santa = turtle.Turtle()
santa.shape("turtle")
santa.color("red")

# Set the initial position and speed of Santa Claus
santa.penup()
santa.goto(0, -200)
santa.pendown()
santa.speed(3)

# Draw Santa Claus's body
santa.begin_fill()
santa.circle(100)
santa.end_fill()

# Draw Santa Claus's face
santa.penup()
santa.goto(0, -100)
santa.pendown()
santa.color("white")
santa.begin_fill()
santa.circle(80)
santa.end_fill()

# Draw Santa Claus's eyes
santa.penup()
santa.goto(-30, 0)
santa.pendown()
santa.color("black")
santa.begin_fill()
santa.circle(10)
santa.end_fill()

santa.penup()
santa.goto(30, 0)
santa.pendown()
santa.begin_fill()
santa.circle(10)
santa.end_fill()

# Draw Santa Claus's nose
santa.penup()
santa.goto(0, -20)
santa.pendown()
santa.color("red")
santa.begin_fill()
santa.circle(7)
santa.end_fill()

# Draw Santa Claus's mouth
santa.penup()
santa.goto(0, -40)
santa.pendown()
santa.color("black")
santa.width(3)
santa.right(90)
santa.circle(20, 180)

# Draw Santa Claus's hat
santa.penup()
santa.goto(-80, 0)
santa.pendown()
santa.color("red")
santa.begin_fill()
santa.goto(80, 0)
santa.goto(0, 180)
santa.goto(-80, 0)
santa.end_fill()

# Draw Santa Claus's hat trim
santa.penup()
santa.goto(-80, 0)
santa.pendown()
santa.color("white")
santa.width(5)
santa.goto(80, 0)

# Draw Santa Claus's hat pom-pom
santa.penup()
santa.goto(0, 180)
santa.pendown()
santa.color("white")
santa.begin_fill()
santa.circle(15)
santa.end_fill()

# Draw Santa Claus's beard
santa.penup()
santa.goto(0, -80)
santa.pendown()
santa.color("white")
santa.right(180)
santa.circle(80, 180)

# Draw Santa Claus's arms
santa.penup()
santa.goto(-100, -100)
santa.pendown()
santa.color("red")
santa.width(10)
santa.goto(-200, -200)

santa.penup()
santa.goto(100, -100)
santa.pendown()
santa.goto(200, -200)

# Draw Santa Claus's hands
santa.penup()
santa.goto(-200, -200)
santa.pendown()
santa.color("white")
santa.begin_fill()
santa.circle(20)
santa.end_fill()

santa.penup()
santa.goto(200, -200)
santa.pendown()
santa.begin_fill()
santa.circle(20)
santa.end_fill()

# Draw Santa Claus's boots
santa.penup()
santa.goto(-100, -200)
santa.pendown()
santa.color("black")
santa.width(10)
santa.goto(-100, -250)

santa.penup()
santa.goto(100, -200)
santa.pendown()
santa.goto(100, -250)

# Draw Santa Claus's belt
santa.penup()
santa.goto(-120, -100)
santa.pendown()
santa.color("black")
santa.width(10)
santa.goto(120, -100)

santa.penup()
santa.goto(-120, -120)
santa.pendown()
santa.goto(120, -120)

# Draw Santa Claus's buckle
santa.penup()
santa.goto(-20, -120)
santa.pendown()
santa.color("yellow")
santa.begin_fill()
santa.goto(20, -120)
santa.goto(20, -140)
santa.goto(-20, -140)
santa.goto(-20, -120)
santa.end_fill()

# Hide the turtle
santa.hideturtle()

# Keep the canvas window open
turtle.done()
