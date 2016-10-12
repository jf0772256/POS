'''
Jesse Fender
Initial start: 05/07/2016
DataBase file:)
Version: A.002.151

See DB Change Log for version data
'''
import os
import encodedecode as ENDE_Code
import saveFilejson as savefilesJ

##Associative Arrays##
Employee={} #Builds Employee Table for use
EmplInactive={} #Builds inactive employee records

Manager={} #Builds Manager Table for use
MngrInactive={}#Builds inactive manager records

Invntry={} #Builds Inventory Table for use
InvInactive={}#Builds inactive inventory records

SalesInvoices={} #Builds Past Sales Invoices to data table

Customer_List={} #Builds Customer data table
Customer_Account={} #Builds Customer Accounts Table

##Item Lists##
#Invce_Data=[]
#Empl_Data=[]
#Invtry_Data=[]
#Man_Data=[]

##Other Variables##
SKU=0
SalesTicketNum=0
SuperAdmin="100" ##super admin -- Do Not Modify! --
SU_Password="P@$$w0rd" ## Default Password, Not recommended that this be changed same as any manager but allows adding and removing Managers.
IsSuper=False #user is logged in as super admin user

##Employee Numbers##
EmplNum=999
ManagerNum=100

#Customer Numbers from 0#
Cust_Num=0
Accnt_Num=0
#inventory starts at 0 and will increment auto to 1.
#sales tickets start from 0 and will increment auto to 1.
#employee numbers start from 999 and will increment auto to 1000.
#managers start from 100 and will increment auto to 101. Super admin is manager num 100
#these values will have to be updated when the service is started and data is read.
PATH = "dbfiles\\"

##class for employees##
class Employees:

   #serch Strings for returning lists of equivilant values
   def Search_LN(self, LName): #searches for last name in the employees list
      global Employee
      return Employee.keys()[Employee.values().index(Lname)]
   def Search_FN(self, FName): #searches for First name in the employees list
      global Employee
      return Employee.keys()[Employee.values().index(Fname)]
   def Search_LN(self, Phone): #searches for phone number in the employees list
      global Employee
      return Employee.keys()[Employee.values().index(Phone)]

   def ValidateEmpl(self, EmployeeNumber): ##internal validation to ensure that a valid Employee exists for use when adding managers only
      global Employee
      retVal=False
      if Employee.has_key(EmployeeNumber):
         if Employee[EmployeeNumber]["Active"]==True:
            retVal=True
            return retVal
         else:
            retVal=False
            return retVal
      else:
         retVal=False
         return retVal

   def Prnt_Empl_Lst(self):
      global Employee
      for key in sorted(Employee):
          print "%s: %s" % (key, Employee[key])
      print ""
      AdminMenu()

   def Add_Empl(self):
      global EmplNum, Employee,EmplInactive
      FirstName=raw_input("Please enter employees first name: ")
      LastName=raw_input("Please enter employees last name: ")
      Phone=raw_input("Please enter employees phone number: ")

      reHireEmpl = False
      for IE_Key in EmplInactive.keys():
         if EmplInactive[IE_Key]["FirstName"]==FirstName and EmplInactive[IE_Key]["LastName"]==LastName and EmplInactive[IE_Key]["Phone"]==Phone:
            del EmplInactive[IE_Key]
            Employee[IE_Key]["Active"]=True
            reHireEmpl = True
            break
         else:
            reHireEmpl = False
      ##if there is no value then create a new entry##
      if reHireEmpl == False:
         EmplNum+=1
         Employee[EmplNum]={"FirstName":FirstName,"LastName":LastName,"Phone":Phone, "Active":True, "isManager":False} ## read following block comment on this##
      else:
         print "There was an error in processing, please check all the information that you have entered and try again."
      print ""
      AdminMenu()
      '''
      Pretty much most is self explanitory, employee name, and phone, may add address here too... Important parts are the last three, Logged in#not yet added#
      Active meaning that the employee is a member of the corporation and not been termed either voluntary or involuntary. isManager is the designation that
      attaches employee to managers que, as a manager additional options become avail if logged in... employee and manager staff had seperate log ins and may
      proocess transactions as employee or as manager depending on log in status. Removal of employees can be done by manager level staff, However only marks
      Active status false. can be reactivated later date if needs be. DEFAULTS: Active=TRUE IsManager=FALSE LoggedIn=FALSE*when applied
      '''
   def Remove_Empl(self):
      #flips is active switch to inactive.#
      global Employee, EmplNum
      self.Prnt_Empl_Lst()
      Termed=int(raw_input("Please enter the employee number of the employee being termed: "))
      isValid=self.ValidateEmpl(Termed) #ensure a number entered exists
      if isValid==True: # is a valid employee number
         Employee[Termed]["Active"]=False #set active status == False
         self.get_Inact_Empl() #iterates through entire list of employee and checks active status
      else:
         print "No such employee exists, please check the employee list and try again."
      AdminMenu()

   def get_Inact_Empl(self):
      global Employee, EmplInactive
      for InvlEmpl in Employee.keys(): #every employee number is searched...
         if Employee[InvlEmpl]["Active"]==False and EmplInactive.has_key(InvlEmpl): #if they are not active, but in array already should skip
            pass
         elif Employee[InvlEmpl]["Active"]==False and EmplInactive.has_key(InvlEmpl)==False:#if they are not active, but nit in array, add to array
            EmplInactive[InvlEmpl]=Employee[InvlEmpl]
      for Empl in EmplInactive.keys(): ##Prints values in a neat list
         print str(Empl) +": ",
         for Empl1 in EmplInactive[Empl].keys():
            print EmplInactive[Empl][Empl1],
         print ""


