from tkinter import Tk, Frame, Label, Button 
from time import sleep

analytical = 0
authority = 0
emotion = 0
finalType = ""
class Question:
    def __init__(self, question, answers, typeOfperson):
        self.question = question
        self.answers = answers
        self.typeOfperson = typeOfperson

    def check(self, letter, view):
        global analytical
        global authority
        global emotion
        if(self.typeOfperson == "authority"):
            if (letter == 1):
                authority += authority
            elif (letter == 2):
                authority = authority + 2 
            elif (letter == 3):
                authority = authority + 3
            elif (letter == 4):
                authority = authority + 4
            elif (letter == 5):
                authority = authority + 5       
        elif(self.typeOfperson == "analytical"):
            if (letter == 1):
                analytical += analytical
            elif (letter == 2):
                analytical = analytical + 2 
            elif (letter == 3):
                analytical = analytical + 3
            elif (letter == 4):
                analytical = analytical + 4
            elif (letter == 5):
                analytical = analytical + 5 
        elif(self.typeOfperson == "emotion"):
            if (letter == 1):
                emotion += emotion
            elif (letter == 2):
                emotion = emotion + 2 
            elif (letter == 3):
                emotion = emotion + 3
            elif (letter == 4):
                emotion = emotion + 4
            elif (letter == 5):
                emotion = emotion + 5        
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check(1, view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check(2, view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check(3, view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check(4, view)).pack()
        Button(view, text=self.answers[4], command=lambda *args: self.check(5, view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, number_of_questions, finalType
    if(number_of_questions == index + 1):
        if (authority > analytical and authority > emotion):
            finalType = "authority"
        elif (analytical > authority and analytical > emotion):    
            finalType = "analytical"
        elif (emotion > authority and emotion > analytical):
            finalType = "emotion"    
        Label(window, text="Authority: " + str(authority) + " Analytical: " + str(analytical) + " Emotion: " + str(emotion) + " . You are " + finalType).pack()
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (5):
        answers.append(file.readline())
    typeOfperson = file.readline()
    typeOfperson = typeOfperson[:-1]
    questions.append(Question(questionString, answers, typeOfperson))
    line = file.readline()
file.close()
index = -1
number_of_questions = len(questions)

window = Tk()
button = Button(window, text="Start", height = 20, width = 20,  command=askQuestion)
button.pack()
lblStatus = Label(window, text = "Status")
window.geometry('600x600')
window.mainloop()