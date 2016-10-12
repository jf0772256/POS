'''
Jesse Fender
05/07/2016
DataBase Test file:)
'''
import DB_Connect as DB
import os
##Project Variables
Adm_Login=False
loadScreen = True

Customer=DB.Customer()
Employees=DB.Employees()
Managers=DB.Managers()
Inventory=DB.Inventory()

print ""

def Main():
   global Managers, Adm_Login, Employees, Customer, loadScreen
   if loadScreen == True:
      print "Loading... Please Wait"
      DB.Read_JSON_Data()
      loadScreen = False
      print "done..."
      print ""
   DB.MenuItems()
   choice=int(raw_input("Enter your selection from here: "))
   if choice==1:
      DB.Sales_Menu()
      salesLogin()
   elif choice==2:
      UserName=raw_input("Enter your manager number: ")#now should validate Manager number
      Psswrd=raw_input("Enter your password: ")
      Adm_Login=Managers.Admin_Login(UserName,Psswrd)
      if Adm_Login==True:
         Adm_Login_True(Adm_Login)
      else:
         choice=0
         Main()
   elif choice==3: ##hidden Command to exit gracefully
      #you will need to sve db files...
      #and then when done...
      DB.Write_JSON_Data()
      raw_input("Press any key to exit the program >>> ")
      quit()
   elif choice==4:
      DB.Write_JSON_Data()
   else:
      choice=0
      Main()
      
def Adm_Login_True(Success):
   global Managers, Adm_Login, Employees, Inventory
   ##should only pass here if sucessful at logging in##
   print ""
   loggedIn = Success
   Choice=int(raw_input("Select An Option Above: "))
   if Choice==0: ##Log Off
      UserId=raw_input("To confirm your log out command enter your username: ")
      Adm_Login=Managers.Admin_Logoff(UserId)
      loggedIn=False
      Main()
   elif Choice==1:
      Inventory.Add_Inventory()
      Adm_Login_True(loggedIn)
      Main()
   elif Choice==2:
      Employees.Add_Empl()
      Adm_Login_True(loggedIn)
      Main()
   elif Choice==3:
      Managers.Add_Manager()
      Adm_Login_True(loggedIn)
      Main()
   elif Choice==5:
      Employees.Remove_Empl()
      Adm_Login_True(loggedIn)
   elif Choice==8:
      UName=raw_input("Enter your manager number: ")
      Cur_PW = raw_input("Enter your CURRENT password: ")
      New_PW = raw_input("Enter your desired NEW password: ")
      Managers.Change_Man_Pswrd(UName,Cur_PW, New_PW)
      Adm_Login_True(loggedIn)
   elif Choice==10:
      Inventory.Prnt_Inv_Lst()
      Adm_Login_True(loggedIn)
      Main()
   elif Choice==11:
      Employees.Prnt_Empl_Lst()
      Adm_Login_True(loggedIn)
      Main()
   elif Choice==12:
      Managers.Prnt_Mngr_Lst()
      Adm_Login_True(loggedIn)
      Main()
      
def salesLogin(Message=""):
   #sets choice based on sales persons option.
   global Customer
   Cust_Num = 0
   choice = int(raw_input("Please Choose an option from above: "))
   if choice == 1:
      Cust_Num = Customer.Add_Customer()
      Message="Customer created successfully!"
      DB.Sales_Menu()
      salesLogin(Message)
   elif choice == 2:
      Cust_Num = Customer.Search_Customer()
   else:
      Message = "Invalid Entry"
      salesLogin(Message)
      
      
Main()
