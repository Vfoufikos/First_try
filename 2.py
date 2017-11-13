from turtle import *
from tkinter import*
from random import *
import time 

class MyApp: 
	def __init__(self, myParent):
		self.p=myParent
		self.f1=Frame(myParent) #plaisio
		self.f1.pack()
		self.w= Label(self.f1, text="Put text bellow:", font="Arial 24")
		self.w.pack()

		self.message= Button(self.f1 , text="show text ",font="Arial 30", bg="red",command=self.showText)
		
		self.entry=Entry(self.f1, font="Arial 24")
		self.entry.pack(fill=BOTH, expand=1)

		self.b= Button(self.f1 , text="Exit",font="Arial 30", bg="red",command=self.buttonPushed)
		self.b.pack(fill=BOTH, expand=2)

	def buttonPushed(self): #event handler for push b
		self.p.destroy()	#close window

	def showText(self):
		text=self.entry.get()
		print(text)

#-----------------

root= Tk()
root.title("Example1")
myapp= MyApp(root)
root.mainloop()