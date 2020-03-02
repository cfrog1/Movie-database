"""
A program that stores information about movies: Title, Year, RT rating, Director

User can Add, Update, Delete, Search, View All, and Close
"""

from tkinter import Tk, Entry, Label, Listbox, StringVar, Scrollbar, Button, END
import backend

def get_selected_row(event):
    #Puts details of selection in respective entry boxes, and stores global variable
    global selected_row
    if not movie_list.curselection():
        return
    index = movie_list.curselection()[0]
    selected_row = movie_list.get(index)
    title_entry.delete(0,END)
    title_entry.insert(0,selected_row[0])
    year_entry.delete(0,END)
    year_entry.insert(0,selected_row[1])
    rt_entry.delete(0,END)
    rt_entry.insert(0,selected_row[2])
    dir_entry.delete(0,END)
    dir_entry.insert(0,selected_row[3])
    
#Functions that connect to backend.py
def view_command():
    movie_list.delete(0,END)
    for row in backend.view():
        movie_list.insert(END, row)

def search_command():
    movie_list.delete(0,END)
    for row in backend.search(title_val.get(),year_val.get(),rt_val.get(),dir_val.get()): 
        movie_list.insert(END,row)  

def add_command():
    backend.insert(title_val.get(),year_val.get(),rt_val.get(),dir_val.get())
    movie_list.delete(0,END)
    movie_list.insert(END, (title_val.get(),year_val.get(),rt_val.get(),dir_val.get()))

def del_command():
    backend.delete(selected_row[0])

def update_command():
    backend.update(selected_row[0],year_val.get(),rt_val.get(),dir_val.get())


#Creates Tkinter window
master = Tk()
master.wm_title("Movie List")

#Labels and entries for Title, Year, RT rating, Director
title_label = Label(master, text="Title")
title_label.grid(row=0, column=0)

year_label = Label(master, text='Year')
year_label.grid(row=1, column=0)

rt_label = Label(master, text='RT rating')
rt_label.grid(row=0, column=2)

dir_label = Label(master, text='Director')
dir_label.grid(row=1, column=2)

title_val = StringVar()
title_entry = Entry(master, textvariable=title_val)
title_entry.grid(row=0,column=1)

year_val = StringVar()
year_entry = Entry(master, textvariable=year_val)
year_entry.grid(row=1,column=1)

rt_val = StringVar()
rt_entry = Entry(master, textvariable=rt_val)
rt_entry.grid(row=0,column=3)

dir_val = StringVar()
dir_entry = Entry(master, textvariable=dir_val)
dir_entry.grid(row=1,column=3)

#Listbox for viewing movie entries, with scrollbar
movie_list = Listbox(master, height=6, width=35)
movie_list.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll = Scrollbar(master)
scroll.grid(row=2,column=2,rowspan=6)

movie_list.configure(yscrollcommand=scroll.set)
scroll.configure(command=movie_list.yview)

movie_list.bind('<<ListboxSelect>>',get_selected_row) #Activates get_selected_row when listbox selected

#Buttons for View All, Search, Add, Update, Delete, Close
view_button = Button(master, text="View All", width=12, command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(master, text="Search", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(master, text="Add New", width=12, command=add_command)
add_button.grid(row=4, column=3)

update_button = Button(master, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)

del_button = Button(master, text="Delete", width=12, command=del_command)
del_button.grid(row=6, column=3)

close_button = Button(master, text="Close", width=12,command=master.destroy)
close_button.grid(row=7, column=3)

#Driving functions
master.mainloop()
backend.connect()