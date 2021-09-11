# How to change end display box to display answers
#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json

class Quiz:

    def __init__(self):

        # set question number to 0
        self.q_no=0

        self.all_answers = []

        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected=IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts=self.radio_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.buttons()

        # no of questions
        self.data_size=len(question)

        # keep a counter of correct answers
        self.correct=0


    def display_result(self):



        result = self.all_answers

        for option in options[self.q_no]:
            options1 = options[0]

        # Shows a message box to display the result
        if result[0] == 1:
            if 1 in result:
                answer = "you are windrunner"
                mb.showinfo("Result", answer)
        elif result[0] == 2:
            if 2 in result:
                answer = "you are lightweaver"
                mb.showinfo("Result", "You could be a Lightweaver")
        elif result[0] == 3:
            mb.showinfo("Result", "You could be a Bondsmith")
        elif result[0] == 4:
            mb.showinfo("Result", "You could be a Edgedancer")
        else:
            mb.showinfo("Result", "You could be a Dustbringer")
        if result[1] == 1:
            if 1 in result:
                answer = "you are cryptic"
                mb.showinfo("Result", answer)
        elif result[2] == 1:
            mb.showinfo("Result", "You are a bondsmith?")
        elif result[3] == 1:
            mb.showinfo("Result", "You are a slidey person?")

            #def check_answer(self, q_no):

            #if self.opt_selected.get() == answer[q_no]:
            return


    def next_btn(self):

        self.all_answers.append(self.opt_selected.get())

        # Check if the answer is correct
        #if self.check_answer(self.q_no):

        # if the answer is correct it increments the correct by 1
        self.correct += 1




        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:

            # if it is correct then it displays the score


            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
            self.display_result()


    def buttons(self):

        next_button = Button(gui, text="Next",command=self.next_btn,
                             width=10,bg="blue",fg="white",font=("ariel",16,"bold"))

        next_button.place(x=350,y=380)

        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5,bg="black", fg="white",font=("ariel",16," bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)

    #adds the text for the radio buttons
    def display_options(self):

        val=0

        # deselecting the options
        self.opt_selected.set(0)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1


    def display_question(self):

        q_no = Label(gui, text = question[self.q_no], width=60,
                     font=( 'ariel' ,16, 'bold' ), anchor= 'w' )

        q_no.place(x=1, y=2)

    def display_title(self):

        title = Label(gui, text="Radiant quiz",
                      width=50, bg="green",fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    # adds the radio buttons without the text
    def radio_buttons(self):

        q_list=[]

        # position of the first option
        y_pos = 150

        while len(q_list)<5:

            radio_btn = Radiobutton(gui, text=" ", variable= self.opt_selected,
                                    value = len(q_list)+1,font = ("ariel",14))

            q_list.append(radio_btn)

            # placing the button
            radio_btn.place(x = 100, y = y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        return q_list




gui = Tk()

# set the size of the GUI Window
gui.geometry("800x450")

# set the title of the Window
gui.title("GeeksforGeeks Quiz")

# get the data from the json file
with open('data.json') as f:
    data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
#answer = (data[ 'answer'])

# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()
