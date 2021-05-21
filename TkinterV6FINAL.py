from tkinter import *
import random

top = Tk()
bees = []
myRolls = []
appList = []

top.geometry("500x500")

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

    B1Main = Button(text = "  Week 1  ", bg = "white", command = week1, height = 5, width = 20)
    B1Main.grid(column = 0, row = 2)
    
    B2Main = Button(text = "  Week 2  ", bg = "white", command = week2, height = 5, width = 20)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "  Week 3  ", bg = "white", command = week3, height = 5, width = 20)
    B3Main.grid(column = 0, row = 4)

def week1():
    
    def addToList():
        newItem = E1.get()
        bees.append(newItem)
        E1.delete(0, END)
        
    clearWindow()
        
    #Label Widget
    L1 = Label(top, text = "Bees")
    L1.grid(column = 1, row = 1)

    #Button widget
    B1 = Button(text = "  Print Bees  ", bg = "white", command = results)
    B1.grid(column = 1, row = 3)

    B2 = Button(text = " + ", bg = "white", command = addToList)
    B2.grid(column = 3, row = 2)

    B3 = Button(text = "  Export List  ", bg = "white", command = exportList)
    B3.grid(column = 1, row = 4)

    Brexit = Button(text = "  Main Menu  ", bg = "white", command = mainMenu)
    Brexit.grid(column = 1, row = 0)

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
    L1Week2.grid(column = 1, row = 1)

    L2Week2 = Label(top, text = "How many sides?")
    L2Week2.grid(column = 1, row = 2)

    L3Week2 = Label(top, text = "How many rolls?")
    L3Week2.grid(column = 3, row = 2)

    E1Week2 = Entry(top, bd = 5)
    E1Week2.grid(column = 1, row = 3)

    E2Week2 = Entry(top, bd = 5)
    E2Week2.grid(column = 3, row = 3)
              
    B1Week2 = Button(text = "Roll", bg = "white", command = rollDice)
    B1Week2.grid(column = 3, row = 4)

    Brexit = Button(text = "  Main Menu  ", bg = "white", command = mainMenu)
    Brexit.grid(column = 0, row = 1)

def week3():
    
    clearWindow()

    def Add():
        
        def Add2():
            newItem2 = EAdd1.get()
            appList.append(newItem2)
            EAdd1.delete(0, END)
            clearWindow()
            Add()
            
        clearWindow()

        LAdd1 = Label(top, text = "Type what you want to add to the list")
        LAdd1.grid(column = 0, row = 0)

        LAdd2 = Label(top, text = "{}".format(appList))
        LAdd2.grid(column = 0, row = 2)

        EAdd1 = Entry(top, bd = 5)
        EAdd1.grid(column = 0, row = 1)

        BAdd1 = Button(text = " + ", bg = "white", command = Add2)
        BAdd1.grid(column = 1, row = 1)

        BAdd2 = Button(text = "Back", bg = "white", command = week3)
        BAdd2.grid(column = 1, row = 0)

    L1Week3 = Label(top, text = "Welcome to the list app")
    L1Week3.grid(column = 0, row = 0)

    B1Week3 = Button(text = "Add to list", bg = "white", command = Add)
    B1Week3.grid(column = 0, row = 1)

    B2Week3 = Button(text = "Remove from list", bg = "white", command = Add)
    B2Week3.grid(column = 0, row = 2)

    B3Week3 = Button(text = "Add a bunch a numbers", bg = "white", command = Add)
    B3Week3.grid(column = 0, row = 3)

    B4Week3 = Button(text = "Return the value at an index position", bg = "white", command = Add)
    B4Week3.grid(column = 0, row = 4)

    B5Week3 = Button(text = "Sort list", bg = "white", command = Add)
    B5Week3.grid(column = 0, row = 5)

    B6Week3 = Button(text = "Random choice", bg = "white", command = Add)
    B6Week3.grid(column = 0, row = 6)

    B7Week3 = Button(text = "Linear Search", bg = "white", command = Add)
    B7Week3.grid(column = 0, row = 7)

    B8Week3 = Button(text = "recursiveBinarySearch", bg = "white", command = Add)
    B8Week3.grid(column = 0, row = 8)

    B9Week3 = Button(text = "iterativeBinartSearch", bg = "white", command = Add)
    B9Week3.grid(column = 0, row = 9)

    B10Week3 = Button(text = "Print list", bg = "white", command = Add)
    B10Week3.grid(column = 0, row = 10)

    B11Week3 = Button(text = "Clear List", bg = "white", command = Add)
    B11Week3.grid(column = 0, row = 11)

    B12Week3 = Button(text = "End the program", bg = "white", command = Add)
    B12Week3.grid(column = 0, row = 12)

    Brexit = Button(text = "  Main Menu  ", bg = "white", command = mainMenu)
    Brexit.grid(column = 1, row = 1)





    
if __name__ == "__main__":
    mainMenu()
    top.mainloop()
