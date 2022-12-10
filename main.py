import copy
import math

def main():
    print('Welcome to the Feature Selection Algorithm!')
    fileName = input('\nType in the name of the file to test: ')
    userData = open(fileName, 'r')
    totalFeatures = len(next(userData))
    totalInstances = sum(1 for line in userData)
    instances = []
    for i in range(totalInstances):
        instances[i] = [float(j) for j in userData.readline().split()]
    
    mainAccuracy = leave_one_out_cross(instances, totalFeatures, totalInstances)

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
def leave_one_out_cross(data, current_set, feature_to_add):
    for i in range(feature_to_add):
        object_classify = data[i][current_set]
        label_classify = data[i][1]
        nb_distance = float('inf')
        nb_location = float('inf')
        for j in range(len(current_set)):
            distance = 0
            if(i != j):
                distance = math.sqrt(math.sum(math.pow((object_classify - data[j][1:i], 2))))
                if distance <= nb_distance:
                    nb_distance = distance
                    nb_location = j
                    nb_label = data[nb_location - 1][0]  
        if label_classify == nb_label:
            corr_classified =+ 1  
    accuracy = (corr_classified/current_set) * 100
    return accuracy
#Due to the professor pseudoCode rough translation we do not need the nearest neighbor as we have already implemented within the above function
def forwardSearch(data, instances, features):
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
    
    print("Finished the search. The best subset is",usedSubset, "which has an accuracy of: ", bestAccuracy)

            
def backwardSearch(data, instances, subset, acc):

    
    return 0

if __name__ == '__main__':
	main()