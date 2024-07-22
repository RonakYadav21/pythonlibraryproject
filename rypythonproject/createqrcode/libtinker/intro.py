import tkinter as tk
root=tk.Tk()   # create root window
button=tk.Button(root,text="click me")
button.pack()  ## Place the label widget on the root window
#callback function
def click():
    print("button is clicked")


# bind click event with callback function
button.config(command=click)
#config() it is used to change the attribute of the widget
button.config(bg="red")
button.config(state="disabled")  # etc

#creat a label
label=tk.Label(root,text="hellow world")
label.pack()
root.mainloop()  # start mainloo