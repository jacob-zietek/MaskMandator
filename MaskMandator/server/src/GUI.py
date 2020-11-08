import tkinter as tk
import cv2
from PIL import Image, ImageTk
from processUserInput import main as updateText

width, height = 800, 800
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())


label = tk.Label(root, text="Please take a photo of yourself")
label.pack()

lmain = tk.Label(root)
lmain.pack()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def takePicture():
    return_value, image = cap.read()
    cv2.imwrite('face.png', image) 
    label.config(text=updateText())
    label.update_idletasks()


button = tk.Button(
    text = "Take Picture",
    width = 25,
    height = 5,
    bg = "gray",
    fg = "white",
    command = takePicture
)





button.pack()

show_frame()
root.mainloop()

