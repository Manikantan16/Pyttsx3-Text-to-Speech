import pyttsx3
from tkinter import*
import tkinter as tk
from tkinter import ttk
import time 
from tkinter import messagebox
import datetime as dt

root = Tk()
root.geometry('900x430+200+200')
root.configure(bg='lightgreen')
root.title('Google Text to Speech')
root.resizable(False,False)

audio = pyttsx3.init()
voice = audio.getProperty('voices')

def gettime():
    date = dt.datetime.now()
    # Takes the date and formats it.
    format_date = f"{date:%a, %b %d %Y}"
    strtime = format_date +" "+ time.strftime('%H:%M:%S %p')
    Label_time.config(text=strtime)
    Label_time.after(1000,gettime)

def Convert_TexttoSpeech():
    if text_area.compare("end-1c", "==", "1.0"):
        messagebox.showerror("Error", "Text field can not be blank.")
        return
    
    text = text_area.get(1.0,END)
    if len(text) > 5:
        if(CmbGender.get() == 'Male'):
            if(CmbSpeed.get() == 'Normal'):
                audio.setProperty('rate',150)
            elif(CmbSpeed.get() == 'Fast'):
                audio.setProperty('rate',250)
            else:
                audio.setProperty('rate',60)
            audio.setProperty('voice', voice[0].id) 
            
        else:
            if(CmbSpeed.get() == 'Normal'):
                audio.setProperty('rate',150)
            elif(CmbSpeed.get() == 'Fast'):
                audio.setProperty('rate',250)
            else:
                audio.setProperty('rate',60)
            audio.setProperty('voice', voice[1].id) 
    audio.say(text)
    audio.runAndWait()
    
    

lbltitle = Label(root,text='TEXT TO SPEECH RECOGNITION SYSTEM',relief=RIDGE,background='darkgreen',foreground='white',font=('Arial',20,"bold"),padx=2,pady=4)
lbltitle.pack(side=TOP,fill=X)


Label_time = Label(root,text='',font="helvetica 9 bold italic",foreground="black",background="lightgreen",width=30)
Label_time.place(x=700,y=50)


LblTxtArea = Label(root,text='ENTER THE TEXT',font=('Arial',14,'bold'),bg='lightgreen',fg='black').place(x=150,y=70)

text_area = Text(root,font="Robote 14",bg='white',relief=GROOVE,wrap=WORD)
text_area.place(x=20,y=100,width=450,height=250)



LblVoice = Label(root,text='VOICE',font=('Arial',10,'bold'),bg='lightgreen',fg='black').place(x=560,y=155)
LblSpeed = Label(root,text='SPEED',font=('Arial',10,'bold'),bg='lightgreen',fg='black').place(x=700,y=155)

CmbGender = ttk.Combobox(root,values=['Male','Female'],font=('Arial',10,'bold'),state='r',width=10)
CmbGender.place(x=540,y=180)
CmbGender.set('Male')

CmbSpeed = ttk.Combobox(root,values=['Fast','Normal','Slow'],font=('Arial',10,'bold'),state='r',width=10)
CmbSpeed.place(x=680,y=180)
CmbSpeed.set('Normal')

btnPlay = Button(root,text="Play",font=('arial',12,"bold"),bg='#39c790',fg='white',width=23,command=Convert_TexttoSpeech)
btnPlay.place(x=540,y=220)

LblInfo = Label(root,text='key   in a minimum of   5   (Characters)',font=('calibri',8,'italic','bold'),bg='lightgreen',fg='red').place(x=295,y=350)

LblSignature = Label(root,text='Designed by: Manikantan....',font=('calibri',8,'italic','bold'),bg='lightgreen',fg='black').place(x=755,y=410)
gettime()
root.mainloop()


