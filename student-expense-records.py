from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
    
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()
 
    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("Student Expense Tracker")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="white")
 
        # Define the different GUI widgets
        self.Amount_label = tk.Label(self.root, text="Amount:RM :")
        self.Amount_entry = tk.Entry(self.root)
        self.Amount_label.grid(row=0, column= 0 ,sticky = tk.W)
        self.Amount_entry.grid(row=0, column=1,sticky = tk.W)
 
        self.Discription_label = tk.Label(self.root, text="Discription :")
        self.Discription_entry = tk.Entry(self.root)
        self.Discription_label.grid(row=1, column=0 ,sticky = tk.W)
        self.Discription_entry.grid(row=1, column=1,sticky = tk.W)
        
        self.Date_label = tk.Label(self.root, text="Date :")
        self.Date_entry = tk.Entry(self.root)
        self.Date_label.grid(row=2, column= 0, sticky = tk.W)
        self.Date_entry.grid(row=2, column=1,sticky = tk.W)
 
        self.submit_button = tk.Button(self.root, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=3, column=2, sticky = tk.W)
        
        self.total_button = tk.Button(self.root, text="Total:RM", command=self.total_data)
        self.total_button.grid(row=3, column=4, sticky = tk.W)
 
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=100, column=100)
        
        self.label = tk.Label(self.root, text="Total")
        self.label.grid(row=100, column= 50)
 
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=3, column=3)
 
        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('date','Amount','Discription'))
 
        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Date')
        self.tree.heading('#2', text='Amount')
        self.tree.heading('#3', text='Discription')
 
        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)
                
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
                
        self.id = 0
        self.iid = 0
    
    def total_data(self):
        sum1 = 0.0
        for child in self.treeview.get_children():
            sum1 += float(self.treeview.item(child, "values")[1])
            self.label.config(text=sum1)

            print(sum1)
        
    def insert_data(self):
        self.treeview.insert('', 'end', iid=self.iid, text="" + str(self.id),
                             values=( self.Date_entry.get(),
                                     self.Amount_entry.get(),
                                     self.Discription_entry.get()))
        self.iid = self.iid + 1
        self.id = self.id + 1
        
    def delete_data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)
        
    
    def treeview_sort_column(tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

    # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

    # reverse sort next time
            tv.heading(col, command=lambda: \
            treeview_sort_column(tv, col, not reverse))


app = Application(tk.Tk())
app.root.mainloop()