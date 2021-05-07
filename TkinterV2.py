from tkinter import *

top = Tk()
bees = []

def results():
    print(bees)

def addToList():
    newItem = E1.get()
    bees.append(newItem)
    E1.delete(0, END)

def exportList():
    with open("test.txt", "w") as f:
        for item in bees:
            f.write("%s\n" % item)

#Label Widget
L1 = Label(top, text = "Bees")
L1.grid(column = 0, row = 1)

#Button widget
B1 = Button(text = "  Print Bees  ", bg = "white", command = results)
B1.grid(column = 1, row = 2)

B2 = Button(text = " + ", bg = "white", command = addToList)
B2.grid(column = 2, row = 2)

B3 = Button(text = "Export List", bg = "white", command = exportList)
B3.grid(column = 0, row = 4)

#Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column=0, row=2)

top.mainloop()
