import copy
import math
import numpy

def main():
    print('Welcome to the Feature Selection Algorithm!')
    fileName = input('\nType in the name of the file to test: ')
    userData = open(fileName, 'r')

    print("Please enter which alogithm you would like to use\n")
    print("1). Forward Selection\n")
    print("2). Backward Elimination\n")
    userChoice = int(input())
    if userChoice == 1:
        forwardSearch()
    elif userChoice == 2:
        backwardSearch()
    elif ((userChoice >= 0) or (userChoice > 3)):
        print("Error, made the wrong choice, Please Re-enter an appropriate choice")
        userChoice = int(input())
     

def forwardSearch():
    return 0
def backwardSearch():
    return 0


if __name__ == '__main__':
	main()