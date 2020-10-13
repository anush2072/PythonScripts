import sys

def is_prime(number):    
        is_prime = False

        for x in range(2,int(number/2)):
            if number%x == 0:
                is_prime = False
                break;
        else:
            is_prime = True

        return is_prime
        

def main():
    number = input("Hello there! \nEnter a number to see if it is prime or not :\t")
    if(number.isdigit()):
        result = is_prime(int(number))
        if(result):
            print(number + " is a prime number")
        else:
            print(number + " is NOT a prime number")                  
    else:
        print("Please try again! This time enter a valid number")
        
        


if __name__ == "__main__": main()