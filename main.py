from stack import Stack
from tkinter import *
from tkinter import ttk, messagebox, Canvas

appStack = Stack(6)

root = Tk()
# root.geometry
frame = ttk.Frame(root, padding=12)
frame.grid()

canvas = Canvas(frame, background="floral white")
canva.grid(column=0, row=0, columspan=10, rowspan=10)

# initial values
pad = 3
hWidth = 140
candyHeight = 20
x0 = 120+pad
x1 = x0-pad+hWidth-pad
y0 = 10+pad
y1 = y0+candyHeight+pad
step = 25

canvas.create_line(120, 10, 120, 260, width = 2)
canvas.create_line(120, 260, 120+hWidth, 10, width =2)
canvas.create_line(120+hWidth, 260, 120+hWidth, 10, width=2)

# spring
left = 120+pad
right = 120-pad+hWidth
bottom = 260-pad
springTags = []

#
