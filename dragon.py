import random
import time

# displayIntro function definition


def displayIntro():
    print('You are in a land full of dragons.In front of you')
    print('You see two caves in front of you.In one cave, \
        the dragon is friendly')
    print('and will share his treasure.The other dragon')
    print('is greedy and hungry,and will eat you on sight')
    print()

# choosecave function definition


def chooseCave():
    cave = ""
    while cave != 1 and cave != 2:
        print('Which cave will you go into?(1 or 2)')
        cave = input()
        # print cave, type(cave)

    return cave

# checkCave function definition


def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A scary dragon comes in front of you.He opens his jaws and...')
    print()
    time.sleep(2)
    friendlyCave = random.randint(1, 2)
    # print chosenCave, type(chosenCave), friendlyCave, type(friendlyCave)
    if chosenCave == friendlyCave:
        print('Gives you his treasure')
    else:
        print('Gobbles you in one bite!')

#  variable and function call, while loop
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again?(yes or no)')
    playAgain = input()