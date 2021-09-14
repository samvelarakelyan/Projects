from tkinter import Label, Tk 
from time import strftime


window = Tk()
window.title("Digital Clock") 
window.geometry("495x150") 
window.resizable(1,1)


text_font = ("Boulder", 68, 'bold')
background = "#430909"
foreground = "#2A80E1"
border_width = 25


label = Label(window, font=text_font, bg=background,
                          fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digital_clock():
   time_live = strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)


digital_clock()


window.mainloop()
