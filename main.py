from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def fileOpen():
    global name, img, img2, img3, img4, img5

    name = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PNG files","*.png"),("all files","*.*")))

    img = PhotoImage(file = name)
    img2 = PhotoImage(file = name)
    img3 = PhotoImage(file = name)
    img4 = PhotoImage(file = name)
    img5 = PhotoImage(file = name)

    size = "%sx%s"% (img.width(), img.height())
    window.geometry(size)
    displayImg.configure(image = img)
    displayImg.image = img

    for i in range(img.width()):
        for j in range(img.height()):
            (r, g, b) = img.get(i, j)
            avg = int((r + b + g) / 3)
            img2.put("#%02x%02x%02x"% (avg, avg, avg), (i, j))
            img3.put("#%02x%02x%02x"% (255, avg, avg), (i, j))
            img4.put("#%02x%02x%02x"% (avg, 255, avg), (i, j))
            img5.put("#%02x%02x%02x"% (avg, avg, 255), (i, j))

def fileSave():
    displayImg.image.write(name, format = "png")
    messagebox.showinfo("Save", "Successful!")

def fileSaveAS():
    f = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("PNG files","*.png"),("all files","*.*")))
    name = "%s.png"%f
    displayImg.image.write(name, format = "png")
    messagebox.showinfo("Save", "Successful!")

def normalImg():
    displayImg.configure(image = img)
    displayImg.image = img

def grayImg():
    displayImg.configure(image = img2)
    displayImg.image = img2

def redImg():
    displayImg.configure(image = img3)
    displayImg.image = img3

def greenImg():
    displayImg.configure(image = img4)
    displayImg.image = img4

def blueImg():
    displayImg.configure(image = img5)
    displayImg.image = img5

window = Tk()

window.geometry("500x500")
window.title("Photo")
window.iconbitmap("pikachu.ico")
displayImg = Label(window)

displayImg.pack()

name = ""
img = None
img2 = None
img3 = None
img4 = None
img5 = None

menubar = Menu(window)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open File..", command = fileOpen)
filemenu.add_separator()
filemenu.add_command(label = "Normal", command = normalImg)
filemenu.add_command(label = "Gray", command = grayImg)
filemenu.add_command(label = "Red", command = redImg)
filemenu.add_command(label = "Green", command = greenImg)
filemenu.add_command(label = "Blue", command = blueImg)
filemenu.add_separator()
filemenu.add_command(label = "Save", command = fileSave)
filemenu.add_command(label = "Save As...", command = fileSaveAS)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = window.quit)
menubar.add_cascade(label = "File", menu = filemenu)

window.config(menu = menubar)

window.mainloop()