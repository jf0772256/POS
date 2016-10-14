## Test file for the new_dbconnect ##

'''
    written for the purpose of testing new_dbconnect
    date written: 10/13/2016
    Revised Date: 00/00/0000
    version: 01.00.00A
'''

import new_dbconnect as DB

DBControl = DB.dbControl()
Managers = DB.Managers()
Employees = DB.Employees()
Inventory = DB.Inventory()
Encoder = DB.stringEncode()

DB.AdminMenu()
DB.Sales_Menu()
DB.MenuItems()
