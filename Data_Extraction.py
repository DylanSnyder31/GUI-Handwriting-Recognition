import numpy as np
from PIL import Image
from Algorithm import KNN_algorithm

class data_manipulation():

    def convert_image_to_array(self, window, training_data, training_labels, bottom_button, middle_button, third_button, top_button):
        algo = KNN_algorithm()

        #Opens up the resized image that was created by the user (dimensions are 28x28)
        resize = Image.open('Handwriting Data\Input/transform.png')
        #Converts the image to a numpy array
        array_of_image = np.array(resize.getdata(), np.uint8).reshape(resize.size[1], resize.size[0], 3)

        #Same thing as when new data was being created;
        #The numpy array is (28,28,3) and we want to bring the dimensions to (784,), so it matches the MNIST dataset
        image_new = []
        for i in array_of_image:
            for ii in i:
                #This will append one digit to our new array
                #After iteration through array_of_image, an array with size (784,) will be created
                image_new.append(ii[0])

        #Feeds the new array into the classifier
        neighbor = algo.neighbors(training_data, training_labels, image_new, 3)
        algo.confidence(neighbor, bottom_button, middle_button, third_button, top_button)
        
    def main(self, window, training_data, training_labels, testing_data, testing_labels):
        data_extraction = data_manipulation()
        data_extraction.convert_image_to_array(window, training_data, training_labels)
