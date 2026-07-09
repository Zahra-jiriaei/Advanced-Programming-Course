# install libraries
#pip install pillow
#pip install tkcalendar

# Import nessesarry libraries
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror, showwarning, showinfo
from tkcalendar import Calendar
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.messagebox import askyesno


class InputFrame_Email_pass(ttk.Frame):
    """
    This frame make for email and password entry and login
    """
    
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()
        
    def __create_widgets(self):
        """
        Create email and password widget
        """
        # Email
        ttk.Label(self, text='Email: ').grid(column=0, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        # Password
        ttk.Label(self, text='Password: ').grid(
            column=0, row=1, sticky=tk.W)
        Password = ttk.Entry(self, width=30,show='*')
        Password.grid(column=1, row=1, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

            
class ButtonFrame_login(ttk.Frame):
    """
    This frame make for login buttom
    """
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        
        """
        Making login buttom
        """
        ttk.Button(self, text='login',command=self.open_window_2).grid(column=0, row=0)
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)            
    
    # IF CUSTOMER NEED SING UP
    def open_window_0(self):
        showerror(title='Error',message='You have to sign up first!')
        window = Window_SignUp(self)
        window.grab_set()

    # IF CUSTOMER SIGN UP BEFOR
    def open_window_1(self):
        showinfo(title='Information',message='Welcome! you can order now :)')
        window = Window_Order(self)
        window.grab_set()

    # IF MANAGER SING UP
    def open_window_2(self):
        showinfo(title='Information',message='Welcome boss! :)')
        window = Window_boss(self)
        window.grab_set()
    
class welcome_frame(ttk.Frame):
    """
    This frame make for showind welcome massage
    """
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()
        
    def __create_widgets(self):
        """
        Making massage
        """
        label = ttk.Label(self,text='welcom to Amiran Food', font=("Helvetica", 10))
        label.pack(ipadx=10, ipady=10)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3) 
            
            
