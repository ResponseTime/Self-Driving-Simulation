import tkinter as tk
from PIL import ImageTk, Image  

r = tk.Tk()
r.geometry("800x800")
r.title('Car MainLoop')
car_main = Image.open("./assets/car_top_view.png")
tkimage= ImageTk.PhotoImage(car_main)
label=tk.Label(r,image=tkimage)
label.place(relx=0.0, rely=10.0, anchor='sw')
label.pack()
r.mainloop()