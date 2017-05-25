from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        
        self.master.title("Invenger")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.client_exit)
        saveButton = Button(self, text = "Save Inventory", command=self.client_save)
        addButton = Button(self, text = "Add Item", )
        
        quitButton.place(x=0, y=0)
        saveButton.place(x=200, y=0)
        addButton.place(x=300, y=0)
       
        item_name = Entry(root)


        item_name.place (x=100, y= 200)
        
        menu= Menu(self.master)
        self.master.config(menu=menu)

        file= Menu(menu)

        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='Save Inventory', )

        menu.add_cascade(label="File", menu=file)

        edit= Menu(menu)
        edit.add_command(label="undo",)
        edit.add_command(label="show Image", command=self.showImg())
        edit.add_command(label="show Text", command=self.showTxt())

        menu.add_cascade(label="Edit", menu=edit)
    

    def showImg(self):
        load= Image.open('warehouse.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image= render
        img.place(x=0, y=200)

    def showTxt(self):
        text = Label(self, text='hey clean warehouse')
        text.pack()

    def client_save(self):
        import Inventorycounter
        Inventorycounter.inv_db()
    def client_exit(self):
        exit()

root = Tk()
root.geometry("1024x600")
app = Window(root)

root.mainloop()    