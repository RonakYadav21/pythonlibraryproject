from tkinter import *
root=Tk()
#root.geometry('500X500')
root.config(bg='lightyellow')
frame=Frame(root)
label=Label(frame,text="search: ")
label.place(x=20,y=50,height="30",width="50")
label.pack(side=LEFT)
entry = Entry(frame)
entry.pack(side=LEFT, fill=BOTH, expand=1)
button = Button(frame, text="Search")
button.pack(side=RIGHT)
def search():
    # Get the search term from the text box
    search_term = entry.get()

button.config(command=search)


root.mainloop()