"""
Programmer: Andrew Vinals
Project: The Aquarius Constellation Project
Date: 11/9/2022
"""
#imported turtle and time 
import turtle 
import time

turtle.Turtle()
window = turtle.Screen()
window.setup (width=1.0, height=1.0, startx=0, starty=0)
turtle.pensize(1)
turtle.shape("turtle")
turtle.hideturtle()

#This function shows the splash page 
def firstPage():
    turtle.color('blue')
    turtle.penup()
    turtle.goto(-400,100)
    turtle.pendown()
    turtle.right(90)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.write("The Aquarius Constellation", font=("Verdana",50,'bold'),align='center')
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.write("by Andrew Vinals", font=("Courier",30,'italic'),align='center')
    
firstPage()

time.sleep(2)#page will be displayed for 2 seconds
turtle.clear()#this clears the window

#This function displays the second page 
def secondPage():
    window.bgpic('aquarius.gif')
    turtle.color('white')
    time.sleep(2)
secondPage()

window.clear()

#constellation appears in white background
def thirdPage():
   
    
    turtle.bgcolor('white')
    turtle.color('black')
    turtle.penup()
    turtle.fd(300)
    turtle.right(100)
    turtle.fd(-200)
    
    
    turtle.pendown()
    

    #main diagram begins
    turtle.write("     Albali")
    turtle.dot(18)
    turtle.right(40)
    turtle.dot(12)
    turtle.left(-10) 
    turtle.fd(70)
    turtle.dot(12)
    turtle.left(-70) 
    turtle.fd(100)
    turtle.write("  SadaIsuud")
    turtle.dot(18)
    turtle.goto(90, 275)
    turtle.write("  Sadalmelik")
    turtle.dot(18)
    turtle.goto(80, 210)
    turtle.write("  Ancha")
    turtle.dot(18)
    turtle.goto(100, 180)
    turtle.bk(5)
    turtle.dot(12)
    turtle.goto(125, 150) # End point of Ancha
    turtle.dot(12)
    turtle.penup()
    turtle.right(35)
    turtle.fd(129)
    turtle.pendown()
    turtle.dot(12)
    turtle.left(100)
    turtle.fd(40)
    turtle.write("   Sadalachbia")
    turtle.dot(18)
    turtle.right(60)
    turtle.fd(30)
    turtle.right(70)
    turtle.fd(10)
    turtle.dot(7)
    turtle.bk(10)
    turtle.left(110)
    turtle.fd(10)
    turtle.dot(7)
    turtle.penup()
    turtle.left(150)
    turtle.fd(38)
    turtle.dot(7)
    turtle.pendown()
    turtle.right(111)
    turtle.fd(40)
    turtle.write("     Situla")
    turtle.dot(18)
    turtle.left(9)
    turtle.fd(40)
    turtle.dot(12)
    turtle.left(50)
    turtle.fd(40)
    turtle.dot(12)
    turtle.right(30)
    turtle.fd(20)
    turtle.write("     Skat")
    turtle.dot(18)
    turtle.fd(60)
    turtle.dot(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.dot(10)
    turtle.right(5)
    turtle.fd(35)
    turtle.right(60)
    turtle.fd(20)
    turtle.dot(10)
    turtle.right(40)
    turtle.fd(50)
    turtle.dot(10)
    turtle.left(40)
    turtle.fd(30)
    turtle.dot(10)
    turtle.right(95)
    turtle.fd(54)
    turtle.penup()
    # Writing the Logo
    turtle.goto(-500,-150)
    turtle.write("The Aquarius Constellation",font=("Courier",10,'italic'))

thirdPage()
time.sleep(2)
window.clear()

#In this function the dots appears before and the lines get connected after wards
def forthPage():
    window.delay(3)
    turtle.speed('slow')
    turtle.color('white')
    window.bgpic("galaxyGIF.gif")

    #21
    turtle.penup()
    turtle.goto(300,0)
    turtle.dot(10)
    turtle.write("  Albali", font=("Calibri", 10, "normal"), align="left")
    turtle.up()

    #19
    turtle.goto(200,-40)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    

    #4
    turtle.goto(120,40)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    turtle.write("  SadaIsuud", font=("Calibri", 10, "normal"), align="left")

    #5
    turtle.goto(30,140)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    turtle.write("  Sadalmelik", font=("Calibri", 10, "normal"), align="left")

    #13
    turtle.goto(10,-40)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    turtle.write("  Ancha", font=("Calibri", 10, "normal"), align="left")

    #15
    turtle.goto(70,-150)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    # turtle.write(" Iota Aquarii", font=("Calibri", 10, "normal"), align="left")

    

    #5
    turtle.goto(30,140)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #10
    turtle.goto(-20,120)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #7
    turtle.goto(-40,140)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #11
    turtle.goto(-70,150)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    

    #7
    turtle.goto(-40,140)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #20
    turtle.goto(-20,160)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    

    #10
    turtle.goto(-20,120)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    turtle.write("  Sadachbia", font=("Calibri", 10, "normal"), align="left")

    #25
    turtle.goto(-50,70)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    turtle.write("  Situla", font=("Calibri", 10, "normal"), align="left")

    #8
    turtle.goto(-120,-10)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #12
    turtle.goto(-110,-100)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #6
    turtle.goto(-120,-130)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    turtle.write("  Skat", font=("Calibri", 10, "normal"), align="left")

    #blank1
    turtle.goto(-150,-220)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #blank2
    turtle.goto(-190,-210)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #blank3
    turtle.goto(-270,-190)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #18
    turtle.goto(-265,-145)
    turtle.pd()
    turtle.dot(10)
    turtle.up()
    

    #23
    turtle.goto(-260,-135)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #16,17,24
    turtle.goto(-200,-40)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #14
    turtle.goto(-190,0)
    turtle.pd()
    turtle.dot(10)
    turtle.up()

    #8
    turtle.goto(-120,-10)
    turtle.pd()
    turtle.dot(10)
    turtle.up()


    #21
    turtle.up()
    turtle.goto(300,0)
    turtle.pd()

    #19
    turtle.goto(200,-40)

    #4
    turtle.goto(120,40)

    #5
    turtle.goto(30,140)

    #13
    turtle.goto(10,-40)

    #15
    turtle.goto(70,-150)
    turtle.up()

    #5
    turtle.goto(30,140)
    turtle.pd()

    #10
    turtle.goto(-20,120)

    #7
    turtle.goto(-40,140)

    #11
    turtle.goto(-70,150)
    turtle.up()

    #7
    turtle.goto(-40,140)
    turtle.pd()

    #20
    turtle.goto(-20,160)
    turtle.up()

    #10
    turtle.goto(-20,120)
    turtle.pd()

    #25
    turtle.goto(-50,70)

    #8
    turtle.goto(-120,-10)

    #12
    turtle.goto(-110,-100)

    #6
    turtle.goto(-120,-130)

    #blank1
    turtle.goto(-150,-220)

    #blank2
    turtle.goto(-190,-210)

    #blank3
    turtle.goto(-270,-190)

    #18
    turtle.goto(-265,-145)

    #23
    turtle.goto(-260,-135)

    #16,17,24
    turtle.goto(-200,-40)

    #14
    turtle.goto(-190,0)

    #8
    turtle.goto(-120,-10)
forthPage()
time.sleep(2)

window.clear()
