from tkinter import *
import sqlite3
import tkinter.messagebox

#button clear action
def clearEntry():
    entAmount.delete(0,END)
    entCategory.delete(0.0,END)
    entDate.delete(0,END)
    entTotalExpenses.delete(0,END)

#create action for submitting form data to database
def submitForm():
    print(entAmount.get())
    
    
    #Create database/connect to database
    conn = sqlite3.connect('student-expense-logs-data.db')

    #Create a cursor
    c = conn.cursor()
    
    c.execute("INSERT INTO log(amount,category,date,total expenses) VALUES(?,?,?,?)",
              (entAmount.get(),entCategory.get(1.0,END),entDate.get(),entTotalExpenses.get(),))

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()
        
    #show message box for successful query
    tkinter.messagebox.showinfo("Success", "Data inserted successfully.")
    
    #clear the form after button is hit & show existing data
    clearEntry()
    showExisting()

def showExisting():
    conn = sqlite3.connect('student-expense-logs-data.db')  
    c = conn.cursor()
    
    #query existing record from contact table
    c.execute("SELECT * FROM log")
    conn.commit()
    
    #fetch the data
    records = c.fetchall()
    
    #display the data
    rownum = 9 #to hold current row in grid, to be increased with each data existed

    for r in records:
        print(r)
        #to place data
        lblExNo2 = Label(lfExistingContact, text=str(r[0]), bg="white")
        lblExNo2.grid(row=rownum,column=0,padx=2,sticky=W)
        lblExAmount2 = Label(lfExistingContact, text=str(r[1]), bg="white")
        lblExAmount2.grid(row=rownum,column=1,padx=2,sticky=W)
        lblExCategory2 = Label(lfExistingContact, text=str(r[2]), bg="white", justify=LEFT)
        lblExCategory2.grid(row=rownum,column=2,padx=2,sticky=W)
        lblExDate2 = Label(lfExistingContact, text=str(r[3]), bg="white")
        lblExDate2.grid(row=rownum,column=3,padx=2,sticky=W)
        lblExTotalExpenses2 = Label(lfExistingContact, text=str(r[4]), bg="white")
        lblExTotalExpenses2.grid(row=rownum,column=4,padx=2,sticky=W)
        
        rownum += 1
     
    conn.close()
    

#creating main window
root = Tk()
root.title("Student Expense Logs")
#root.geometry("600x400")

#creating LabelFrame
group1 = LabelFrame(root, borderwidth=5, text="Insert an expense")
#creating a label widget
lblTitle = Label(root, text = "Student Expense Logs")
#lblInstruction = Label(root, text = "Insert an expense")
lblAmount = Label(group1, text = "Amount :")
lblCategory = Label(group1, text = "Category :")
lblDate = Label(group1, text = "Date :")
lblTotalExpenses = Label(group1, text = "Total Expenses :")

#creating entry & text widget 
entAmount = Entry(group1, width=50)
entCategory = Text(group1, width=37, height=2)
entDate = Entry(group1, width=50)
entTotalExpenses = Entry(group1, width=50)
#creating frame widget for buttons
buttongroup = Frame(root)
#creating button widget
btnSave = Button(buttongroup, text="Save", command=submitForm)
btnClear = Button(buttongroup, text="Clear", command=clearEntry)
btnShowAll = Button(buttongroup, text="Show All", command=showExisting)

#showing it onto the screen
#myLabel.pack()  #using pack
#using grid layout
lblTitle.grid(row=0, column=0, columnspan=2)
group1.grid(row=1, column=0, padx=50)
lblAmount.grid(row=2, column=0)
lblCategory.grid(row=3, column=0)
lblDate.grid(row=4, column=0)
lblTotalExpenses.grid(row=5, column=0)
entAmount.grid(row=2, column=1)
entCategory.grid(row=3, column=1, sticky=W)
entDate.grid(row=4, column=1)
entTotalExpenses.grid(row=5, column=1)
buttongroup.grid(row=6, column=0)
btnSave.grid(row=6, column=0)
btnClear.grid(row=6, column=1)
btnShowAll.grid(row=6, column=2)

#create & show the existing records part
lfExistingContact = LabelFrame(root, text="Student Expense Records", bg="white", width=400, height=500)
lfExistingContact.grid(row=7, column=0)
#lfExistingContact.grid_propagate(0) #to prevent the grid to shrink according to content and ignore the specified width & height
lblExNo = Label(lfExistingContact, text="No.")
lblExNo.grid(row=8,column=0,padx=2,sticky=W)
lblExAmount = Label(lfExistingContact, text="Amount")
lblExAmount.grid(row=8,column=1,padx=2,sticky=W)
lblExCategory = Label(lfExistingContact, text="Category")
lblExCategory.grid(row=8,column=2,padx=2,sticky=W)
lblExDate = Label(lfExistingContact, text="Date")
lblExDate.grid(row=8,column=3,padx=2,sticky=W)
lblExTotalExpenses = Label(lfExistingContact, text="Total Expenses")
lblExTotalExpenses.grid(row=8,column=4,padx=2,sticky=W)


#call the mainloop of tk
root.mainloop()