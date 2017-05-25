from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        
        self.master.title("Invenger")

        self.pack(fill=BOTH, expand=1)
        #Buttons
        quitButton = Button(self, text="Quit", command=self.client_exit)
        saveButton = Button(self, text = "Save Inventory", command=self.client_save)
        addButton = Button(self, text = "Add Item", )
        #Buttons Placements
        quitButton.place(x=0, y=0)
        saveButton.place(x=200, y=0)
        addButton.place(x=300, y=0)
       #Text Entry
        item_name = Entry(root)
        item_num = Entry(root)
        itemdescrip = Entry(root)
        #Text Entry Placements

        item_name.place (x=50, y= 50)
        item_num.place (x= 200, y= 50)
        itemdescrip.place (x=350, y= 50)
        
        #Text Labels
        item_name_label = Label(root, text= "Item Name")
        item_num_label = Label(root, text = "Item Number")
        itemdescriplabel= Label(root, text = "Item Description")
        #Text Labels Placements
        item_name_label.place(x = 25, y= 25)
        item_num_label.place(x = 175, y = 25)
        itemdescriplabel.place(x = 325, y = 25)


        menu= Menu(self.master)
        self.master.config(menu=menu)
        #File Cascade Menu
        file= Menu(menu)

        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='Save Inventory', )

        menu.add_cascade(label="File", menu=file)

        edit= Menu(menu)
        edit.add_command(label="Undo",)
       # edit.add_command(label="show Image", command=self.showImg())
       # edit.add_command(label="show Text", command=self.showTxt())

        menu.add_cascade(label="Edit", menu=edit)
   

  #  def showImg(self):
      #  load= Image.open('warehouse.png')
      #  render = ImageTk.PhotoImage(load)

      #  img = Label(self, image=render)
      #  img.image= render
      #  img.place(x=0, y=200)

    def showTxt(self):
        text = Label(self, text='hey clean warehouse')
        text.pack()

    def client_save(self):
        import Inventorycounter
        Inventorycounter.inv_db()
    def client_exit(self):
        exit()

root = Tk()
#Work on the resize background image
C= Canvas(root, bg="red", height=1024, width=600)
filename=PhotoImage(file = "warehouse.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
root.geometry("1024x600")
app = Window(root)

root.mainloop()    