import tkinter as tk
from resizeimage import resizeimage
import os
from PIL import Image, ImageDraw
from User_Input import image_saving
from Data_Extraction import data_manipulation

class draw_line():

    def __init__(self):
        #Create a new canvas
        self.drawing_canvas =  tk.Canvas()
        #Create that same canvas,but only in memory this time
        #This allows to get a PNG format of the user's input
        self.memory_image = Image.new("RGB", (986, 366), (0,0,0))

    def save_image(self, drawing_canvas, list):
        #Saves the PIL image that was drawn on in memory, copied from the input on the canvas
        self.memory_image.save("Handwriting Data\Input\input.png")
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

        #Clear the old corrdinates, so a new line can be drawn
        #Without this it would be impossible to draw in more than one continuous line
        list.clear()

    def draw(self, window, training_data, training_labels, bottom_button, middle_button, third_button, top_button, list):
        list = list
        data = data_manipulation()
        draw_on_memory_image = ImageDraw.Draw(self.memory_image)

        #Places the canvas in these pixels, where the user can draw
        self.drawing_canvas.place(x=2,y=299, height = 366, width = 986)
        #Thickness of the line is set the 6 pixels, in order for the algorithm to read the image the best, and give the user the best experience
        thickness_of_line = 6

        '''
        This is the main block that will draw on the canvas, it works in a few steps.
        The first thing to note is that this repeats everytime the mouse is moving, and the left button is clicked
        '''

        #Checks to make sure that the list isn't empty (if the mouse is released the list becomes empty)
        if len(list) != 0:
            #Get the corrdinates of the mouse;

            #First it gets the corrdinates of the mouse relative to your computer screen, then subtracts the
            #corrdinates relative to the window, finally it subtracts an amout of pixels (9 for x-axis, 29 for y-axis) to compensate for the margins
            x1 = window.winfo_pointerx() - window.winfo_x() -9
            y1 = window.winfo_pointery() - 299 - window.winfo_y() - 29
            #Saves those values by appending them to the list
            list.append(x1)
            list.append(y1)
            '''
            Now the list has to sets of corrdinates inside of it, so it is time to make a line
            This makes a line on the canvas, to give the user visual feedback on their input; and
            it draws a line in memory, so the image can be stored as a PNG
            '''
            self.drawing_canvas.create_line(list[2], list[3], list[0], list[1], width = thickness_of_line, fill = "#635f57")
            draw_on_memory_image.line((list[2], list[3], list[0], list[1]),width = 6, fill = "#FFFFFF")

        #This happens if the list is empty, to make sure on the next loop the list will not be empty
        if len(list) == 0:
            #Appends the current corrdinates of the mouse relative to the drawing_canvas to the list, in the same way as above
            list.append(window.winfo_pointerx() - window.winfo_x() -9)
            list.append(window.winfo_pointery() - 299 - window.winfo_y() - 29)

        else:
            #This executes if the list is currently at a length of four
            #The goal of this is to delete the first set of corrdinates in the list

            #Get the last two corrdinates
            x = list[2]
            y = list[3]
            #CLear the list
            list.clear()
            #Append the last two corrdinates to the empty list, making it have a length of 2
            list.append(x)
            list.append(y)

        #Calls another function to turn the newly created image into an array
        data.convert_image_to_array(window, training_data, training_labels, bottom_button, middle_button, third_button, top_button)


    def delete_canvas(self, drawing_canvas, middle_button, third_button, top_button):
        #The goal of this function is to clear the button's text and to clear the canvas' drawing
        drawing_canvas.delete("all")
        self.drawing_canvas =  tk.Canvas()
        #Clears the image stored in memory
        self.memory_image = Image.new("RGB", (986, 366), (0,0,0))
        top_button.config(text="")
        middle_button.config(text="")
        third_button.config(text="")


    def bind_drawing_and_mouse(self, window, training_data, training_labels, bottom_button, middle_button, third_button, top_button, drawing_canvas, list):
        draw_class = draw_line()
        self.drawing_canvas.place(x=2,y=299, height = 366, width = 986)

        #Binds the mouse motion to the draw function
        window.bind('<B1-Motion>',lambda event, window = window, training_data = training_data, training_labels= training_labels, bottom_button=bottom_button, middle_button=middle_button, third_button=third_button, top_button=top_button, list = list:
                                    draw_class.draw(window, training_data, training_labels, bottom_button, middle_button, third_button, top_button, list))
        #Binds the left button to the save_image function
        window.bind('<ButtonRelease-1>', lambda event, drawing_canvas = drawing_canvas, list = list: draw_class.save_image(drawing_canvas, list))
        #Binds the spacebar key to the delete_canvas function
        window.bind('<space>', lambda event, drawing_canvas = drawing_canvas, middle_button = middle_button, third_button = third_button,
                        top_button = top_button: draw_class.delete_canvas(drawing_canvas, middle_button, third_button, top_button))

    def main(self,  window, training_data, training_labels, testing_data, testing_labels, bottom_button, middle_button, third_button, top_button):

        draw_class = draw_line()
        user_input = image_saving()
        self.window = window

        #Assigns the list to an empty array in this function so the list doesn't clear at every movement of the mouse
        #If the list did clear at that then nothing would ever be able to be drawn
        list = []

        draw_class.bind_drawing_and_mouse(window, training_data, training_labels, bottom_button, middle_button, third_button, top_button, self.drawing_canvas, list)
        user_input.main(window, self.drawing_canvas, training_data, training_labels, testing_data, testing_labels)
