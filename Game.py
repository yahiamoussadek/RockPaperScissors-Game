from tkinter import *
from random import randint


def rock():
	text = ""
	x = randint(0,2)	

	if x == 0:
		text += "Computer's Choice: Rock\nResult = Tie.\n"

	elif x == 1:
		text += "Computer's Choice: Paper\nResult = Computer Wins.\n"
	else :
		text += "Computer's Choice: Scissors\nResult = You win.\n"	

	space.insert(END,text+"\n================\n")	

def scissors():
	text = ""
	x = randint(0,2)

	if x == 0:
		text += "Computer's Choice: Rock\nResult = Computer Wins.\n"

	elif x == 1:
		text += "Computer's Choice: Paper\nResult = You win.\n"
	else :
		text += "Computer's Choice: Scissors\nResult = Tie.\n"

	space.insert(END,text+"\n================\n")


def paper():
	text = ""
	x = randint(0,2)
	if x == 0:
		text += "Computer's Choice: Rock\nResult = You Win.\n"

	elif x == 1:
		text += "Computer's Choice: Paper\nResult = Tie.\n"
	else :
		text += "Computer's Choice: Scissors\nResult = Computer Wins.\n"

	space.insert(END,text+"\n================\n")

root = Tk()
root.title("Yahia Moussadek")
root.geometry("500x510")
root.configure(bg="#2C3E50")

Rock = Button(root,text="Rock",width=25,height=3,background="#007CFF",command=rock)
Rock.pack(padx=70,pady=7)

Paper = Button(root,text="Paper",width=25,height=3,background="#F9325C",command=paper)
Paper.pack(padx=70,pady=7)

Scissors = Button(root,text="Scissors",width=25,height=3,background="#28E84E",command=scissors)
Scissors.pack(padx=70,pady=7)



#space = Label(root,text=s,width=70,height=15,background="#FAEA5B",padx=-5,pady=0)
#space.pack(padx=50,pady=7)

space = Text(root,height=17,width=55,bg="#faea5b")
space.insert(END,"Welcome to Rock-Paper-Scissors Game\n\nThis Game is developped by Yahia Moussadek\n\n")

space.pack(padx=50,pady=8)

root.resizable(False,False)
root.mainloop()