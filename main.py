import copy
import math

def main():
    print('Welcome to the Feature Selection Algorithm!')
    fileName = input('\nType in the name of the file to test: ')
    userData = open(fileName, 'r')
    inputRead= userData.readline()
    #https://www.guru99.com/python-file-readline.html#:~:text=Python%20readline()%20method%20reads,will%20return%20you%20binary%20object.
    totalFeatures = len(inputRead.split()) - 1
    totalInstances = sum(1 for line in userData)
    #https://pynative.com/python-count-number-of-lines-in-file/
    instances = []
    for i in range(totalInstances):
        instances.append([]) #we need to populate instances with lists that 
    for i in range(totalInstances):
        instances[i] = [float(j) for j in userData.readline().split()]
        #This is converting all of the values in the data file to float so we cann take it in.

    mainAccuracy = leave_one_out_cross(instances, totalFeatures, totalInstances)

    print("Please enter which alogithm you would like to use\n")
    print("1). Forward Selection\n")
    print("2). Backward Elimination\n")
    userChoice = int(input())
    if userChoice == 1:
        forwardSearch(instances,totalFeatures, totalInstances)
    elif userChoice == 2:
        backwardSearch(instances, totalFeatures, totalInstances)
    elif ((userChoice >= 0) or (userChoice > 3)):
        print("Error, made the wrong choice, Please Re-enter an appropriate choice")
        userChoice = int(input())


#Using Professors PseudoCode
def leave_one_out_cross(instancesD, totalF, totalI):
    correct = 0.0
    distance = 0
    for i in range(totalI):
        nb = 0
        nb_shortest = float('inf')
        for j in range(len(totalF)):
            distance = distance + pow((instancesD[i][totalF[j]] - instancesD[i][totalF[j]]),2 )
            distance = math.sqrt(distance)
            if distance < nb_shortest:
                nb_shortest = distance
                nb = i
        if instancesD[nb][0] == instancesD[i][0]:
            correct += 1
    accuracy = (correct / totalF) * 100
    return accuracy 
#Due to the professor pseudoCode rough translation we do not need the nearest neighbor as we have already implemented within the above function
def forwardSearch(instancesD, instances, features):
    usedSubset = [] #subset used so we dont rerun things 
    finalSet = [] #What the user wants to see
    bestAccuracy = 0.0
    for i in range(features):
        adding = 0
        localAccuracy = 0.0
        for j in range(1, features + 1):
            if j not in usedSubset:
                copy_subset = copy.deepcopy(usedSubset)
                copy_subset.append(j)
                accuracy = leave_one_out_cross(data, copy_subset, instances)
                if accuracy > bestAccuracy:
                    bestAccuracy = accuracy
                    localAccuracy = accuracy
                    adding = j
        if adding > 0:
            usedSubset.append(adding)
            finalSet.append(adding)
        else:
            usedSubset.append(adding)
        print ('\n\nFeature set ', usedSubset, ' was best, accuracy is ', bestAccuracy, '%\n\n')
    
    print("Finished the search. The best subset is",usedSubset, "which has an accuracy of: ", bestAccuracy)

def backwardSearch(data, instances, userSubset):
    subset = []
    finalSet = []
    bestAccuracy = leave_one_out_cross(data, userSubset, instances)
    for i in range(1, userSubset):
        subset.append[i]
    for i in range(1,userSubset):
        finalSet.append[i]
    for i in range(instances):
        delete = 0
        localAccuracy = 0
        for j in range(1, userSubset + 1):
            if j in userSubset:
                copy_subset = copy.deepcopy(userSubset)
                copy_subset.remove(j)
                accuracy = leave_one_out_cross(data, copy_subset, instances)
                print ('Using feature(s) ', copy_subset, ' accuracy is ', accuracy)

                if accuracy > bestAccuracy:
                    bestAccuracy = accuracy
                    if accuracy>localAccuracy:
                        localAccuracy = accuracy
                    delete = j
            finalSet.remove(delete)

if __name__ == '__main__':
	main()