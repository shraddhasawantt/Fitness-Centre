import os
import sys
import random
from subprocess import call


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
details_list=[]

def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]

class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO

class FITNESSHUB_checkin:

    def __init__(self):
        self.NAME=""
        self.ADDERESS=""
        self.MOBILE=""

        def chk_name():
            while True:

                self.k = self.name.get()

                a = self.k.isdigit()
                if len(self.k) != 0 and a != True:
                    self.NAME=self.k
                    self.Text1.insert(INSERT, "name has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid name""\n")
                    break

        def chk_add():
            while True:
                self.g = str(self.addr.get())


                ak = self.g.isdigit()
                if len(self.g)!= 0 and ak!=True:
                    self.ADDERESS=self.g
                    self.Text1.insert(INSERT, "address has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid address""\n")
                    break

        def chk_mo():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.Text1.insert(INSERT, "mobile number has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid mobile number""\n")
                break


        def enter(self):
            self.name = self.NAME
            self.address = self.ADDERESS
            self.mobile_no = self.MOBILE


        def submit_clicked():

            enter(self)
            details_list.append(self.name)
            details_list.append(self.address)
            details_list.append(self.mobile_no)
            wb = open("database.txt", "a")
            wb.write("\n \nCustomer Details: ")
            custID = random.randint(1000000,9999999)
            wb.write(str(custID) + "\n")
            for i in range(3):
                wb.write(details_list[i] + "\n")
            wb.close()

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
        font11 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1069x742")
        root.title("FITNESS HUB")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=995)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#ffffff")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''YOU CLICKED ON''')
        self.Message1.configure(width=496)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.52, rely=0.19, relheight=0.74, relwidth=0.07)
        self.Message2.configure(background="#ffffff")
        self.Message2.configure(font=font11)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#ffffff")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text=''':''')
        self.Message2.configure(width=66)

        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.57, rely=0.11, relheight=0.79, relwidth=0.35)
        self.Message3.configure(background="#ffffff")
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#ffffff")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''NEW CUSTOMER''')
        self.Message3.configure(width=347)

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=995)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.05, rely=0.03, height=47, width=289)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''ENTER YOUR NAME''')

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.045, rely=0.29, height=47, width=329)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''ENTER YOUR NUMBER''')



        self.Entry3 = Entry(self.Frame2)
        self.name=StringVar()
        self.Entry3.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#bfbfbf")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#ffffff")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#e6e6e6")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(textvariable=self.name)


        self.Entry4 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry4.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#bfbfbf")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#ffffff")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#e6e6e6")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(textvariable=self.mobile)

        self.Entry5 = Entry(self.Frame2)
        self.addr = StringVar()
        self.Entry5.place(relx=0.47, rely=0.18,height=34, relwidth=0.43)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#bfbfbf")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#ffffff")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#e6e6e6")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.configure(textvariable=self.addr)

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.045, rely=0.16, height=47, width=334)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''ENTER YOUR ADDRESS''')


        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=chk_name)

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=33, width=43)
        self.Button2.configure(activebackground="#ffffff")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#ffffff")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')
        self.Button2.configure(command=chk_add)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=33, width=43)
        self.Button3.configure(activebackground="#ffffff")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#ffffff")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''OK''')
        self.Button3.configure(command=chk_mo)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.76, rely=0.66, height=83, width=156)
        self.Button4.configure(activebackground="#ffffff")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font16)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#ffffff")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''SUBMIT''')
        self.Button4.configure(command=submit_clicked)



        root.mainloop()

if __name__ == '__main__':
    FIHUB=FITNESSHUB_checkin()
