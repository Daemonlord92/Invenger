
import sqlite3
from sqlite3 import Error


class NewDatabase(object):

    def main():
        database = "C:\\sqlite\db\inventory.db"

        conn = create_connection(database)
        with conn:
            print("1.Add Item to Inventory:")


    def create_db(self):
        try:
            conn = sqlite3.connect(inventory.db)
            return conn
        except Error as e:
            print(e)

        return None

#User inputs Item Information in the Database


class InvItem(object):
   def item_name(self):
       pass

   def item_num(self):
       pass

   def item_descrip(self):
       pass

   def item_weight(self):
       pass

   def item_amount(self):
       pass

   def item_cost(self):
       pass



#Sorts through the items in the Database and put the Aphlabetlcally

class SortInvItems(object):
    pass


#Item Database

class InvDb(object):
    pass

#Creates a back-up list on a website

class BackupList(object):
    pass

#Saves the Database


class SaveDb(InvDb):

    def __init__(self):
        pass
