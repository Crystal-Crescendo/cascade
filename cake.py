import tkinter as tk
from time import sleep
from random import randint
# Useful functions
def kWO(root,ms): # Acronym for "keep Window Open"
    for t in range(ms):
            sleep(.01)
            root.update_idletasks()
            root.update() 
def event1(textInput):
    text = textInput.get().lower()
    if text=="skip" or text=="quit" or text=="stop" or text=="die":
        return 0
    elif text=="live":
        return 1
    elif text=="meow":
        return 2
def new(* args):
    print("WAOWOWAOWOAOWAOWOAWAO")
    newWindow = tk.Tk()
    newWindow.geometry("300x200")
    popup = tk.Message(newWindow)
    popup.configure(width=80,text="STOP IT")
    popup.pack()
    kWO(newWindow,randint(200,1000))
    newWindow.quit()
# Screen
screen = tk.Tk()
screen.configure(height=400,width=400,background="WHITE")
screen.title("hi")

# Bootup
textInput = tk.Entry(screen)
textInput.configure(foreground="RED")
textInput.pack(side="bottom",pady=10)

text = tk.Text(screen)
text.configure(width=300,height=300)
text.pack()
added_text = ["HELLO!!!!","\nIT'S OMG ITS WORKING WAOWOWOWW","\nI'm actually learning something USEFUL holy shit :3","\nCOUGH","\nCOUGH","\nOK so like what do i Do again"]
for i in range(len(added_text)):
    text.insert(tk.END,added_text[i])
    kWO(screen,100)
    x = event1(textInput)
    if x==0:
        break
    elif x==1:
        for i in added_text:
            i += " yay!@"
    elif x==2:
        for i in added_text:
            i = "meow"
            
# DESTROY ITTT AAGHH GET OUT OF HERE

textInput.delete(0,len(textInput.get()))
kWO(screen,300)
text.insert(tk.END,"\nBleh .u.\n my stomuch hurt :<")
kWO(screen,200)
text.destroy()



# Anyways, the actual app i think idk :3
text = tk.Text(screen)
text.configure(width=100,height=50,pady=10)
text.pack(side="top")


button = tk.Button(screen,text="CLICK ME",command=new())
button.configure(width=50,height=50)



spam = "I dont want to die"
button.pack(side="left")

for i in range(2000):
    text.insert(tk.END,spam)
    kWO(screen,1)
    # change the flavor text
    x = event1(textInput)
    if x==0:
        break
    elif x==1:
        spam = "yay"
    elif x==2:
        spam = "meow"
    
    # if the button gets pressed do some bullshit
    
screen.quit()


# End
screen.mainloop()
