import tkinter as tk
from tkinter import messagebox

messagebox.showinfo('Info', 'This is a sample window')  # we put this command in a function and call it inside a button 
root = tk.Tk()  # Create a window and store it in the variable 'root'

root.title('GUI')  # Set the title of the window to 'GUI'
root.geometry('500x500')  # Set the dimensions of the window to 500x500 pixels
root.configure(background='cornflowerblue')  # Set the background color to 'cornflowerblue'

# Get the screen width and height
ws = root.winfo_screenwidth()  
hs = root.winfo_screenheight()
w=500
h=500
# here we need int values we can also do like x=int(ws/2-w/2)
x=(ws//2-w//2)
y=(hs//2-h//2)

# here we need sting values inside geometery()
data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y) # givenwidth x givenheight + x-offset + y-offset(400 x 400 + 500 + 400)if ws=1400 & wh=1200 , w=400 & h=400
root.geometry(data)

# thats not working messagebox.showinfo(f"Screen width: {ws}, Screen height: {hs}")  # Print the screen dimensions
def btn():
    print("helooooo!")

#remember that grid and pack are not used simultaneously, u only have to choose one b/w them but (place and grid or place and pack ares used simultaneously) 
# pack makes window responsive
l= tk.Label(root, text='hello world')
l.pack()

          
b= tk.Button(root, text='click here', command=btn, height=2, width=10, font=('Courier',12), fg='coral', bg='aquamarine', relief='groove')
b.pack(side=tk.RIGHT)

b2= tk.Button(root, text='click here', command=btn)
b2.pack(side=tk.BOTTOM)

'''b3= tk.Button(root, text='PLACE btn', command=btn)
b3.place(x=50, y=50)

b4= tk.Button(root, text='click here', command=btn)
b4.grid(row=0, column=0)
b5= tk.Button(root, text='click here', command=btn)
b5.grid(row=0, column=3)
b6= tk.Button(root, text='click here', command=btn)
b6.grid(row=1, column=2) '''

e1 = tk.Entry(root, font=('arial', 16))
e1.pack(padx=50, pady=50, ipadx=20)

r1= tk.Radiobutton(root,text='apple', font=('arial', 18), )
r1.pack()

root.mainloop()  # This window is now in an endless loop, waiting for events
