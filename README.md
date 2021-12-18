# subdomain-finder
This is my own tool.But that is probably same any other tool.So,credit to everyone


# Digital clock in Tkinter ကျွန်တော်ရေးတာမဟုတ်ပါဘူး။ copy idea

from tkinter import *
import time

def clocktime(time1=''):
    time2=time.strftime('%H:%M:%S')
    if time2!=time1:
        time1=time2
        clock.config(text=time2)
        clock.after(200,clocktime)
        
x=Tk()
clock=Label(x,font='Verdana 15 bold', bg='black', fg = 'blue')
clock.pack(fill='both', expand=1)
clocktime()
x.mainloop()
