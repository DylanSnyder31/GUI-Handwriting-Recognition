import numpy as np
from collections import Counter
import math
from math import sqrt

class KNN_algorithm():
    #This class is the algorithm that was chosen; a simple K-Nearest Neighbors implementation

    #This is a euclidean distance implementation in Python
    #https://en.wikipedia.org/wiki/Euclidean_distance
    def distance(self, instance1, instance2, length):
        distance = 0
        for i in range(length):
            distance += pow((instance1[i] - instance2[i]), 2)
        return math.sqrt(distance)

    def neighbors(self, training_data,
                      training_labels,
                      input_data,
                      k):
    
        distances_from_neighbors = []
        for index in range(len(training_data)):
            #This iterates through all of the training_data
            algo = KNN_algorithm()
            length = 783
            #Calculates the distance from the new data (what the user has drawn on thw canvas), and each point in the training_data
            dist = algo.distance(input_data, training_data[index], length)
            #Appends the data point, the distance of that point, and the label of that point to distances_from_neighbors
            distances_from_neighbors.append((training_data[index], dist, training_labels[index]))
        #Sorts the array
        distances_from_neighbors.sort(key=lambda x: x[1])

        #Get the first K of the distances (The closest to the new data point)
        neighbors = distances_from_neighbors[:k]

        return neighbors



    def vote_counter(self, neighbors):
        counter = Counter()
        for neighbor in neighbors:
            #This counts how many of each different label (alphabet/ Digit) was one of the K-nearest
            counter[neighbor[2]] += 1
        #Returns the most most common neighbor
        #This means that the new image is classified as what is returned
        return counter.most_common(1)[0][0]


    def confidence(self, neighbors, bottom_button, middle_button, third_button, top_button):
        counter = Counter()

        #This is the confidence of the image being classified right
        alphabet_dict = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10: 'A', 11: 'a', 12: 'B', 13: 'b', 14: 'C', 15: 'c', 16: 'D', 17: 'd', 18: 'E', 19: 'e', 20: 'F', 21: 'f',
        22: 'G', 23: 'g', 24: 'H', 25: 'h', 26: 'I', 27: 'i', 28: 'J', 29: 'j', 30: 'K', 31: 'k', 32: 'L', 33: 'l', 34: 'M', 35: 'm',
        36: 'N', 37: 'n', 38: 'O', 39: 'o', 40: 'P', 41: 'p', 42: 'Q', 43: 'q', 44: 'R', 45: 'r', 46: 'S', 47: 's', 48: 'T', 49: 't', 50: 'U',
        51: 'u', 52: 'V', 53: 'v', 54: 'W', 55: 'w', 56: 'X', 57: 'x', 58: 'Y', 59: 'y', 60: 'Z', 61: 'z'}


        for neighbor in neighbors:
            counter[neighbor[2]] += 1

        #This gets all the labels and votes for the new image (there are K number of votes)
        labels, votes = zip(*counter.most_common())

        #This is what was returned in the vote_counter function;
        #This is what the algorithm classified the new input data as
        new_classification = counter.most_common(1)[0][0]

        #This is how many of the K-nearest 'voted' for the new classification
        number_of_votes_for_classification = counter.most_common(1)[0][1]

        '''
        This part is for the window, and displaying the probability of the classification on the buttons
        Since there are only four buttons, we can only display the top 3 "choices", or less
        '''
        bottom_button.config(text="")
        middle_button.config(text="")
        third_button.config(text="")
        top_button.config(text="")

        if len(counter) <= 3:
            length = len(counter)
            index = 0
            for i in counter:
                if index == 2:
                    middle_button.config(text="%s\n %s" %(alphabet_dict[i], str(round(counter[i]/sum(votes), 2))[1:]))
                elif index == 1:
                    third_button.config(text="%s\n %s" %(alphabet_dict[i], str(round(counter[i]/sum(votes), 2))[1:]))
                else:
                    top_button.config(text="%s \n %s" %(alphabet_dict[i], str(round(counter[i]/sum(votes), 2))[1:]))
                index += 1


        else:
            length = len(counter)
            index = 0
            while index != 4:
                for i in counter:
                    if index == 2:
                        middle_button.config(text="%s\n (%s)" %(alphabet_dict[i], str(round(counter[i]/sum(votes), 2))[1:]))
                    elif index == 1:
                        third_button.config(text="%s \n (%s)" %(alphabet_dict[i], str(round(counter[i]/sum(votes), 2))[1:]))
                    else:
                        top_button.config(text="%s \n (%s)" %(alphabet_dict[i], str(round(counter[i]/sum(votes), 2))[1:]))
                    index += 1


        #This returns the new_classification, and the percent of 'voters' that votes for it
        return new_classification, number_of_votes_for_classification/sum(votes), counter
