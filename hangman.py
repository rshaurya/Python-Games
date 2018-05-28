import random

HANGMANPICS = ['''
  +---+
    |
    |
    |
    ===''','''
    +---+
    0  |
       |
       |
      ===''','''
    +---+
    0  |
    |  |
       |
      ===''','''
      +---+
      0  |
     /|  |
         |
        ===''','''
        +---+
        0  |
       /|\ |
           |
          ===''','''
          +---+
          0  |
         /|\ |
         /   |
            ===''','''
            +---+
            0  |
           /|\ |
           / \ |
              ===''']


words = 'ant boboon badger bat beaver cat clam camel cobra cougar coyote deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole newt otter owl panda parrot pigeon python rabbit ram rat rhaven rhino salmon seal shark sheep snunk sloth spider snake stork swan tiger toad trout turkey weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end='')
    for letter in missedLetters:
        print(letter, end='')
        print()

        blanks = '_' * len(secretWord)

        for i in range(len(secretWord)):
            if secretWord[i] in correctLetters:
                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks:
            print(letter,end='')
            print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')


print('<<<<<< H A N G M A N >>>>>>')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameisDone = False


while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes!The secret word is "' + secretWord + '"! You have won!')
            gameisDone = True
        else:
           missedLetters = missedLetters + guess

           if len(missedLetters) == len(HANGMANPICS)-1:
               displayBoard(HANGMANICS,missedLetters,correctLetters,secretWord)
               print('You have run out of guesses!\nAfter' + str(len(missedLetters)) +'missed guesses and' +str(len(correctLetters)) +'correct guesses,the word was "' + secretWord + '"')
               gameisDone = True

        if gameisDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameisDone = False
                secretWord = getRandomWord(words)
            else:
                break