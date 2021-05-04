from tkinter import *

top = Tk()

beeList = []

def results():
    print(beeList)

def addToList():
    newItem = E1.get()
    beeList.append(newItem)
#Label widget
L1 = Label(top, text = "Bee hit list")
L1.grid(column = 0, row = 1)

#Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a Button widget
B1 = Button(text = "  Print list  ", bg = "white", command = results)
B1.grid(column = 0, row = 3)

B2 = Button(text = "  Add to list  " , bg = "white", command = addToList)
B2.grid(column = 1, row = 2)


top.mainloop()