##Class for Managers##
class Managers:

   def Prnt_Empl_Lst(self):
      global Employee
      for Empl in Employee.keys():
         print str(Empl) +": ",
         for Empl1 in Employee[Empl].keys():
            print Employee[Empl][Empl1],
         print ""

   def ValidateEmpl(self, EmployeeNumber): ##internal validation to ensure that a valid Employee exists for use when adding managers only
      global Employee
      retVal=False
      if EmployeeNumber in Employee:
         if Employee[EmployeeNumber]["Active"]==True:
            retVal=True
            return retVal
         else:
            retVal=False
            return retVal
      else:
         retVal=False
         return retVal

   def Add_Manager(self):
      global ManagerNum, Manager, Employee, IsSuper #to flip isManager switch
      if IsSuper==True:
         ManagerNum+=1
         self.Prnt_Empl_Lst()
         EmployeeNum=int(raw_input("Please enter the new managers employee number: "))
         isValid=self.ValidateEmpl(EmployeeNum)
         if isValid==True:
            Employee[EmployeeNum]["isManager"]=True
            Password=raw_input("Please enter new password for the new manager: ")
            Manager[ManagerNum]={"EmployeeNumber":EmployeeNum,"Password":Password,"MgrLogedIn":False, "Active":True} ## Read Block Comment on this##
            AdminMenu()
         else:
            print "You have entered an invalid Employee number. Please try again."
            self.Add_Manager()
      else:
         print "You must be logged in as Super Admin User before you will be allowed to add managers. Logg off your user and log in as your Super Administrator to add a manager."
         AdminMenu()
      '''
      This function will require that you have Super Admin User logged in, this will limit the ability of the other managers from adding unauthorized employees
      as manager staff. the Super Admin User cannot be logged in at the sale ticket so you must have at least one other regular manager level person. Removing a
      manager from being a manager either by termination or demotion either voluntary or involuntary will mark Active state to false, thus not being able to log
      in as a manager or make sales transactions as a manager. DEFAULTS: Active=TRUE MgrLoggedIn=FALSE
      '''

   def Prnt_Mngr_Lst(self):
      global Manager
      for Mngr in Manager.keys():
         print str(Mngr) +": ",
         for Mngr1 in Manager[Mngr].keys():
            print Manager[Mngr][Mngr1],
         print ""

   def ValidateMngr(self, MngrID): ##internal validation to ensure that a valid manager exists
      global Manager
      retVal=False
      if MngrID=="100": ## Super Admin Is ALWAYS Valid :)
         retVal=True
         return retVal
      elif MngrID in Manager:
         print "Im here"
         if Manager[MngrID]["Active"]==True:
            retVal=True
            return retVal
         else:
            print "I failed to find an active manager"
            retVal=False
            return retVal
      else:
         print "I failed to find the manager that you were looking for."
         retVal=False
         return retVal

   def Admin_Login(self,UserName,Password):
      global Manager, Employee, SuperAdmin, SU_Password, IsSuper
      isValid=self.ValidateMngr(UserName)
      Sucess=False
      IsSuper=False
      if isValid==True and UserName==SuperAdmin and SU_Password==Password:
         print ""
         print "You have successfully logged in as Super Admin User."
         Sucess=True
         IsSuper=True
         AdminMenu()
      elif UserName==SuperAdmin and Password != SU_Password: # if wrong password entered for super user, fails, rather than error.
         isValid=False
         print ""
         print "Your log in was unsuccessful."
         Sucess=False
      elif isValid==True and Manager[UserName]["Password"]==Password:
         Manager[UserName]["MgrLogedIn"]=True
         print ""
         fName = Employee[str(Manager[UserName]["EmployeeNumber"])]["FirstName"]
         lName = Employee[str(Manager[UserName]["EmployeeNumber"])]["LastName"]
         print "You have successfully logged in " + fName + " " + lName
         Sucess=True
         AdminMenu()
      else:
         print ""
         print "Your log in was unsuccessful."
         Sucess=False
      return Sucess

   def Admin_Logoff(self, ManagerID):
      global Manager, Employee, SuperAdmin
      isValid=self.ValidateMngr(ManagerID)
      Success=True
      if isValid==True and ManagerID==SuperAdmin:
         print ""
         print "You have successfully logged out, Super Admin User."
         Success=True
         return Success
      elif isValid==True and Manager[ManagerID]["MgrLogedIn"]==True:
         Manager[ManagerID]["MgrLogedIn"]=False
         Success=True
         print ""
         print Employee[str(Manager[ManagerID]["EmployeeNumber"])]["FirstName"], Employee[str(Manager[ManagerID]["EmployeeNumber"])]["LastName"] + ", you have successfully logged off."
         return Success
      else:
         print ""
         print "Either you entered an invalid manager number or you were not logged in."
         Success=False
         return Success

   def Change_Man_Pswrd(self,UserName, oldPassword, newPassword):
      global Manager, SuperAdmin, SU_Password
      isValid=self.ValidateMngr(UserName)
      ##Goal: take username and old password to allow manager to change password##
      if isValid==True and UserName==SuperAdmin and oldPassword==SU_Password:
         print "You may not change the Super Admin password here, Contact IT department or Helpdesk for how to change the SA user Password."
         AdminMenu()
      elif isValid==True and Manager[UserName]["Password"]==oldPassword:
         Manager[UserName]["Password"]=newPassword
         print "Password has been changed Sucessfully."
         AdminMenu()
      else:
         print "Your Username or Password didn't Match records."
         AdminMenu()


