##########
# The Friendship Algorithm
# Dr. Sheldon Cooper, Ph.D.
# Adapted for Python by Jacob Turner
##########

import random
import time

raw_input("Press any key to place a phone call")
print
athome = random.randint(0, 1)
if athome == 0:
    print 'Not at home - leaving message...'
    print
    waittime = random.randint(1, 3)
    time.sleep(waittime)
print "*phone is answered*"
raw_input("Would you like to share a meal? (press any key)")
hunger = random.randint(0, 1)
waittime = random.randint(1, 3)
time.sleep(waittime)
if hunger == 0:
    print "The answer is No"
    print
    print "Do you enjoy a hot beverage?"
    earlgrey = random.randint(0, 1)
    waittime = random.randint(1, 3)
    time.sleep(waittime)
    if earlgrey == 0:
        print "The answer is No"
        n = 0
        while n < 6:
            print
            print "Recreational activity? Tell me one of your interests."
            shared = random.randint(0, 1)
            waittime = random.randint(1, 3)
            time.sleep(waittime)
            if shared == 0:
                print "*interest is not shared*"
                n += 1
            elif shared == 1:
                print "*interest is shared*"
                print "Why don't we do that together?"
                print "*partake in interest*"
                break
        if n >= 6:
            print "*chooses least objectionable interest*"
            print "*partake in interest*"
    elif earlgrey == 1:
        print 'The answer is Yes'
        drinks = ["Tea", "Coffee", "Cocoa"]
        drink = random.randint(0, 2)
        waittime = random.randint(1, 3)
        time.sleep(waittime)
        print "The person prefers" + drinks[drink]
        print "*have " + drinks[drink] + "*"
elif hunger == 1:
    print "The answer is Yes"
    print "*dine together*"
print
raw_input("BEGIN FRIENDSHIP!")