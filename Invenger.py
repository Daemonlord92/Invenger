from tkinter import *
from tkinter import messagebox

import Inventorycounter

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
        quitButton.place(x=0, y=500)
        saveButton.place(x=200, y=500)
        addButton.place(x=300, y=500)
       #Text Entry
        item_name = Entry(root, )
        item_num = Entry(root)
        itemdescrip = Entry(root)
        item_weight = Entry(root)
        item_amount = Entry(root)
        item_cost = Entry(root)
        #Text Entry Placements

        item_name.place (x=50, y= 50)
        item_num.place (x= 200, y= 50)
        itemdescrip.place (x=350, y= 50)
        item_weight.place (x= 500, y= 50)
        item_amount.place (x= 650, y= 50)
        item_cost.place (x= 800, y = 50)
        #Text Labels
        item_name_label = Label(root, text= "Item Name", )
        item_num_label = Label(root, text = "Item Number")
        itemdescriplabel= Label(root, text = "Item Description")
        item_weight_label= Label(root, text = "Item Weight")
        item_amount_label= Label(root, text = "Item Quanity")
        item_cost_label = Label(root, text = "Item Cost")
        #Text Labels Placements
        item_name_label.place(x = 25, y= 25)
        item_num_label.place(x = 175, y = 25)
        itemdescriplabel.place(x = 325, y = 25)
        item_weight_label.place(x = 475, y = 25)
        item_amount_label.place(x = 625, y = 25)
        item_cost_label.place(x = 775, y = 25)


        menu= Menu(self.master)
        self.master.config(menu=menu)
        #File Cascade Menu
        file= Menu(menu)

        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='Save Inventory', command=self.client_save)
        file.add_command(label='Add Item')

        menu.add_cascade(label="File", menu=file)

        edit= Menu(menu)
        edit.add_command(label="Undo",)
       # edit.add_command(label="show Image", command=self.showImg())
       # edit.add_command(label="show Text", command=self.showTxt())

        menu.add_cascade(label="Edit", menu=edit)
   


   # def showTxt(self):
    #    text = Label(self, text='hey clean warehouse')
     #   text.pack()

    def client_save(self):
        #Work on the save buttons
        Inventorycounter.Save_db
    def client_exit(self):
        exit()

root = Tk()
root.geometry("1024x600")
app = Window(root)

root.mainloop()    