class Window_SignUp(tk.Toplevel):
    """
    this window appear if customer is not login to the system
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        # Size of the top level info
        self.geometry('500x700')
        # Title of size level info
        self.title('Sign up')
        
        self.__create_widgets()
        
    def __create_widgets(self):
        # Name
        ttk.Label(self, text='Name: ').grid(column=1, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=2, row=0, sticky=tk.W)
        
        # Family Name
        ttk.Label(self, text='Last name: ').grid(column=1, row=1, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=2, row=1, sticky=tk.W)
        
        # Phone number
        ttk.Label(self, text='Phone number: ').grid(column=1, row=2, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=2, row=2, sticky=tk.W)
        
        # ID--> کد ملی
        ttk.Label(self, text='ID: ').grid(column=1, row=3, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=2, row=3, sticky=tk.W)
        
        # Email
        ttk.Label(self, text='Email: ').grid(column=1, row=4, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=2, row=4, sticky=tk.W)
        
        # Password
        ttk.Label(self, text='Password: ').grid(column=1, row=5, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=2, row=5, sticky=tk.W)
        
        # Repeat Password
        ttk.Label(self, text='Repeat password: ').grid(column=1, row=6, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=2, row=6, sticky=tk.W)
        
        # Sing up button
        ttk.Button(self, text='Sign Up',).grid(column=2, row=8)
        
        for widget in self.winfo_children():
            widget.grid(padx=20, pady=5)

class Window_Order(tk.Toplevel):
    """
    this window appear if customer login befor, it will order
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        # Size of the top level info
        self.geometry('500x700')
        # Title of size level info
        self.title('Amiranfood Restaurent')


       # create a notebook
        notebook = ttk.Notebook(self)
        notebook.grid(column=0, row=0)
        # create frames
        self.frame1 = ttk.Frame(notebook, width=400, height=280)
        self.frame2 = ttk.Frame(notebook, width=400, height=280)
        self.frame3 = ttk.Frame(notebook, width=400, height=280)
        self.frame1.grid(column=0, row=0)
        self.frame2.grid(column=0, row=0)
        self.frame3.grid(column=0, row=0)
        # add frames to notebook
        notebook.add(self.frame1, text='Shop')
        notebook.add(self.frame2, text='Profile')
        notebook.add(self.frame3, text='Shopping cart')        
        self.__create_widgets_Shop()
        self.__create_widgets_Profile()
        self.__create_widgets_Shopping_cart()
        
    def __create_widgets_Shop(self):
        
        # Add Calendar
        cal = Calendar(self.frame1, selectmode = 'day',
                       year = 2021, month = 7,day = 4)
        cal.grid(column=2, row=0,padx=0, pady=5)

        def grad_date():
            """
            To get date that have beenn choosen
            """
            date.config(text = "Selected Date is: " + cal.get_date())
        Button(self.frame1, text = "Get Date",
               command = grad_date).grid(column=2, row=1,padx=0, pady=5)
        date = Label(self.frame1, text = "")
        date.grid(column=3, row=1,padx=0, pady=5)
        
        Search=Label(self.frame1, text='Amiran Resturent ',font=("Helvetica", 20)).grid(column=0, row=0, sticky=tk.W,padx=100, pady=50)
        
        # search Box
        Search=Label(self.frame1, text='Search: ').grid(column=0, row=1, sticky=tk.W,padx=100, pady=50)
        Search_box = Entry(self.frame1, width=20)
        Search_box.focus()
        Search_box.grid(column=1, row=1, sticky=tk.W,padx=0, pady=50)
        
        # Add food list
        ## Add drink
        A0 = Label(self.frame1, text = "Drinks").grid(column=0, row=2,padx=0, pady=5)
        A1 = Label(self.frame1, text = "A1").grid(column=0, row=3,padx=0, pady=5)
        A1_current_value = tk.StringVar()
        A1_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A1_current_value,wrap=True).grid(column=1, row=3, sticky=tk.W)

        A2 = Label(self.frame1, text = "A2").grid(column=0, row=4,padx=0, pady=5)
        A2_current_value = tk.StringVar()
        A2_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A2_current_value,wrap=True).grid(column=1, row=4, sticky=tk.W)   
  

        A3 = Label(self.frame1, text = "A3").grid(column=0, row=5,padx=0, pady=5)
        A3_current_value = tk.StringVar()
        A3_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A3_current_value,wrap=True).grid(column=1, row=5, sticky=tk.W)

        A4 = Label(self.frame1, text = "A4").grid(column=0, row=6,padx=0, pady=5)
        A4_current_value = tk.StringVar()
        A4_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A4_current_value,wrap=True).grid(column=1, row=6, sticky=tk.W)
        
        A5 = Label(self.frame1, text = "A5").grid(column=0, row=7,padx=0, pady=5)
        A5_current_value = tk.StringVar()
        A5_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A5_current_value,wrap=True).grid(column=1, row=7, sticky=tk.W)

        A6 = Label(self.frame1, text = "A6").grid(column=0, row=8,padx=0, pady=5)
        A6_current_value = tk.StringVar()
        A6_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A6_current_value,wrap=True).grid(column=1, row=8, sticky=tk.W)
        
        A7 = Label(self.frame1, text = "A7").grid(column=0, row=9,padx=0, pady=5)
        A7_current_value = tk.StringVar()
        A7_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A7_current_value,wrap=True).grid(column=1, row=9, sticky=tk.W)

        A8 = Label(self.frame1, text = "A8").grid(column=0, row=10,padx=0, pady=5)
        A8_current_value = tk.StringVar()
        A8_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A8_current_value,wrap=True).grid(column=1, row=10, sticky=tk.W)

        A9 = Label(self.frame1, text = "A9").grid(column=0, row=11,padx=0, pady=5)
        A9_current_value = tk.StringVar()
        A9_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A9_current_value,wrap=True).grid(column=1, row=11, sticky=tk.W)

        A10 = Label(self.frame1, text = "A10").grid(column=0, row=12,padx=0, pady=5)
        A10_current_value = tk.StringVar()
        A10_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=A10_current_value,wrap=True).grid(column=1, row=12, sticky=tk.W)
        
        ## Add Food
        B0 = Label(self.frame1, text = "Food").grid(column=2, row=2,padx=100, pady=5)
        B1 = Label(self.frame1, text = "B1").grid(column=2, row=3,padx=100, pady=5)
        B1_current_value = tk.StringVar()
        B1_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B1_current_value,wrap=True).grid(column=3, row=3, sticky=tk.W)
        B1 = Label(self.frame1, text = "B1").grid(column=3, row=3,padx=100, pady=5)
           
        B2 = Label(self.frame1, text = "B2").grid(column=2, row=4,padx=100, pady=5)
        B2_current_value = tk.StringVar()
        B2_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B2_current_value,wrap=True).grid(column=3, row=4, sticky=tk.W)   
        B2 = Label(self.frame1, text = "B1").grid(column=3, row=4,padx=100, pady=5)
        
        B3 = Label(self.frame1, text = "B3").grid(column=2, row=5,padx=100, pady=5)
        B3_current_value = tk.StringVar()
        B3_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B3_current_value,wrap=True).grid(column=3, row=5, sticky=tk.W)
        B3 = Label(self.frame1, text = "B1").grid(column=3, row=5,padx=100, pady=5)
        
        B4 = Label(self.frame1, text = "B4").grid(column=2, row=6,padx=100, pady=5)
        B4_current_value = tk.StringVar()
        B4_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B4_current_value,wrap=True).grid(column=3, row=6, sticky=tk.W)
        B4 = Label(self.frame1, text = "B1").grid(column=3, row=6,padx=100, pady=5)
        
        B5 = Label(self.frame1, text = "B5").grid(column=2, row=7,padx=100, pady=5)
        B5_current_value = tk.StringVar()
        B5_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B5_current_value,wrap=True).grid(column=3, row=7, sticky=tk.W)
        B5 = Label(self.frame1, text = "B1").grid(column=3, row=7,padx=100, pady=5)
        
        B6 = Label(self.frame1, text = "B6").grid(column=2, row=8,padx=100, pady=5)
        B6_current_value = tk.StringVar()
        B6_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B6_current_value,wrap=True).grid(column=3, row=8, sticky=tk.W)

        B7 = Label(self.frame1, text = "B7").grid(column=2, row=9,padx=100, pady=5)
        B7_current_value = tk.StringVar()
        B7_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B7_current_value,wrap=True).grid(column=3, row=9, sticky=tk.W)
        B7 = Label(self.frame1, text = "B7").grid(column=3, row=9,padx=200, pady=5)
        
        B8 = Label(self.frame1, text = "B8").grid(column=2, row=10,padx=100, pady=5)
        B8_current_value = tk.StringVar()
        B8_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B8_current_value,wrap=True).grid(column=3, row=10, sticky=tk.W)
        B8 = Label(self.frame1, text = "B8").grid(column=3, row=10,padx=200, pady=5)
        
        B9 = Label(self.frame1, text = "B9").grid(column=2, row=11,padx=100, pady=5)
        B9_current_value = tk.StringVar()
        B9_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B9_current_value,wrap=True).grid(column=3, row=11, sticky=tk.W)
        B9 = Label(self.frame1, text = "B9").grid(column=3, row=11,padx=200, pady=5)
        
        
        B10 = Label(self.frame1, text = "B10").grid(column=2, row=12,padx=100, pady=5)
        B10_current_value = tk.StringVar()
        B10_spin_box = ttk.Spinbox(self.frame1,from_=0,to=40,values=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40),
            textvariable=B10_current_value,wrap=True).grid(column=3, row=12, sticky=tk.W)
        B10 = Label(self.frame1, text = "B10").grid(column=3, row=12,padx=200, pady=5)
        

    def __create_widgets_Shopping_cart(self):

        # Title of showing cost table
        Items=Label(self.frame3,text="Items").grid(column=0, row=0,padx=20, pady=10)
        Number_Items=Label(self.frame3,text="number of items").grid(column=1, row=0,padx=20, pady=10)
        Number_Total_cost=Label(self.frame3,text="number of items").grid(column=2, row=0,padx=20, pady=10)
        # Showing cost
        food_cost_na=Label(self.frame3,text="Food cost").grid(column=0, row=1,padx=20, pady=10)
        food_cost_nu=Label(self.frame3,text="?").grid(column=1, row=1,padx=20, pady=10)
        food_cost=Label(self.frame3,text="?").grid(column=2, row=1,padx=20, pady=10)

        Drink_cost_na=Label(self.frame3,text=" Drink cost").grid(column=0, row=2,padx=20, pady=10)
        Drink_cost_nu=Label(self.frame3,text="?").grid(column=1, row=2,padx=20, pady=10)
        Drink_cost=Label(self.frame3,text="?").grid(column=2, row=2,padx=20, pady=10)

        Total_cost=Label(self.frame3,text="Total cost").grid(column=0, row=3,padx=20, pady=10)
        Total_cost_nu=Label(self.frame3,text="?").grid(column=1, row=3,padx=20, pady=10)

        Discount_code=Label(self.frame3,text="Discount code").grid(column=0, row=4,padx=20, pady=10)
        Discount_code_nu = ttk.Entry(self.frame3, width=30)
        Discount_code_nu.focus()
        Discount_code_nu.grid(column=1, row=4,padx=20, pady=10)
        
        Discount_cost=Label(self.frame3,text="Discount cost").grid(column=0, row=5,padx=20, pady=10)
        Discount_cost_nu=Label(self.frame3,text="?").grid(column=1, row=5,padx=20, pady=10)

        Final_cost=Label(self.frame3,text="Final cost").grid(column=0, row=6,padx=20, pady=10)
        Final_cost_nu=Label(self.frame3,text="?").grid(column=1, row=6,padx=20, pady=10)

        # Receipt
        Receipt=Label(self.frame3,text="Final cost").grid(column=4, row=0,padx=20, pady=10)
        Receipt_=Label(self.frame3,text="=================").grid(column=4, row=1,padx=20, pady=10)
        Receipt_=Label(self.frame3,text="Bill").grid(column=4, row=2,padx=20, pady=10)
        Receipt_=Label(self.frame3,text="=================").grid(column=4, row=3,padx=20, pady=10)

        # LIST OF ITEM MUST SHOW HERE
        
        #for item in list_of_item:
            #Label(self.frame3,text=f"{item}").grid(column=4, row=4+list_of_item.index(item),padx=20, pady=10)
        #for cost in cost_of_item:
            #Label(self.frame3,text=f"{cost}").grid(column=6, row=4+cost_of_item.index(cost),padx=20, pady=10)
        #for number in number_of_item:
            #Label(self.frame3,text=f"{number}").grid(column=5, row=4+number_of_item.index(number),padx=20, pady=10)

        # Customer advises
        Suggestions_label=Label(self.frame3,text="Suggestions").grid(column=5, row=0,padx=20, pady=10)
        Suggestions_text = Text(self.frame3, height=8).grid(column=5, row=1,padx=20, pady=10)
        Suggestions_text.insert('1.0', 'Write your suggestion here')


        def reset():
            """
            ALL THING MUST RETURN TO 0
            """
            m=askyesno(title="SYSTEM ALERT",
                    message= "Are You Sure Reset All..! \n")
            if m == 1:
                "EVERY THING MUST BE 0"
            else:
                showinfo("SYSTEM ALERT", "Canceled")

        def Show_cost():
            """
            CALCULATE EVERY THING
            """
            pass
        
        def pay_online():
            pass

        def pay_ofline():
            pass
        
        Button_reset=ttk.Button(self.frame3,text="Reset",command=reset).grid(column=0, row=7,padx=20, pady=10)
        Button_calculate_cost=ttk.Button(self.frame3,text="Calculate",command=Show_cost).grid(column=1, row=7,padx=20, pady=10)
        Button_pay_online=ttk.Button(self.frame3,text="Pay online",command=pay_online).grid(column=2, row=7,padx=20, pady=10)
        Button_reset=ttk.Button(self.frame3,text="Pay ofline",command=pay_ofline).grid(column=3, row=7,padx=20, pady=10)


            
    def __create_widgets_Profile(self):
        # Name
        ttk.Label(self.frame2, text='Name: ').grid(column=1, row=0, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=0, sticky=tk.W)
        
        # Family Name
        ttk.Label(self.frame2, text='Last name: ').grid(column=1, row=2, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=2, sticky=tk.W)
        
        # Phone number
        ttk.Label(self.frame2, text='Phone number: ').grid(column=1, row=4, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=4, sticky=tk.W)
        
        # ID--> کد ملی
        ttk.Label(self.frame2, text='ID: ').grid(column=1, row=6, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=6, sticky=tk.W)
        
        # Email
        ttk.Label(self.frame2, text='Email: ').grid(column=1, row=8, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=8, sticky=tk.W)
        
        # Password
        ttk.Label(self.frame2, text='Password: ').grid(column=1, row=10, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=10, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=20, pady=5)

    
        
