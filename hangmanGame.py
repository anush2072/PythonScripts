#importing the time module
import time
import random
import sys

def getRandomWord():
    listOfWords = [ "wish", "opposite", "illegal", "ski", "yarn", "base", "blue", "squash", "melodic", "grease", "berry", "fuel", "book", 
                    "feeble", "merciful", "examine", "rampant", "greedy", "smash", "trouble", "knee", "instruct", "remember", "birthday", "digestion" ]
    # return random.sample(listOfWords, 1)
    return random.choice(listOfWords);

def hangAMan(turn):

    if turn == 7:
         print("-----\n|\n|\n|\n|\n|\n|\n|\n|\n-------\n--------")
    elif turn == 6:
        print("-----\n|   |\n|   O\n|\n|\n|\n|\n|\n|\n-------\n--------")
    elif turn == 5:
        print("-----\n|   |\n|   O\n|  -+-\n|\n|\n|\n|\n|\n-------\n--------")
    elif turn == 4:
        print("-----\n|   |\n|   O\n| (-+-\n|\n|\n|\n|\n|\n-------\n--------")
    elif turn == 3:
        print("-----\n|   |\n|   O\n| (-+-)\n|\n|\n|\n|\n|\n-------\n--------")
    elif turn == 2:
        print("-----\n|   |\n|   O\n| (-+-)\n|   |\n|\n|\n|\n|\n-------\n--------")
    elif turn == 1:
        print("-----\n|   |\n|   O\n| (-+-)\n|  (|\n|\n|\n|\n|\n-------\n--------")
    elif turn == 0:
        print("-----\n|   |\n|   O\n| (-+-)\n|  (|)\n|\n|\n|\n|\n-------\n--------")
       



def main():
    #welcoming the user
    name = input("What is your name? ")

    print("Hello, " + name + "! Time to play hangman!\n")

    #wait for 1 second
    time.sleep(1)

    #determine the number of turns
    turns = 7
    hangAMan(10)

    print("Start guessing...")
    time.sleep(0.5)

    #creates an variable with an empty value
    guesses = ''

    #here we set the secret
    word = getRandomWord()
    #print(word)

    # Create a while loop

    #check if the turns are more than zero
    while( turns > 0 ):         

        # ask the user to guess a character
        guess = input("\nGuess a character in the password :") 

        # set the players guess to guesses
        guesses += guess                    
            
        # make a counter that starts with zero
        failed = 0 

        # for every character in secret_word    
        for char in word:      

        # see if the character is in the players guess
            if char in guesses:    
                # print then out the character
                sys.stdout.write (char),    

            else:
                # if not found, print a dash
                sys.stdout.write  ("_"),     
           
            # and increase the failed counter with one
                failed += 1    

        # if failed is equal to zero
        # print You Won
        # exit the script
        if failed == 0:        
            print ("\nYou won")  
            break              

        # if the guess is not found in the secret word
        if guess not in word:  
     
         # turns counter decreases with 1
            turns -= 1  
            print("\nNumber of turn left : ", turns)
            hangAMan(turns)      
     
        # print wrong
            print( "\nWrong")

            if turns == 0:
                print("\nYou loose!")


if __name__ == "__main__": main()