##Class for Inventory##
class Inventory:
   def Add_Inventory(self):
      global SKU, Invntry
      SKU+=1
      Inv_Title=raw_input("Enter the item description here: ")
      Inv_Prce=float(raw_input("Enter Item Price here(000.00): "))
      Inv_Quan=int(raw_input("How many of this item are there?: "))
      Inv_Cat=raw_input("Enter the item category here: ")

      Invntry[SKU]={"Name":Inv_Title,"Price":Inv_Prce,"Quanity":Inv_Quan,"Category":Inv_Cat}

      AdminMenu()

   def Prnt_Inv_Lst(self):
      global Invntry
      for Inv in Invntry.keys():
         print str(Inv) +": ",
         for Inv1 in Invntry[Inv].keys():
            print Invntry[Inv][Inv1],
         print ""

class Customer:
   ##MainSha-Bang!##
   def Add_Customer(self):
      global Customer_List, Cust_Num, Accnt_Num
      ##Procedure to add a new customer##
      CFName=raw_input("What is the customers FIRST Name?: ")
      CLName=raw_input("What is the customers LAST Name?: ")
      CPhone=raw_input("What is the customers Phone Number?: ")
      CEmail=raw_input("What is the customers Email Address?: ")
      CStrAddr=raw_input("What is the customers Street Address?(Not Including Apt,Unit,Flr,Bldg,etc): ")
      CStrAddr2L=raw_input("Apartment, Unit, Building, Floor, etc: ")
      CCity=raw_input("What is the customers City?: ")
      CState=raw_input("What is the customers State?: ")
      CPostCode=raw_input("What is the customers Postal/Zip Code?: ")
      CZipSupl=raw_input("What is the customers Zip Supplement(Zip+4)?: ")
      New_Account=raw_input("Is the customer opening an account with us?: ").upper()
      New_Account=New_Account[0] ##Isolates the first letter##
      ##Putting it all together##
      Cust_Num+=1
      if New_Account=="Y":
         Accnt_Num+=1
         Customer_List[Cust_Num]={"FirstName":CFName,"LastName":CLName,"Phone":CPhone,"Email":CEmail,"StreetAddress":CStrAddr,"Address2ndLine":CStrAddr2L,"City":CCity,"State":CState,"PostalCode":CPostCode,"Zip+4":CZipSupl,"HasAccount":New_Account,"AccountNumber":Accnt_Num}
      else:
         Customer_List[Cust_Num]={"FirstName":CFName,"LastName":CLName,"Phone":CPhone,"Email":CEmail,"StreetAddress":CStrAddr,"Address2ndLine":CStrAddr2L,"City":CCity,"State":CState,"PostalCode":CPostCode,"Zip+4":CZipSupl,"HasAccount":New_Account,"AccountNumber":None}
      return Cust_Num

   def Print_Cust_List(self):
      global Customer_List
      os.system('cls' if os.name == 'nt' else 'clear')
      for Empl in Customer_List.keys():
         print str(Empl) +": ",
         for Empl1 in Customer_List[Empl].keys():
            print Customer_List[Empl][Empl1],
         print ""

   def Search_Customer(self,Message=""):
      global Customer_List
      os.system('cls' if os.name == 'nt' else 'clear')
      ##select a search Method and type, and let the program do the work for you:)##
      count=0
      customer=[]
      print ""
      print "Messages:",Message
      print ""
      print "Find Your Customer: 1. Customer Number   2. Phone Number   3. Email Address"
      SearchItem=raw_input("Enter search method: ")
      if SearchItem=="1":
         CustomerNum=int(raw_input("Enter the customer number: "))
         if Customer_List.has_key(CustomerNum):  ##is unique customer number
            print "Customer Name:",Customer_List[CustomerNum]["FirstName"],Customer_List[CustomerNum]["LastName"]
            print "Customer Phone:",Customer_List[CustomerNum]["Phone"],"Email:",Customer_List[CustomerNum]["Email"]
            print "Customer Address:",Customer_List[CustomerNum]["StreetAddress"],Customer_List[CustomerNum]["Address2ndLine"],Customer_List[CustomerNum]["City"],Customer_List[CustomerNum]["State"],Customer_List[CustomerNum]["PostalCode"]+"-"+Customer_List[CustomerNum]["Zip+4"]
            print "Customer Account:",Customer_List[CustomerNum]["HasAccount"],"Account Number:",Customer_List[CustomerNum]["AccountNumber"]
            Selected=raw_input("Is this the correct customer? (Y/N): ").upper()
            if Selected=="N":
               Message="No Customer Selected."
               Search_Customer(Message)
            else:
               return CustomerNum
         else:
            Message="Invalid Customer Number selected."
            Search_Customer(Message)

      elif SearchItem=="2": ##Non-Unique look up, will return a list that will need to be selected from.##
         Phone=raw_input("Customers Phone Number: ")
         for cust in Customer_List.keys():
            if Customer_List[cust]["Phone"]==Phone:
               customer.append(cust)
         if len(customer)==0:
            Message="No customers with that phone number were found."
            customer[:]=[]
            Search_Customer(Message)
         elif len(customer)==1:
            print "Customer Name:",Customer_List[customer[0]]["FirstName"],Customer_List[customer[0]]["LastName"]
            print "Customer Phone:",Customer_List[customer[0]]["Phone"],"Email:",Customer_List[customer[0]]["Email"]
            print "Customer Address:",Customer_List[customer[0]]["StreetAddress"],Customer_List[customer[0]]["Address2ndLine"],Customer_List[customer[0]]["City"],Customer_List[customer[0]]["State"],Customer_List[customer[0]]["PostalCode"]+"-"+Customer_List[customer[0]]["Zip+4"]
            print "Customer Account:",Customer_List[customer[0]]["HasAccount"],"Account Number:",Customer_List[customer[0]]["AccountNumber"]
            Selected=raw_input("Is this the correct customer? (Y/N): ").upper()
            if Selected=="N":
               Message="No Customer Selected."
               customer[:]=[]
               Search_Customer(Message)
            else:
               return customer[0]
         elif len(customer)>1:
            for i in range(0,len(customer)-1):
               count+=1
               print count,": Customer Name:",Customer_List[customer[i]]["FirstName"],Customer_List[customer[i]]["LastName"]
               print "Customer Phone:",Customer_List[customer[i]]["Phone"],"Email:",Customer_List[customer[i]]["Email"]
               print "Customer Address:",Customer_List[customer[i]]["StreetAddress"],Customer_List[customer[i]]["Address2ndLine"],Customer_List[customer[i]]["City"],Customer_List[customer[i]]["State"],Customer_List[customer[i]]["PostalCode"]+"-"+Customer_List[customer[i]]["Zip+4"]
               print "Customer Account:",Customer_List[customer[i]]["HasAccount"],"Account Number:",Customer_List[customer[i]]["AccountNumber"]
               Selected=raw_input("Select customer from list using the number by the name, if none, enter N: ").upper()
               if Selected=="N":
                  Message="No Customer Selected."
                  customer[:]=[]
                  count=0
                  Search_Customer(Message)
               else:
                  return customer[int(Selected)-1]
         else:
            Message="There must have been an error, please try again"
            Search_Customer(Message)

      elif SearchItem=="3": ##Semi-Unique look up, may return a list or single customer.##
         Email=raw_input("Customers Email Address: ")
         for cust in Customer_List.keys():
            if Customer_List[cust]["Email"]==Email:
               customer.append(cust)
         if len(customer)==0:
            Message="No customers with that Email Address were found."
            customer[:]=[]
            Search_Customer(Message)
         elif len(customer)==1:
            print "Customer Name:",Customer_List[customer[0]]["FirstName"],Customer_List[customer[0]]["LastName"]
            print "Customer Phone:",Customer_List[customer[0]]["Phone"],"Email:",Customer_List[customer[0]]["Email"]
            print "Customer Address:",Customer_List[customer[0]]["StreetAddress"],Customer_List[customer[0]]["Address2ndLine"],Customer_List[customer[0]]["City"],Customer_List[customer[0]]["State"],Customer_List[customer[0]]["PostalCode"]+"-"+Customer_List[customer[0]]["Zip+4"]
            print "Customer Account:",Customer_List[customer[0]]["HasAccount"],"Account Number:",Customer_List[customer[0]]["AccountNumber"]
            Selected=raw_input("Is this the correct customer? (Y/N): ").upper()
            if Selected=="N":
               Message="No Customer Selected."
               customer[:]=[]
               Search_Customer(Message)
            else:
               return customer[0]
         elif len(customer)>1:
            for i in range(0,len(customer)-1):
               count+=1
               print count,": Customer Name:",Customer_List[customer[i]]["FirstName"],Customer_List[customer[i]]["LastName"]
               print "Customer Phone:",Customer_List[customer[i]]["Phone"],"Email:",Customer_List[customer[i]]["Email"]
               print "Customer Address:",Customer_List[customer[i]]["StreetAddress"],Customer_List[customer[i]]["Address2ndLine"],Customer_List[customer[i]]["City"],Customer_List[customer[i]]["State"],Customer_List[customer[i]]["PostalCode"]+"-"+Customer_List[customer[i]]["Zip+4"]
               print "Customer Account:",Customer_List[customer[i]]["HasAccount"],"Account Number:",Customer_List[customer[i]]["AccountNumber"]
               Selected=raw_input("Select customer from list using the number by the name, if none, enter N: ").upper()
               if Selected=="N":
                  Message="No Customer Selected."
                  customer[:]=[]
                  count=0
                  Search_Customer(Message)
               else:
                  return customer[int(Selected)-1]
         else:
            Message="There must have been an error, please try again"
            Search_Customer(Message)
      else:
         Message="Invalid Entry, try again!"
         Search_Customer(Message)

   def Update_Cust_Info(self,CNumber,Messages=""):
      ##Module added 06/05/2016##
      global Customer_List
      os.system('cls' if os.name == 'nt' else 'clear')
      ##Display Messages##
      print ""
      print "Messages:",Messages
      print ""
      ##display customer details##
      print "Customers Name:",Customer_List[CNumber]["FirstName"],Customer_List[CNumber]["LastName"]
      print "Phone:",Customer_List[CNumber]["Phone"],"Email:",Customer_List[CNumber]["Email"]
      print "Street Address:",Customer_List[CNumber]["StreetAddress"],Customer_List[CNumber]["Address2ndLine"]
      print "City:",Customer_List[CNumber]["City"],"\t","State:",Customer_List[CNumber]["State"],"\t","Postal Code:",Customer_List[CNumber]["PostalCode"]+"-"+Customer_List[CNumber]["Zip+4"]
      ##Display Menu##
      print ""
      print "1. Update Name   2. Update Phone/Email   3. Update Street Address"
      print "4. Update City/State   5. Update Zip/Postal Code  6. Done Editing"
      print ""
      ##get user input##
      choice = raw_input("Select an option between 1 and 6: ")
      Messages=""
      print ""
      print "Any Blanks will be discarded and will remain the same."
      print ""
      if choice=="1":
         NFN=raw_input("Enter the customers first name: ")
         NLN=raw_input("Enter the customers last name: ")
         if NFN!="":
            Customer_List[CNumber]["FirstName"]=NFN
            Messages="The first name"
         if NLN!="":
            Customer_List[CNumber]["LastName"]=NLN
            Messages=Messages+" The last name"
         Messages=Messages+" has/have been updated sucessfully."
         Update_Cust_Info(CNumber,Messages)
      elif choice=="2":
         NPH=raw_input("Enter the customers Phone Number: ")
         NEM=raw_input("Enter the customers Email Address: ")
         if NPH!="":
            Customer_List[CNumber]["Phone"]=NPH
            Messages="The Phone Number"
         if NEM!="":
            Customer_List[CNumber]["Email"]=NEM
            Messages=Messages+" The Email Address"
         Messages=Messages+" has/have been updated sucessfully."
         Update_Cust_Info(CNumber,Messages)
      elif choice=="3":
         NSA=raw_input("Enter the Street Address(Not Incl Apartment or building numbers): ")
         NSA2=raw_input("Enter the Optional building Info. e.g apt# Unit# floor# or room# etc: ")
         if NSA!="":
            Customer_List[CNumber]["StreetAddress"]=NSA
            Messages="The Street Address"
         if NSA2!="":
            Customer_List[CNumber]["Address2ndLine"]=NSA2
            Messages=Messages+" The Building Information"
         Messages=Messages+" has/have been updated sucessfully."
         Update_Cust_Info(CNumber,Messages)
      elif choice=="4":
         NCTY=raw_input("Enter the City: ")
         NSTE=raw_input("Enter the State: ")
         if NCTY!="":
            Customer_List[CNumber]["City"]=NCTY
            Messages="The City"
         if NSTE!="":
            Customer_List[CNumber]["State"]=NSTE
            Messages=Messages+" The State"
         Messages=Messages +" has/have been updated sucessfully."
         Update_Cust_Info(CNumber,Messages)
      elif choice=="5":
         NPC=raw_input("Enter the Zip/Postal Code: ")
         NZP4=raw_input("Enter the Zip+4: ")
         if NPC!="":
            Customer_List[CNumber]["PostalCode"]=NPC
            Messages="The Zip/Postal Code "
         if NZP4!="":
            Customer_List[CNumber]["Zip+4"]=NZP4
            Messages=Messages+"The Zip Supplemental"
         Messages=Messages+" has/have been updated sucessfully."
         Update_Cust_Info(CNumber,Messages)
      elif choice=="6":
         return 0
      else:
         Messages="You have selected an invalid answer, Please try again."
         Update_Cust_Info(CNumber,Messages)

   def Add_Cust_AcntInfo(self,CustNum,Messages=""):
      ##Module added 06/14/2016##
      global Customer_List,Customer_Accnt,Accnt_Num
      os.system('cls' if os.name == 'nt' else 'clear')
      CAccount=0
      ##Display Messages##
      print ""
      print "Messages:",Messages
      print ""
      ##see if customer has an account onfile with the POS system.##
      if Customer_List[CustNum]["HasAccount"]!="N" or Customer_List[CustNum]["HasAccount"]!="NO":
         AccntNum+=1
         CAccount=AccntNum
         Customer_List[CustNum]["AccountNumber"]=CAccount

