#MyFirstGUI
from tkinter import *

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()
        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()
        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Date of Birth")
        self.label3.pack()
        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Enter Member Type")
        self.label4.pack()
        self.entry4 = Entry()
        self.entry4.pack()

        
        self.InsertDB = Button(master, text="Insert Into Database", command=self.InsertDBFunction)
        self.InsertDB.pack()

        self.PrintMembers = Button(master, text="Print Members", command=self.PrintMembersFunction)
        self.PrintMembers.pack()    


        self.closeButton = Button(master, text="Close", command=self.close)
        self.closeButton.pack()

    def InsertDBFunction(self):    
        print("Testing " + self.entry1.get())
        
    def PrintMembersFunction(self):    
        print("Print Test " + self.entry1.get())

    def close(self):
        root.destroy()

root = Tk()
my_gui = MyFirstGUI(root)
root.dooneevent()