class Window_boss(tk.Toplevel):
    """
    this window appear if boss login 
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        # Size of the top level info
        self.geometry('500x700')
        # Title of size level info
        self.title('Amiranfood Restaurent')

       # create a notebook
        notebook = ttk.Notebook(self)
        notebook.grid(column=0, row=0)
        # create frames
        self.frame1 = ttk.Frame(notebook, width=400, height=280)
        self.frame2 = ttk.Frame(notebook, width=400, height=280)
        
        self.frame1.grid(column=0, row=0)
        self.frame2.grid(column=0, row=0)
        
        # add frames to notebook
        notebook.add(self.frame1, text='Menue and Orders')
        notebook.add(self.frame2, text='Resturent Profile')
        

        
        self.__create_widgets_Menue_and_Orders()
        self.__create_widgets_Resturent_Profile()
        
        
    def __create_widgets_Menue_and_Orders(self):
        #Title
        Label(self.frame1, text = "Inventory").grid(column=0, row=0,padx=0, pady=5)
        Label(self.frame1, text = "Name").grid(column=0, row=1,padx=0, pady=5)
        Label(self.frame1, text = "Number").grid(column=1, row=1,padx=0, pady=5)
        Label(self.frame1, text = "Present number").grid(column=2, row=1,padx=0, pady=5)
        Label(self.frame1, text = "Supply price").grid(column=3, row=1,padx=0, pady=5)
        Label(self.frame1, text = "Sale price").grid(column=4, row=1,padx=0, pady=5)
        # A1
        Label(self.frame1, text = "A1").grid(column=0, row=2,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=2,padx=0, pady=5)
        A1=ttk.Entry(self.frame1, width=30)
        A1.focus()
        A1.grid(column=2, row=2,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=2,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=2,padx=0, pady=5)
        # A2
        Label(self.frame1, text = "A2").grid(column=0, row=3,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=3,padx=0, pady=5)
        A2=ttk.Entry(self.frame1, width=30)
        A2.focus()
        A2.grid(column=2, row=3,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=3,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=3,padx=0, pady=5)
        # A3
        Label(self.frame1, text = "A3").grid(column=0, row=4,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=4,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=4,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=4,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=4,padx=0, pady=5)
        # A4
        Label(self.frame1, text = "A4").grid(column=0, row=5,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=5,padx=0, pady=5)
        A4=ttk.Entry(self.frame1, width=30)
        A4.focus()
        A4.grid(column=2, row=5,padx=0, pady=5)
        Label(self.frame1, text = "Present number")
        Label(self.frame1, text = "?").grid(column=3, row=5,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=5,padx=0, pady=5)
        # A5
        Label(self.frame1, text = "A5").grid(column=0, row=6,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=6,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=6,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=6,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=6,padx=0, pady=5)
        # A6
        Label(self.frame1, text = "A6").grid(column=0, row=7,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=7,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=7,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=7,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=7,padx=0, pady=5)
        # A7
        Label(self.frame1, text = "A7").grid(column=0, row=8,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=8,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=8,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=8,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=8,padx=0, pady=5)
        # A8
        Label(self.frame1, text = "A8").grid(column=0, row=9,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=9,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=9,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=9,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=9,padx=0, pady=5)
        # A9
        Label(self.frame1, text = "A9").grid(column=0, row=10,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=10,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=10,padx=0, pady=5)
        Label(self.frame1, text = "Present number")
        Label(self.frame1, text = "?").grid(column=3, row=10,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=10,padx=0, pady=5)
        # A10
        Label(self.frame1, text = "A10").grid(column=0, row=11,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=11,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=11,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=11,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=11,padx=0, pady=5)
        # B1
        Label(self.frame1, text = "B1").grid(column=0, row=12,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=12,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=12,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=12,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=12,padx=0, pady=5)
        # B2
        Label(self.frame1, text = "B2").grid(column=0, row=13,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=13,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=13,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=13,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=13,padx=0, pady=5)
        # B3
        Label(self.frame1, text = "B3").grid(column=0, row=14,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=14,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=14,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=14,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=14,padx=0, pady=5)
        # B4
        Label(self.frame1, text = "B4").grid(column=0, row=15,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=15,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=15,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=15,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=15,padx=0, pady=5)
        # B5
        Label(self.frame1, text = "B5").grid(column=0, row=16,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=16,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=16,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=16,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=16,padx=0, pady=5)
        # B6
        Label(self.frame1, text = "B6").grid(column=0, row=17,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=17,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=17,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=17,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=17,padx=0, pady=5)
        # B7
        Label(self.frame1, text = "B7").grid(column=0, row=18,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=18,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=18,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=18,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=18,padx=0, pady=5)
        # B8
        Label(self.frame1, text = "B8").grid(column=0, row=19,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=19,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=19,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=19,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=19,padx=0, pady=5)
        # B9
        Label(self.frame1, text = "B9").grid(column=0, row=20,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=20,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=20,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=20,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=20,padx=0, pady=5)
        # B10
        Label(self.frame1, text = "B10").grid(column=0, row=21,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=1, row=21,padx=0, pady=5)
        A3=ttk.Entry(self.frame1, width=30)
        A3.focus()
        A3.grid(column=2, row=21,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=3, row=21,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=4, row=21,padx=0, pady=5)

        # Total Statistic
        Label(self.frame1, text = "Total Statistic").grid(column=5, row=0,padx=0, pady=5)
        Label(self.frame1, text = "Total Sale").grid(column=5, row=1,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=5, row=2,padx=0, pady=5)
        Label(self.frame1, text = "Profit").grid(column=6, row=1,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=6, row=2,padx=0, pady=5)
        Label(self.frame1, text = "Sent").grid(column=7, row=1,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=7, row=2,padx=0, pady=5)
        Label(self.frame1, text = "Check out").grid(column=8, row=1,padx=0, pady=5)
        Label(self.frame1, text = "?").grid(column=8, row=2,padx=0, pady=5)

        
        #Suggestion
        Label(self.frame1, text = "Suggestions").grid(column=5, row=4,padx=0, pady=5)
        Label(self.frame1, text = ".......").grid(column=5, row=5,padx=0, pady=5)

        # Check out
        Label(self.frame1, text = "Check out").grid(column=10, row=0,padx=0, pady=5)
        Label(self.frame1, text = ".........................").grid(column=10, row=1,padx=0, pady=5)
        def send():
            """
            after pushing button, check out will send
            """
            pass
        send_button = ttk.Button(self.frame1,text='send',command=send)
        send_button.grid(column=11, row=1, sticky=tk.W)
        
        
        #Sent
        Label(self.frame1, text = "Sent").grid(column=9, row=0,padx=0, pady=5)
        Label(self.frame1, text = ".........................").grid(column=9, row=1,padx=0, pady=5)


    def __create_widgets_Resturent_Profile(self):
        # Boss Name
        ttk.Label(self.frame2, text='Boss name: ').grid(column=1, row=0, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=0, sticky=tk.W)
        # Boss Last name
        ttk.Label(self.frame2, text='Boss Last name: ').grid(column=1, row=1, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=1, sticky=tk.W)
        # Region name
        ttk.Label(self.frame2, text='Region name: ').grid(column=1, row=2, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=2, sticky=tk.W)
        # Resturant name
        ttk.Label(self.frame2, text='Resturant name: ').grid(column=1, row=3, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=3, sticky=tk.W)
        # Resturant address
        ttk.Label(self.frame2, text='Resturant address: ').grid(column=1, row=4, sticky=tk.W)
        keyword = ttk.Entry(self.frame2, width=30)
        keyword.focus()
        keyword.grid(column=2, row=4, sticky=tk.W)
        # Upload Menu
        def select_image():
            # Select the Imagename  from a folder
            x = openfilename()
            # opens the image
            img = Image.open(x)
            # resize the image and apply a high-quality down sampling filter
            img = img.resize((300,300), Image.ANTIALIAS)
            # PhotoImage class is used to add image to widgets, icons etc
            img = ImageTk.PhotoImage(img)
            # create a label
            panel = Label(self.frame2, image = img)
            # set the image as img
            panel.image = img
            panel.grid(column=2, row=6, sticky=tk.W,padx=10, pady=5)

        def openfilename():
            # open file dialog box to select image
            # The dialogue box has a title "Open"
            filename = filedialog.askopenfilename(title ='"pen')
            return filename
          
        ## open Menue button
        open_button = ttk.Button(self.frame2,text='Open a image',command=select_image)
        open_button.grid(column=2, row=5, sticky=tk.W)
        for widget in self.winfo_children():
            widget.grid(padx=20, pady=5)
        
             
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Defining title window
        self.title('Amiranfood')
        # Define size of window
        self.geometry('500x400')
        # Make window un resizeable
        self.resizable(False, False)
        # windows only (remove the minimize/maximize button)
        self.attributes('-toolwindow', True)
        # layout on the root window
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        
        # Runiing function
        self.__create_widgets()

    def __create_widgets(self):
        """
        This function define place for each frame
        """
        # create the input frame
        input_frame = InputFrame_Email_pass(self)
        input_frame.grid(column=0, row=1)

        # create the button frame
        button_frame = ButtonFrame_login(self)
        button_frame.grid(column=0, row=2)
        
        # create the Welcome frame
        welcom_frame = welcome_frame(self)
        welcom_frame.grid(column=0, row=0)
        
    
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
