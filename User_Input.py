from PIL import Image
import os
from resizeimage import resizeimage
from Algorithm import KNN_algorithm

class image_saving():

    def __init__(self):
        pass

    def resize_image(self, event=None):
        algo = KNN_algorithm()

        #Where the .png is stored
        filename = "Handwriting Data\Input\input.png"

        #This resizes the image from it's original state to a 28x28 image;
        #28x28 is the same size as the MNISt dataset
        with open(filename, 'r+b') as file:
            with Image.open(file) as image:
                resize = resizeimage.resize_cover(image, [28, 28])

        #Removes the large picture becasue it isn't needed
        os.remove("Handwriting Data\Input\input.png")
        #Saves the resized image
        resize.save('Handwriting Data\Input/transform.png',  image.format)

        #Feeds the new and resized image into the classifier
        neighbor = algo.neighbors(training_data, training_labels, image_new, 7)

        return resize


    ############################################################################
    ############   UNCOMMENT THIS IF YOU WANT TO MAKE CUSTOM DATA   ############
    ############################################################################

    '''
    def save_user_input(resize):

        #This gets the resized image into a Numpy Array
        resized_array = np.array(resize.getdata(), np.uint8).reshape(resize.size[1], resize.size[0], 3)

        #This takes the resized_array as input and output an array that is sized (784,); the same format as the MNIST dataset
        #This code is needed because resized array is sized as (28,28,3)

        finished_array = []
        for i in resized_array:
            for ii in i:
                #Appending the first index is important because the file is structured as an array with length 3, all the same number;
                #example: [1,1,1]. This is unnecessary so to reduce the array to one number we take the first index of the array
                finished_array.append(ii[0])

        #Makes finished_array into a numpy array
        finished_array = np.array(finished_array)

        return finished_array




    def custom_data(finished_array):
        #This function is if the user wants to make custom data;
        ##This is how the custom English Character Data was made

        #Splits the data into test (1/5 of the time) and training (4/5 of the time)

        if number % 5 != 0:
            ###
            #The training data
            ###
            #Opens the file
            MNIST_training_data = open('Handwriting Data\MNIST Data (Digits)/mnist_train_data.csv', 'a')
            with MNIST_training_data as file:
                writer = csv.writer(file)
                #Writes the size (784,) array into a new row, in the CSV
                writer.writerow(finished_array)
            #Closes the file
            MNIST_training_data.close()

            #Now to add the label to the correct file;
            #Does the same thing as appending the data
            MNIST_training_labels = open('Handwriting Data\MNIST Data (Digits)\mnist_train_labels.csv', 'a')
            with MNIST_training_labels as file:
                writer = csv.writer(file)
                writer.writerow(11) #put the number that corrisponds to the correct letter that you are making the data for
            MNIST_training_labels.close()
        else:
            ###
            #The testing data
            ###
            #opens up the MNIST testing data that was converted into a CSV
            MNIST_test_data = open('Handwriting Data\MNIST Data (Digits)\mnist_test_data.csv', 'a')
            with MNIST_test_data as file:
                writer = csv.writer(file)
                #Writes the size (784,) array into a new row, in the CSV
                writer.writerow(finished_array)
            #Closes the MNIST data; it has one more row than it started out with
            MNIST_test_data.close()


            This does the same thing, but with the labels
            It opens up the file,
            writes the labels (hard-coded in),
            and closes the file

            MNIST_test_labels = open('Handwriting Data\MNIST Data (Digits)\mnist_test_labels.csv', 'a')
            with MNIST_test_labels as file:
                writer = csv.writer(file)
                writer.writerow(11) #put the number that corrisponds to the correct letter that you are making the data for
            MNIST_test_labels.close()
    '''

    def main(self, window, drawing_canvas, training_data, training_labels, testing_data, testing_labels):
        #Calls the function
        user_input = image_saving()
