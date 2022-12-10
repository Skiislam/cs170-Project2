import copy
import math
import numpy
import pandas as pd

def main():
    print('Welcome to the Feature Selection Algorithm!')
    fileName = input('\nType in the name of the file to test: ')
    userData = pd.read_csv(fileName, delimiter=" ")
    totalFeatures = len(next(userData))
    totalInstances = sum(1 for line in userData)
    instances = []
    for i in range(totalInstances):
        instances[i] = [float(j) for j in userData.readline().split()]

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


#Using Professors PseudoCode
def leave_one_out_cross(data, current_set, feature_to_add, length):
    for i in range(len(data)):
        object_classify = data[i][2:length]
        label_classify = data[i][1]
        nb_distance = float('inf')
        nb_location = float('inf')
        for j in range(len(data)):
            distance = 0
            if(i != j):
                distance = math.sqrt(math.sum(math.pow((object_classify - data[j][1:length], 2))))
                if distance <= nb_distance:
                    nb_distance = distance
                    nb_location = j
                    nb_label = data[nb_location - 1][0]  
        if label_classify == nb_label:
            corr_classified =+ 1  
    accuracy = corr_classified/len(data)
    return accuracy
#Due to the professor pseudoCode rough translation we do not need the nearest neighbor as we have already implemented within the above function
def forwardSearch(data, instances, subset):
    return 0
def backwardSearch(data, instances, subset):
    return 0


if __name__ == '__main__':
	main()