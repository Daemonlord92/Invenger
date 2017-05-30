from openpyxl import *
inv_db =Workbook()



#User inputs Item Information in the Database
class inv_item(object):
   def item_name(self):
       
       pass
   def item_num(self):
       pass
   def itemdescrip(self):
       pass
   def itemweight(self):
       pass
   def item_amount(self):
       pass
   def item_cost(self):
       pass



#Sorts through the items in the Database and put the Aphlabetlcally
class sort_inv_items(object):
    pass
#Item Database
class inv_db(object):
    ws = inv_db.active
    wb2= load_workbook('Inventory.xlsx')
    
    

    pass
#Creates a backuplist on a website
class backup_list(object):
    pass
#Saves the Database
class Save_db(inv_db):

    def __init__(self):
        inv_db.save("Inventory.xlsx")