def MenuItems():
   print "Welcome to the FDF Point-Of-Sale system"
   print "Please Choose from the below options:"
   print "1. Start a Sales Ticket         2. Log into Administration Menu"
   print ""

def AdminMenu():
   print "Welcome to the Admin menu of the FDF Point-Of-Sale system"
   print "It is up to you to protect company assets, security is key!"
   print ""
   print "1: Add Inventory                      2: Add Employee"
   print "3: Add Manager(req Special Log In)    4: Remove Inventory"
   print "5: Remove Employee                    6: Remove Manager(req Special Log In)"
   print "7: Update Employee                    8: Update Manager"
   print "9: Update Inventory                   0: Log Off Admin"
   print "10: Print Inventory                   11: Print Employees"
   print "12: Print Managers                    13: View Reports Menu"

def Sales_Menu():
   ##prints selection Meu for sales selection##
   print "Sales Ticket Menu"
   print "1. Add Customer  2. Search Customer"

def Write_JSON_Data():
   ##puts data into files##
   global PATH, Employee, EmplInactive, Manager, MngrInactive, Invntry, InvInactive
   global SalesInvoices, Customer_List, Customer_Account
   #set variables for numeric data lost when the POS is unloaded#
   global SKU, SalesTicketNum, EmplNum, ManagerNum, Cust_Num, Accnt_Num
   ##savefilesJ##
   print "Saving DataBase Files ",
   data={"SKUs":SKU,"SalesTicketNumber":SalesTicketNum,"Employee":EmplNum,"Manager":ManagerNum,"Customer":Cust_Num,"Account":Accnt_Num}
   print "++",
   savefilesJ.write_JSON(PATH+"manager.json", Manager)
   print "++",
   savefilesJ.write_JSON(PATH+"employee.json", Employee)
   print "++",
   savefilesJ.write_JSON(PATH+"mngrinactive.json", MngrInactive)
   print "++",
   savefilesJ.write_JSON(PATH+"emplinactive.json", EmplInactive)
   print "++",
   savefilesJ.write_JSON(PATH+"inventory.json", Invntry)
   print "++",
   savefilesJ.write_JSON(PATH+"invinact.json", InvInactive)
   print "++",
   savefilesJ.write_JSON(PATH+"invoices.json", SalesInvoices)
   print "++",
   savefilesJ.write_JSON(PATH+"clist.json", Customer_List)
   print "++",
   savefilesJ.write_JSON(PATH+"caccnt.json", Customer_Account)
   print "++",
   savefilesJ.write_JSON(PATH+"data.json", data)
   print "++",
   #this should write 9 files
   print "Files Saved Successfully"
   print "Exiting Sales System"

