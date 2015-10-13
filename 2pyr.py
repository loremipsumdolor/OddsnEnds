##########
# 2PyR - Math tutoring program written in Python
# Code by Jacob Turner
# Released under the MIT license
###########

import random

def add(level, num):
    while True:
        inc = 0
        cor = 0
        if level == 1:
            end = 10
        elif level == 2:
            end = 50
        elif level == 3:
            end = 100
        for x in range(int(num)):
            a = random.randint(1, end)
            b = random.randint(1, end)
            add = raw_input("What is " + str(a) + " + " + str(b) + "? ")
            if not add.isdigit():
                add = 0
            ab = a + b
            if ab != int(add):
                print "Incorrect."
                print str(a) + " + " + str(b) + " = " + str(ab)
                inc += 1
            else:
                print "Correct!"
                cor += 1
        print str(float(cor) / int(num))
        percent = str(float(cor) / float(num) * 100).partition(".")[0]
        print "You made a " + percent + " percent."
        print "(" + str(cor) + " correct, " + str(inc) + " incorrect)"
        yn = raw_input("Would you like to do more problems (yes)? ")
        if yn == "yes" or "":
            pass
        else:
            break

def sub(level, num):
    while True:
        inc = 0
        cor = 0
        if level == 1:
            end = 10
        elif level == 2:
            end = 50
        elif level == 3:
            end = 100
        for x in range(int(num)):
            while True:
                a = random.randint(1, end)
                b = random.randint(1, end)
                if a >= b:
                    break
                else:
                    pass
            sub = raw_input("What is " + str(a) + " - " + str(b) + "? ")
            if not sub.isdigit():
                sub = 0
            ab = a - b
            if ab != int(sub):
                print "Incorrect."
                print str(a) + " - " + str(b) + " = " + str(ab)
                inc += 1
            else:
                print "Correct!"
                cor += 1
        percent = str(float(cor) / float(num) * 100).partition(".")[0]
        print "You made a " + percent + " percent."
        print "(" + str(cor) + " correct, " + str(inc) + " incorrect)"
        yn = raw_input("Would you like to do more problems (yes)? ")
        if yn == "yes" or "":
            pass
        else:
            break

def mult(level, num):
    while True:
        inc = 0
        cor = 0
        if level == 1:
            end = 10
        elif level == 2:
            end = 50
        elif level == 3:
            end = 100
        for x in range(int(num)):
            a = random.randint(1, end)
            b = random.randint(1, end)
            mult = raw_input("What is " + str(a) + " x " + str(b) + "? ")
            if not mult.isdigit():
                mult = 0
            ab = a * b
            if ab != int(mult):
                print "Incorrect."
                print str(a) + " * " + str(b) + " = " + str(ab)
                inc += 1
            else:
                print "Correct!"
                cor += 1
        percent = str(float(cor) / float(num) * 100).partition(".")[0]
        print "You made a " + percent + " percent."
        print "(" + str(cor) + " correct, " + str(inc) + " incorrect)"
        yn = raw_input("Would you like to do more problems (yes)? ")
        if yn == "yes" or "":
            pass
        else:
            break

def div(level, num):
    while True:
        inc = 0
        cor = 0
        if level == 1:
            end = 20
        elif level == 2:
            end = 50
        elif level == 3:
            end = 100
        for x in range(int(num)):
            while True:
                a = random.randint(1, end)
                b = random.randint(1, end)
                if float(a) / b == float(a / b):
                    break
                else:
                    pass
            div = raw_input("What is " + str(a) + " / " + str(b) + "? ")
            if not div.isdigit():
                div = 0
            ab = a / b
            if ab != int(div):
                print "Incorrect."
                print str(a) + " / " + str(b) + " = " + str(ab)
                inc += 1
            else:
                print "Correct!"
                cor += 1
        percent = str(float(cor) / float(num) * 100).partition(".")[0]
        print "You made a " + percent + " percent."
        print "(" + str(cor) + " correct, " + str(inc) + " incorrect)"
        yn = raw_input("Would you like to do more problems (yes)? ")
        if yn == "yes" or "":
            pass
        else:
            break

while True:
    print "Welcome to 2PyR!"
    print "Which would you like to work on?"
    print "1 - Addition"
    print "2 - Subtraction"
    print "3 - Multiplication"
    print "4 - Division"
    probs = raw_input("> ")
    if probs.isdigit() and 1 <= int(probs) <= 4:
        probs = int(probs)
    else:
        print "Invalid answer. Exiting."
        break
    print "1 - Easy"
    print "2 - Medium"
    print "3 - Hard"
    lvl = raw_input("At what level do you want to practice? ")
    if lvl.isdigit() and 1 <= int(lvl) <= 3:
        lvl = int(lvl)
    else:
        print "Invalid answer. Exiting."
        break
    num = raw_input("How many problems would you like to practice? ")
    if num.isdigit():
        if probs == 1:
            add(lvl, num)
        if probs == 2:
            sub(lvl, num)
        if probs == 3:
            mult(lvl, num)
        if probs == 4:
            div(lvl, num)
    else:
        print "Invalid answer. Exiting."
        break
