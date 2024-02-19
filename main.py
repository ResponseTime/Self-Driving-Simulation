import tkinter as tk
from PIL import ImageTk, Image


def left(e):
    x = -20
    y = 0
    canvas.move(img, x, y)


def right(e):
    x = 20
    y = 0
    canvas.move(img, x, y)


def up(e):
    x = 0
    y = -20
    canvas.move(img, x, y)


def down(e):
    x = 0
    y = 20
    canvas.move(img, x, y)


r = tk.Tk()
r.geometry("800x800")
r.title("Car MainLoop")
canvas = tk.Canvas(r, width=800, height=800, bg="white")
canvas.pack(pady=20)
image = ImageTk.PhotoImage(Image.open("./assets/car_top_view.png"))
img = canvas.create_image(250, 120, anchor="nw", image=image)

r.bind("<Left>", left)
r.bind("<Right>", right)
r.bind("<Up>", up)
r.bind("<Down>", down)

r.mainloop()
