import tkinter as tk
from tkcalendar import *
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import sqlite3
from tkinter import messagebox
import smtplib
import random
import time
import psycopg2
class ChatApp():
    def __init__(self,root):
        self.root=root
        self.root.title("Chat with your friends...")
        self.root.geometry('600x600+400+20')
        self.root.resizable(False,False)

        ####################################
        self.entry_var=StringVar()
        self.entry_name=StringVar()

        heading_label=Label(self.root,text="Chat Box.",font=("times new roman",15,'bold'),height=1).pack()
        self.text_box=Text(self.root,padx=10,bg='lightyellow')
        self.text_box.place(x=10,y=60,width=580)
        entry_name_label=Label(self.root,text=("Enter your name:"),font=(("times new roman"),10,'bold')).place(x=10,y=30)
        entry_name=ttk.Entry(self.root,textvariable=self.entry_name,width=50)
        entry_name.place(x=130,y=31)
        entry_box=ttk.Entry(self.root,width=96,textvariable=self.entry_var)
        entry_box.place(x=10,y=480)
        send_button=ttk.Button(self.root,text="Send message",width=96,command=self.send_message)
        send_button.place(x=10,y=520)
        self.feth_message()
        #self.text_box.insert("0.1","hi")
    def send_message(self):
        #global self.entry_name
        #self.text_box.insert("0.1",self.entry_var.get())
        #self.text_box.insert("0.1","UMESHA:   ")
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        if self.entry_var.get()=="":
            messagebox.showerror("Error","Plese enter the text in the entry box..")
        else:
            #self.entry_name="umesh"
            cur.execute("insert into ChatData (one_chat,send_data) values(%s,%s)",(
               self.entry_var.get(),
               self.entry_name.get()
            ))
            con.commit()
            messagebox.showinfo("Info","The the message is sended..")
            self.feth_message()
            con.close()
    def feth_message(self):
        
        #self.text_box.insert("0.1",self.entry_var.get())
        #self.text_box.insert("0.1","UMESHA:   ")
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            cur.execute('select * from ChatData')
            rows=cur.fetchall()
            self.text_box.insert("0.1",rows)
            
        except Exception as sr:
                messagebox.showerror('Error',f'Error due to {str(sr)}')



if __name__=='__main__':
    root=tk.Tk()
    ob1=ChatApp(root)
    root.mainloop() 