def Read_JSON_Data():
   ##reads data from files##
   global PATH, Employee, EmplInactive, Manager, MngrInactive, Invntry, InvInactive
   global SalesInvoices, Customer_List, Customer_Account
   #set variables for numeric data lost when the POS is unloaded#
   global SKU, SalesTicketNum, EmplNum, ManagerNum, Cust_Num, Accnt_Num
   data={}
   ##savefilesJ##
   print "Loading data files into database ",
   Manager=savefilesJ.read_JSON(PATH+"manager.json")
   print "++",
   Employee=savefilesJ.read_JSON(PATH+"employee.json")
   print "++",
   MngrInactive=savefilesJ.read_JSON(PATH+"mngrinactive.json")
   print "++",
   EmplInactive=savefilesJ.read_JSON(PATH+"emplinactive.json")
   print "++",
   Invntry=savefilesJ.read_JSON(PATH+"inventory.json")
   print "++",
   InvInactive=savefilesJ.read_JSON(PATH+"invinact.json")
   print "++",
   SalesInvoices=savefilesJ.read_JSON(PATH+"invoices.json")
   print "++",
   Customer_List=savefilesJ.read_JSON(PATH+"clist.json")
   print "++",
   Customer_Account=savefilesJ.read_JSON(PATH+"caccnt.json")
   print "++",
   data=savefilesJ.read_JSON(PATH+"data.json")
   print "++",
   print "Loading of data has been completed"
   print "Loading system data variables ",
   SKU=data["SKUs"]
   print "++",
   SalesTicketNum=data["SalesTicketNumber"]
   print "++",
   EmplNum=data["Employee"]
   print "++",
   ManagerNum=data["Manager"]
   print "++",
   Cust_Num=data["Customer"]
   print "++",
   Accnt_Num=data["Account"]
   print "++",
   print "Loading of variables complete"
