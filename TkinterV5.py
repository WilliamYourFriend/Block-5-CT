from tkinter import *
import random

top = Tk()
bees = []
myRolls = []

def results():
    print(bees)

def exportList():
    with open("test.txt", "w") as f:
        for item in bees:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)

    B1Main = Button(text = "  Week 1  ", bg = "white", command = week1)
    B1Main.grid(column = 0, row = 2)
    
    B2Main = Button(text = "  Week 2  ", bg = "white", command = week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "  Week 3  ", bg = "white")
    B3Main.grid(column = 0, row = 4)

def week1():
    
    def addToList():
        newItem = E1.get()
        bees.append(newItem)
        E1.delete(0, END)
        
    clearWindow()
        
    #Label Widget
    L1 = Label(top, text = "Bees")
    L1.grid(column = 0, row = 1)

    #Button widget
    B1 = Button(text = "  Print Bees  ", bg = "white", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg = "white", command = addToList)
    B2.grid(column = 2, row = 2)

    B3 = Button(text = "  Export List  ", bg = "white", command = exportList)
    B3.grid(column = 0, row = 4)

    Brexit = Button(text = "  Main Menu  ", bg = "white", command = mainMenu)
    Brexit.grid(column = 3, row = 1)

    #Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column=0, row=2)

def week2():
    def rollDice():
        #update variable data
        dieType = E2Week2.get()
        rollTimes = E1Week2.get()
        #clear window AFTER updating variables
        clearWindow()
        #roll the dice
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #duild the results window
        L4Week2 = Label(top, text = "Heres your rolls")
        L4Week2.grid(column = 0, row = 1)

        L5Week2 = Label(top, text = "{}".format(myRolls))
        L5Week2.grid(column = 0, row = 2)

        B2Week2 = Button(text = "Main Menu", bg = "white", command = mainMenu)
        B2Week2.grid(column = 0, row = 3)
        
    clearWindow()

    L1Week2 = Label(top, text = "Dice Roller Program")
    L1Week2.grid(column = 0, row = 1)

    L2Week2 = Label(top, text = "How many sides?")
    L2Week2.grid(column = 0, row = 2)

    L3Week2 = Label(top, text = "How many rolls?")
    L3Week2.grid(column = 2, row = 2)

    E1Week2 = Entry(top, bd = 5)
    E1Week2.grid(column = 0, row = 3)

    E2Week2 = Entry(top, bd = 5)
    E2Week2.grid(column = 2, row = 3)
              
    B1Week2 = Button(text = "Roll", bg = "white", command = rollDice)
    B1Week2.grid(column = 2, row = 4)
        
if __name__ == "__main__":
    mainMenu()
    top.mainloop()
