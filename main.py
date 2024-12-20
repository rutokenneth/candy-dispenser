from stack import Stack
from tkinter import *
from tkinter import ttk, messagebox, Canvas

appStack = Stack(6)

root = Tk()
# root.geometry("400x300")
frame = ttk.Frame(root, padding=12)
frame.grid()

canvas = Canvas(frame, background="wheat")
canvas.grid(column=0, row=0, columnspan=10, rowspan=10)

# initial values
pad = 3
hWidth = 140
candyHeight = 20
x0 = 120 + pad
x1 = x0 - pad + hWidth - pad
y0 = 10 + pad
y1 = y0 + candyHeight + pad
step = 25

canvas.create_line(120, 10, 120, 260, width=2)
canvas.create_line(120, 260, 120 + hWidth, 10, width=2)
canvas.create_line(120 + hWidth, 260, 120 + hWidth, 10, width=2)

# spring
left = 120 + pad
right = 120 - pad + hWidth
bottom = 260 - pad
springTags = []


def refreshSpring():
    y_init = bottom
    squeeze = 40 - (appStack.getSize() * 4.2)

    try:
        for x in springTags:
            canvas.delete(x)
        springTags.clear()
    except Exception as e:
        print(e)

    springTags.append(canvas.create_line(x0, y_init, x1, y_init))  # bottom line

    for x in range(6):
        if x % 2 == 0:
            springTags.append(canvas.create_line(left, y_init, right, (y_init - squeeze)))
        else:
            springTags.append(canvas.create_line(left, (y_init - squeeze), right, y_init))
        y_init = y_init - squeeze

    springTags.append(canvas.create_line(left, y_init, right, y_init))  # top line


myTags = []
refreshSpring()


def _push():
    try:
        tag = "C" + str(appStack.top + 1)
        appStack.push(tag)
        refreshSpring()
        canvas.create_rectangle(x0, y0 + (step * appStack.top + 1), x1,
                                y1 + (step * appStack.top + 1), fill="dodgerblue", tags=tag)
        myTags.append(tag)
    except:
        messagebox.showerror(title='Error', message="Stack Full")


def _pop():
    try:
        canvas.delete(myTags.pop())
        appStack.pop()
        refreshSpring()
    except:
        messagebox.showerror(title='Error', message="Stack is empty")


def _peek():
    try:
        value = appStack.peek()
    except:
        messagebox.showerror(title='Error', message="Stack Empty")
    else:
        messagebox.showinfo(title='Peek', message="Top Value is " + str(value))


def refresh():
    for x in myTags:
        canvas.delete(x)


ttk.Label(frame, text="Candy Dispenser").grid(column=12, row=0)
ttk.Button(frame, text="Push", width=10, command=_push).grid(column=12, row=1)
ttk.Button(frame, text="Pop", width=10, command=_pop).grid(column=12, row=2)
ttk.Button(frame, text="Peek", width=10, command=_peek).grid(column=12, row=3)

root.mainloop()
