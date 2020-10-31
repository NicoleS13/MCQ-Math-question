from tkinter import *
window = Tk()
c = Canvas(window, height=100, width=400)
c.pack()

c.create_text(50, 30, text = "What is 12 + 4?", fill = 'black')
c.create_text(113, 50, text = "Press the button with the answer to answer", fill = 'black')

def bAaction():
  print("\nCorrect!")
def bBaction():
  print("\nWrong!")
def bCaction():
  print("\nWrong!")
def bDaction():
  print("\nWrong!")

buttonA = Button(window, text="a) 16", command=bAaction)
buttonB = Button(window, text="b) 8", command=bBaction)
buttonC = Button(window, text="c) 48", command=bCaction)
buttonD = Button(window, text="d) 3", command=bDaction)
buttonA.pack()
buttonB.pack()
buttonC.pack()
buttonD.pack()
