#Kartiki Sharma
#Game
import random
from qa import *
question_number = 0
right = 0
wrong = 0   

#Intro Screen
print "Welcome to Canadian Trivia!"
print "Game Designed by: Kartiki Sharma"
play = raw_input("Do you want to play? y/n ")
fo = open ('highscore.txt', 'r+')
highscore = fo.read()
print "The current highscores have been made by:\n %s" % highscore

if play == "y":
    print "Trivia will be of 5 questions. Make sure your answer is spelled correctly and matches one of the options. One point will be awarded for a right answer. A highscore will be made with 5 points."
    name = raw_input("Please enter your name: ")

#Questions: **Omit repeating random number
while play == "y":
    question_number = random.randint(0,19)
    print qlist[question_number]

    answer = raw_input("What is your answer? ")
    if answer == alist[question_number]:
        print "Correct answer!"
#right score variable
        right = right + 1
        print "You scored %d point(s)" % right

    else:
        print "Incorrect answer!"
#wrong score variable
        wrong = wrong + 1 

#after 5 questions    
    if right + wrong == 5:
        print "You answered all your 5 questions! Your final score is %d points. You got %d question(s) wrong." % (right, wrong)  
        if right == 5:
            print "New highscore made by %s" % name
            fo.write(name)
            fo.close()

#**save results to a file
        play = raw_input ("Do you want to play again? y/n ")
        right = 0
        wrong = 0

#If n is pressed

print "Thanks for playing."
