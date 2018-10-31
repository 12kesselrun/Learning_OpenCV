import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
x=0
y=0

def save_vals():
	# If you want to adjust global variables in a function you need to declare that you want to use the globals and not the locals
	global x
	global y
	# Set x and y to the values of the w1 and w2 sliders
	x=w1.get()
	y=w2.get()
	# End the tkinter method and move past the blocking line: top.mainloop()
	top.destroy()

# Start a tkinter object (show a GUI)
top = Tk()
top.geometry("200x200")
# Add scales to the object and pack them into it
w1 = Scale(top, from_=0, to=300, orient=HORIZONTAL)
w1.pack()
w2 = Scale(top, from_=0, to=300, orient=HORIZONTAL)
w2.pack()
# Add a save button
Button(top, text='Save', command=save_vals).pack()

# Blocks so that the GUI stays onscreen
top.mainloop()

# Do some openCV image processing1
img = cv2.imread('shapes.JPG',0)
print("X:",x,"Y:",y)
edges=cv2.Canny(img,x,y)
cv2.imshow("Edges",edges)
cv2.waitKey(4000)
cv2.destroyAllWindows()
