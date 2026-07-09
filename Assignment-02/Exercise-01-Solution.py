
from tkinter import *

# massage box
from tkinter import messagebox

root= Tk()

# write title for game
root.title('Tic-Tac-Toe')

# Build Buttom
b1=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b1))
b2=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b2))
b3=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b3))

b4=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b4))
b5=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b5))
b6=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b6))

b7=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b7))
b8=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b8))
b9=Button(root, text=' ', font=("Helvetica", 20), height=3, width=6, bg="gray",command= lambda: b_click(b9))

# Grid our Button to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

#disable all button():
def disable_all_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# winner Check
def Winner():

    # Check if X win
    if b1["text"]==b2["text"]==b3["text"]=="X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    elif b1["text"]==b4["text"]==b7["text"]=="X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    elif b1["text"]==b5["text"]==b9["text"]=="X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    elif b4["text"]==b5["text"]==b6["text"]=="X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    elif b7["text"]==b8["text"]==b9["text"]=="X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    elif b2["text"]==b5["text"]==b8["text"]=="X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    elif b3["text"]==b9["text"]==b6["text"]=="X":
        b3.config(bg="green")
        b9.config(bg="green")
        b6.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    elif b3["text"]==b5["text"]==b7["text"]=="X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," X win!! :)")
        disable_all_button()
        
    #Check if O win
    elif b1["text"]==b2["text"]==b3["text"]=="O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
        
    elif b1["text"]==b4["text"]==b7["text"]=="O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
        
    elif b1["text"]==b5["text"]==b9["text"]=="O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
        
    elif b4["text"]==b5["text"]==b6["text"]=="O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
        
    elif b7["text"]==b8["text"]==b9["text"]=="O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
        
    elif b2["text"]==b5["text"]==b8["text"]=="O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
        
    elif b3["text"]==b9["text"]==b6["text"]=="O":
        b3.config(bg="green")
        b9.config(bg="green")
        b6.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
        
    elif b3["text"]==b5["text"]==b7["text"]=="O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        messagebox.showinfo("Tic Tac Toe"," O win!! :)")
        disable_all_button()
    elif count==9:
        messagebox.showinfo("Tic Tac Toe",'No one win!')
        disable_all_button()
# Who start? X
# for swiching between players
count=0
## Button clicked function
def b_click(b):
    global count
    # X Trun
    if (b['text']== " ") and (count %2==0 ):
        b['text']="X"
        count +=1
        Winner()
    # O Trun
    elif (b['text']== " ") and (count %2==1):
        b['text']="O"
        count +=1
        Winner()
    # if it has text X or O in it
    else: 
        messagebox.showinfo("Tic Tac Toe",'This box has been choosen befor Click on other bottom')
        
        
        



root.mainloop()
