import random
# intoduction(name)
guessesTaken = 0
guess = 10
print('Hello,What is your name?')
myName = input()
# asking input(no.between 1,20)
number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')
# taking guess(too high or low)
while guessesTaken < 6:
    print('Take a guess')
    guess = input()

    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess > number:
        print('Your guess is too high')
    elif guess < number:
        print('Your guess is too low')
    else:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' +
        guessesTaken + ' guesses!!')
        break
# if no. is not equal to (gives the correct number)
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
