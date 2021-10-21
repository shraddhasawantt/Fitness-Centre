import os
import pickle

details_list=[]

def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



class New_Toplevel:

    def __init__(self):
        def confirm():
            self.choice = str(self.data1.get())
            v = int(self.choice)
            wb = open("database.txt", "a")
            wb.write("\n\nPlan Selected: ")
            if v == 1:
                wb.write("Personal Trainer \n")
                self.Text1.insert(INSERT, " It'll be 15000 Rs. \n The Trainer will guide you with your workout")
            elif v == 2:
                wb.write("Weight Loss \n")
                self.Text1.insert(INSERT, " It'll be 12000 Rs. \n Your Workout Routine will be whatsapped to you")
            elif v == 3:
                wb.write("Bulking \n")
                self.Text1.insert(INSERT, " It'll be 10000 Rs. \n Your Workout Routine will be whatsapped to you")
            elif v == 4:
                wb.write("Build \n")
                self.Text1.insert(INSERT, " It'll be 8000 Rs. \n Your Workout Routine will be whatsapped to you")


        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1011x750")
        root.title("FITNESS HUB")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)


        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.05, rely=0.03, height=47, width=400)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''1. Personal Trainer''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.045, rely=0.10, height=47, width=400)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#bfbfbf")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''2. Weight Loss ''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.04, rely=0.17, height=47, width=400)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''3. Bulking ''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.035, rely=0.24, height=47, width=400)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''4. Maintain ''')

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.03, rely=0.31, height=47, width=289)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Your Choice: ''')

        self.Entry1 = Entry(self.Frame1)
        self.data1=StringVar()
        self.Entry1.place(relx=0.35, rely=0.32,height=34, relwidth=0.43)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.data1)


        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.05, rely=0.54, relheight=0.4, relwidth=0.89)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.34, rely=0.40, height=93, width=286)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Confirm''')
        self.Button1.configure(command=confirm)
        root.mainloop()



if __name__ == '__main__':
    out=New_Toplevel()
