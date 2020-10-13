import sys

def is_palindrome(word):    
        letters = list(word)
        is_palindrome = True

        for letter in letters:
            if letter == letters[-1]:
                letters.pop(-1)
            else:
                is_palindrome = False
            break

        return is_palindrome
        

def main():
    print("Hello there!")
    if(len(sys.argv) == 2):
        result = is_palindrome(sys.argv[1])
        if(result):
            print(sys.argv[1] + " is a palindrome")
        else:
            print(sys.argv[1] + " is NOT a palindrome")                  
    else:
        print("Please try again! This time enter a valid string argument")
        
        


if __name__ == "__main__": main()
