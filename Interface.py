import tkinter as tk
from PIL import Image, ImageTk
from Draw import draw_line
from tkinter import PhotoImage


class displayed_window():

    def __init__(self):
        #sets some basic variables
        self.width_of_window = 1150
        self.height_of_window = 665
        self.color_of_buttons = "#FFA54A"
        self.color_of_text = "#FFFFFF"



    def canvas_setup(self):
        #Creates the Tkinter window
        self.window = tk.Tk()

        #Creates the window with no title, to give the application a clean look
        self.window.title("")

        #Allows the window to always be displayed in the center of the user's screen
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        xx = (ws/2) - (self.width_of_window/2)
        yy = (hs/2) - (self.height_of_window/2)
        self.window.geometry('%dx%d+%d+%d' % (self.width_of_window, self.height_of_window, xx, yy))

        #Create the main canvas, will the the frame for the application
        canvas = tk.Canvas(self.window, width=self.width_of_window, height=self.height_of_window)
        canvas.pack()


        #Creates the label
        image_label_top = tk.Label(bg = '#5DBCD2')
        image_label_top.place(x = 3, y = 3, width = 1145, height = 296)

        #DESIGN PREFERENCE - - Makes the window unable to be resized
        self.window.resizable(False, False)

    def create_the_buttons(self, training_data, training_labels, testing_data, testing_labels):
        #The margin is for the disgn of the buttons, allowing them to not touch the edge of the canvas
        margin = -2
        #In pixels
        all_button_width = 160
        all_button_height = 90
        current_class = displayed_window()
        draw_class = draw_line()

        #Creates the label that the text will go into

        self.label = tk.Label(self.window, text = "", fg = "white", font=("San Francisco", 74), anchor="e", bg = '#5DBCD2')

        self.label.place(x = 74, y = 70, width = 999, height = 200)

        #This creates all four buttons with the correct variables
        self.top_button = tk.Button(self.window, text = " ", bg = self.color_of_buttons, relief='flat',
                        activebackground=self.color_of_buttons, font =("San Francisco", 12), fg = self.color_of_text)
        self.third_button = tk.Button(self.window, text = "", bg = self.color_of_buttons, relief='flat',
                        activebackground=self.color_of_buttons, font =("San Francisco", 12), fg = self.color_of_text)
        self.middle_button = tk.Button(self.window, text = "", bg = self.color_of_buttons, relief='flat',
                        activebackground=self.color_of_buttons, font =("San Francisco", 12), fg = self.color_of_text)
        self.bottom_button = tk.Button(self.window, text = "", bg = self.color_of_buttons, relief='flat',
                        activebackground=self.color_of_buttons, font =("San Francisco", 12), fg = self.color_of_text)

        #Hack-ish solution to place the buttons in the desirable locations, and sets the width and height of each button
        self.bottom_button.place(x = self.width_of_window - (all_button_width - margin), y = self.height_of_window - (all_button_height - margin),
                                                            width = all_button_width, height = all_button_height)
        self.middle_button.place(x = self.width_of_window - (all_button_width - margin), y = (self.height_of_window - (all_button_height - margin)) - all_button_height - 1,
                                                            width = all_button_width, height = all_button_height)
        self.third_button.place(x = self.width_of_window - (all_button_width - margin),
                                    y = (self.height_of_window - (all_button_height - margin)) - all_button_height - all_button_height - 2,
                                    width = all_button_width, height = all_button_height)
        self.top_button.place(x = self.width_of_window - (all_button_width - margin),
                            y = (self.height_of_window - (all_button_height - margin)) - all_button_height - all_button_height - all_button_height - 3,
                            width = all_button_width, height = all_button_height)

        #This configures each button press to the label that displats text
        #Gives the buttons functionality
        self.top_button.configure(command = lambda label=self.label, txt = self.top_button: current_class.callback(label,txt))
        self.middle_button.configure(command = lambda label=self.label, txt = self.middle_button: current_class.callback(label,txt))
        self.third_button.configure(command = lambda label=self.label, txt = self.third_button: current_class.callback(label,txt))
        self.bottom_button.configure(command = lambda label=self.label, txt = 'reset': current_class.callback(label,txt))

        #Binds the backspace key with the task of deleting one digit from the current display
        self.window.bind("<BackSpace>", lambda event, label = self.label: current_class.delete_text(label))

        draw_class.main(self.window, training_data, training_labels, testing_data, testing_labels, self.bottom_button,
                                                        self.middle_button, self.third_button, self.top_button)

    def delete_text(self, label):
        '''
        This is binded to the Baskspace key
        The job of this function is to remove the last (most new) digit to the display
        '''

        #Get the text of the label
        text_of_label = label.cget('text')

        #This is an edge-case, if the backspace key is pressed without text inside the label
        if text_of_label == "":
            #Does nothing
            pass
        else:
            #This replaces the label's text with the new text
            label.configure(text = text_of_label[:len(text_of_label) - 1], fg="white", font =("San Francisco", 74))

    def bind_the_buttons(self):
        #This makes all the buttons a different color (#ea9527) when the mouse enters the range of pixels; to show feedback to the user
        self.top_button.bind("<Enter>", lambda event: self.top_button.configure(bg="#ea9527", fg="white"))
        self.third_button.bind("<Enter>", lambda event: self.third_button.configure(bg="#ea9527", fg="white"))
        self.middle_button.bind("<Enter>", lambda event: self.middle_button.configure(bg="#ea9527", fg="white"))
        self.bottom_button.bind("<Enter>", lambda event: self.bottom_button.configure(bg="#ea9527", fg="white"))

        #Returns the buttons to a normal state when the mouse courser leaves
        self.top_button.bind("<Leave>", lambda event: self.top_button.configure(bg=self.color_of_buttons))
        self.third_button.bind("<Leave>", lambda event: self.third_button.configure(bg=self.color_of_buttons))
        self.middle_button.bind("<Leave>", lambda event: self.middle_button.configure(bg=self.color_of_buttons))
        self.bottom_button.bind("<Leave>", lambda event: self.bottom_button.configure(bg=self.color_of_buttons))

        #An infinite loop to make the window visible to the user
        #Without this loop, everything the program does will have been done in memory, and nothing would have been displayed on the screen
        self.window.mainloop()

    def callback(self, label, text):
        #The purpose of this function is to display the Algorithm's output onto the label
        text_of_label = label.cget('text')

        #The bottom button doesn't display a guess, it is always blank
        #This is beacuse it has a different purpose; to reset the label
        if text == 'reset':
            label.configure(text = "", fg="white", font =("San Francisco", 74))
        else:
            #Adds the guess only (at the 0-th index of the button's text) to the already existing label's text
            label.configure(text = str(text_of_label) + str(text.cget('text'))[0], fg="white", font =("San Francisco", 74))


    def main(self, training_data, training_labels, testing_data, testing_labels):
        #Calls all of the functions
        current_class = displayed_window()
        current_class.__init__()
        current_class.canvas_setup()
        current_class.create_the_buttons(training_data, training_labels, testing_data, testing_labels)
        current_class.bind_the_buttons()
