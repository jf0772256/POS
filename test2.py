## Test file for the new_dbconnect ##

'''
    written for the purpose of testing new_dbconnect
    date written: 10/13/2016
    Revised Date: 10/14/2016
    version: 01.00.10A
'''

import new_dbconnect as DB

DBControl = DB.dbControl()
Managers = DB.Managers()
Employees = DB.Employees()
Inventory = DB.Inventory()
Encoder = DB.stringEncode()

PATH = "\\dbfiles\\"

DB.AdminMenu()
print ""
DB.Sales_Menu()
print ""
DB.MenuItems()
print ""
print PATH
raw_input("press key to exit")
