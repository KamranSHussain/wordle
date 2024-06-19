
import random
import wordle

allwords = wordle.words

#Game info and score variables
tries = []
loses = 0

#Key
print("KEY")
print("* = letter is in the correct position")
print("? = letter exists in the wordle")
print()
print()

#Loop to repeat the game
while True:

    #randomly select wordle
    select = random.randint(1,12962)

    wordle = allwords[select].upper()

    #Header
    print("            WORDLE            ")
    print("------------------------------")

    #variable to store guesses
    guesslist = []

    #loop to make guesses
    while True:
        #prompt user for first guess
        guess = (input("Guess the word: ")).upper()

        #reprompt if invalid
        while True:
            if len(guess) != 5:
                print("You must enter a 5 letter word.")
                guess = (input("Guess the word: ")).upper()
                continue
            if guess.lower() not in allwords:
                print("Invalid word.")
                guess = (input("Guess the word: ")).upper()
                continue
            if guess.lower() in allwords and len(guess) == 5:
                break

        print()


        #Create list
        guessstring = [guess[0], guess[1], guess[2], guess[3], guess[4]]
        wordlelist = [wordle[0], wordle[1], wordle[2], wordle[3], wordle[4]]

        guesseval = ""

        #eval guess
        for x in range(5):
            #if word in right position
            if guessstring[x] == wordlelist[x]:
                guesseval += format(guessstring[x] + '*', '<3s')

            #if word is wrong position
            elif guessstring[x] in wordlelist:
                guesseval += format(guessstring[x] + '?', '<3s')

            #if doesnt exist
            else:
                guesseval += format(guessstring[x], '<3s')

        #Store guesses
        guesslist.append(guesseval)

        #print guesses
        for y in range(len(guesslist)):
            print(guesslist[y])

        #if user guesses the wordle
        if guess == wordle:
            #store num of tries
            tries += [len(guesslist)]
            print()
            print("Correct! The Wordle is", wordle)
            print("You guessed the Wordle in", len(guesslist), "tries")
            break

        #if user doesn't guess
        elif len(guesslist) == 6:
            #store num of tries and lose
            loses += 1
            print()
            print("Sorry, you did not guess the Wordle. The Wordle is", wordle)
            break

    #Ask user to replay
    print()
    replay = (input("Do you want to play again? (Y) or (N) ")).upper()
    
    #check if answer is invalid
    while replay != 'Y' and replay != 'N':
        print("Invalid response.")
        replay = (input("Do you want to play again? (Y) or (N) ")).upper()

    if replay == "N":
        break

    elif replay == "Y":
        print()
            
#print score info
print()
#Print Highscore and Average
scoresum = 0

if len(tries) == 0:
    print("High Score: 0")
    print("Average Score: 0")

else:
    print("High Score:", min(tries))

    for x in tries:
        scoresum += x
    print("Average Score:", format(scoresum/len(tries), '.2f'))

#Print loses
print("Number of lost games:", loses)
