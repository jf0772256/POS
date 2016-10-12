'''
Revised FDF POS database connection
Version 0.3.8
10/07/2016
why a new file? we needed to clean up the code and get it working better than before
'''

## Declarations and more ##
import os as OS
import json as DBSO

## Associative Arrays ##
## -------------------------------------------------------
Employee = {}             #Builds Employee Table for use
EmplInactive = {}         #Builds inactive employee records
Manager = {}              #Builds Manager Table for use
MngrInactive = {}         #Builds inactive manager records
Invntry = {}              #Builds Inventory Table for use
InvInactive = {}          #Builds inactive inventory records
SalesInvoices = {}        #Builds Past Sales Invoices to data table
Customer_List = {}        #Builds Customer data table
Customer_Account = {}     #Builds Customer Accounts Table

## Archive Arrays ##
## ---------------------------------------------------------
ArchEmp = {}            #Builds Employee archive table
ArchMan = {}            #Builds Manager archive table
ArchInv = {}            #Builds Inventory archive table
ArchSIn = {}            #Builds SalesInvoice archive table
ArchCus = {}            #Builds Customer archive table
ArchAct = {}            #Builds CustAccounts archive table

## Numerical Data Variables
## ------------------------------------------------------------
SKU = 0                     ## Inventory keyID
SalesTicketNum = 0          ## SalesTicket KeyID
SuperAdmin = "100"          ## superadmin -- Do Not Modify! --
SU_Password = "P@$$w0rd"    ## Default Password, Not recommended that this be changed same as any manager but allows adding and removing Managers.
IsSuper = False             ## user is logged in as super admin user
EmplNum = 999               ## Employee keyID
ManagerNum = 100            ## Manager KeyID
Cust_Num = 0                ## Customer-Number ID
Accnt_Num = 0               ## Customer-Account KeyID

## Non-Class modules or functions
## ------------------------------------------------------------


## Classes Below Here
## ------------------------------------------------------------
class dbControl():
    def write_JSON(self, fileName, PassData):
        with open(fileName,'wb') as f:
            json.dump(PassData,f)
        file.close(f)

    def read_JSON(self, fileName):
        with open(fileName,'rb') as f:
            FileData = json_load_byteified(f)
        file.close(f)
        return FileData

    ##from Stack Overflow http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python
    ##will replace read_JSON() for correct reads
    def json_load_byteified(self, file_handle):
        return _byteify(json.load(file_handle, object_hook=_byteify),ignore_dicts=True)

    def json_loads_byteified(self, json_text):
        return _byteify(json.loads(json_text, object_hook=_byteify),ignore_dicts=True)

    def _byteify(self, data, ignore_dicts = False):
        if isinstance(data, unicode):
            return data.encode('utf-8')
        if isinstance(data, list):
            return [ _byteify(item, ignore_dicts=True) for item in data ]
        if isinstance(data, dict) and not ignore_dicts:
            return { _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True) for key, value in data.iteritems() }
        return data

    def updateData(self, filepath, data):
        ## Use this function to write the data from the database tables to the database files
        write_JSON(filepath, data)
    def selectData(self, filepath):
        ## Use this function to read the data from the database files into the database tables
        return read_JSON(filepath)

class stringEncode():
    my_Cypher={"a":ord('a'), "b":ord('b'), "c":ord('c'), "d":ord('d'), "e":ord('e'), "f":ord('f'), "g":ord('g'), "h":ord('h'), "i":ord('i'), "j":ord('j'), "k":ord('k'), "l":ord('l'), "m":ord('m'), "n":ord('n'), "o":ord('o'), "p":ord('p'), "q":ord('q'), "r":ord('r'), "s":ord('s'), "t":ord('t'),
               "u":ord('u'), "v":ord('v'), "w":ord('w'), "x":ord('x'), "y":ord('y'), "z":ord('z'), "A":ord('A'), "B":ord('B'), "C":ord('C'), "D":ord('D'), "E":ord('E'), "F":ord('F'), "G":ord('G'), "H":ord('H'), "I":ord('I'), "J":ord('J'), "K":ord('K'), "L":ord('L'), "M":ord('M'), "N":ord('N'),
               "O":ord('O'), "P":ord('P'), "Q":ord('Q'), "R":ord('R'), "S":ord('S'), "T":ord('T'), "U":ord('U'), "V":ord('V'), "W":ord('W'), "X":ord('X'), ":":ord(':'), ";":ord(';'), "\"":ord('\"'), "\'":ord('\''), "<":ord('<'), ">":ord('>'), ",":ord(','), ".":ord('.'), "/":ord('/'), "?":ord('?'),
               "+":ord('+'), "!":ord('!'), "@":ord('@'), "#":ord('#'), "$":ord('$'), "%":ord('%'), "^":ord('^'), "&":ord('&'), "*":ord('*'), "(":ord('('), ")":ord(')'), "-":ord('-'), "_":ord('_'), "=":ord('='), "`":ord('`'), "~":ord('~'), " ":ord(' '),
               "\xa0":ord('\xa0'), "\xa1":ord('\xa1'), "\xa2":ord('\xa2'), "\xa3":ord('\xa3'), "\xa4":ord('\xa4'), "\xa5":ord('\xa5'), "\xa6":ord('\xa6'), "\xa7":ord('\xa7'), "\xa8":ord('\xa8'), "\xa9":ord('\xa9'), "\xaa":ord('\xaa'), "\xab":ord('\xab'), "\xac":ord('\xac'), "\xad":ord('\xad'), "\xae":ord('\xae'), "\xaf":ord('\xaf'),
               "\xb0":ord('\xb0'), "\xb1":ord('\xb1'), "\xb2":ord('\xb2'), "\xb3":ord('\xb3'), "\xb4":ord('\xb4'), "\xb5":ord('\xb5'), "\xb6":ord('\xb6'), "\xb7":ord('\xb7'), "\xb8":ord('\xb8'), "\xb9":ord('\xb9'), "\xba":ord('\xba'), "\xbb":ord('\xbb'), "\xbc":ord('\xbc'), "\xbd":ord('\xbd'), "\xbe":ord('\xbe'), "\xbf":ord('\xbf'),
               "\xc0":ord('\xc0'), "\xc1":ord('\xc1'), "\xc2":ord('\xc2'), "\xc3":ord('\xc3'), "\xc4":ord('\xc4'), "\xc5":ord('\xc5'), "\xc6":ord('\xc6'), "\xc7":ord('\xc7'), "\xc8":ord('\xc8'), "\xc9":ord('\xc9'), "\xca":ord('\xca'), "\xcb":ord('\xcb'), "\xcc":ord('\xcc'), "\xcd":ord('\xcd'), "\xce":ord('\xce'), "\xcf":ord('\xcf'),
               "\xd0":ord('\xd0'), "\xd1":ord('\xd1'), "\xd2":ord('\xd2'), "\xd3":ord('\xd3'), "\xd4":ord('\xd4'), "\xd5":ord('\xd5'), "\xd6":ord('\xd6'), "\xd7":ord('\xd7'), "\xd8":ord('\xd8'), "\xd9":ord('\xd9'), "\xda":ord('\xda'), "\xdb":ord('\xdb'), "\xdc":ord('\xdc'), "\xdd":ord('\xdd'), "\xde":ord('\xde'), "\xdf":ord('\xdf'),
               "\xe0":ord('\xe0'), "\xe1":ord('\xe1'), "\xe2":ord('\xe2'), "\xe3":ord('\xe3'), "\xe4":ord('\xe4'), "\xe5":ord('\xe5'), "\xe6":ord('\xe6'), "\xe7":ord('\xe7'), "\xe8":ord('\xe8'), "\xe9":ord('\xe9'), "\xea":ord('\xea'), "\xeb":ord('\xeb'), "\xec":ord('\xec'), "\xed":ord('\xed'), "\xee":ord('\xee'), "\xef":ord('\xef'),
               "\xf0":ord('\xf0'), "\xf1":ord('\xf1'), "\xf2":ord('\xf2'), "\xf3":ord('\xf3'), "\xf4":ord('\xf4'), "\xf5":ord('\xf5'), "\xf6":ord('\xf6'), "\xf7":ord('\xf7'), "\xf8":ord('\xf8'), "\xf9":ord('\xf9'), "\xfa":ord('\xfa'), "\xfb":ord('\xfb'), "\xfc":ord('\xfc'), "\xfd":ord('\xfd'), "\xfe":ord('\xfe'), "\xff":ord('\xff'),
               "\x10":ord('\x10'), "\x11":ord('\x11'), "\x12":ord('\x12'), "\x13":ord('\x13'), "\x14":ord('\x14'), "\x15":ord('\x15'), "\x16":ord('\x16'), "\x17":ord('\x17'), "\x18":ord('\x18'), "\x19":ord('\x19'), "\x1a":ord('\x1a'), "\x1b":ord('\x1b'), "\x1c":ord('\x1c'), "\x1d":ord('\x1d'), "\x1e":ord('\x1e'), "\x1f":ord('\x1f'),
               "\x20":ord('\x20'), "\x21":ord('\x21'), "\x22":ord('\x22'), "\x23":ord('\x23'), "\x24":ord('\x24'), "\x25":ord('\x25'), "\x26":ord('\x26'), "\x27":ord('\x27'), "\x28":ord('\x28'), "\x29":ord('\x29'), "\x2a":ord('\x2a'), "\x2b":ord('\x2b'), "\x2c":ord('\x2c'), "\x2d":ord('\x2d'), "\x2e":ord('\x2e'), "\x2f":ord('\x2f'),
               "\x30":ord('\x30'), "\x31":ord('\x31'), "\x32":ord('\x32'), "\x33":ord('\x33'), "\x34":ord('\x34'), "\x35":ord('\x35'), "\x36":ord('\x36'), "\x37":ord('\x37'), "\x38":ord('\x38'), "\x39":ord('\x39'), "\x3a":ord('\x3a'), "\x3b":ord('\x3b'), "\x3c":ord('\x3c'), "\x3d":ord('\x3d'), "\x3e":ord('\x3e'), "\x3f":ord('\x3f'),
               "\x40":ord('\x40'), "\x41":ord('\x41'), "\x42":ord('\x42'), "\x43":ord('\x43'), "\x44":ord('\x44'), "\x45":ord('\x45'), "\x46":ord('\x46'), "\x47":ord('\x47'), "\x48":ord('\x48'), "\x49":ord('\x49'), "\x4a":ord('\x4a'), "\x4b":ord('\x4b'), "\x4c":ord('\x4c'), "\x4d":ord('\x4d'), "\x4e":ord('\x4e'), "\x4f":ord('\x4f'),
               "\x50":ord('\x50'), "\x51":ord('\x51'), "\x52":ord('\x52'), "\x53":ord('\x53'), "\x54":ord('\x54'), "\x55":ord('\x55'), "\x56":ord('\x56'), "\x57":ord('\x57'), "\x58":ord('\x58'), "\x59":ord('\x59'), "\x5a":ord('\x5a'), "\x5b":ord('\x5b'), "\x5c":ord('\x5c'), "\x5d":ord('\x5d'), "\x5e":ord('\x5e'), "\x5f":ord('\x5f'),
               "\x60":ord('\x60'), "\x61":ord('\x61'), "\x62":ord('\x62'), "\x63":ord('\x63'), "\x64":ord('\x64'), "\x65":ord('\x65'), "\x66":ord('\x66'), "\x67":ord('\x67'), "\x68":ord('\x68'), "\x69":ord('\x69'), "\x6a":ord('\x6a'), "\x6b":ord('\x6b'), "\x6c":ord('\x6c'), "\x6d":ord('\x6d'), "\x6e":ord('\x6e'), "\x6f":ord('\x6f'),
               "\x70":ord('\x70'), "\x71":ord('\x71'), "\x72":ord('\x72'), "\x73":ord('\x73'), "\x74":ord('\x74'), "\x75":ord('\x75'), "\x76":ord('\x76'), "\x77":ord('\x77'), "\x78":ord('\x78'), "\x79":ord('\x79'), "\x7a":ord('\x7a'), "\x7b":ord('\x7b'), "\x7c":ord('\x7c'), "\x7d":ord('\x7d'), "\x7e":ord('\x7e'), "\x7f":ord('\x7f'),
               "\x80":ord('\x80'), "\x81":ord('\x81'), "\x82":ord('\x82'), "\x83":ord('\x83'), "\x84":ord('\x84'), "\x85":ord('\x85'), "\x86":ord('\x86'), "\x87":ord('\x87'), "\x88":ord('\x88'), "\x89":ord('\x89'), "\x8a":ord('\x8a'), "\x8b":ord('\x8b'), "\x8c":ord('\x8c'), "\x8d":ord('\x8d'), "\x8e":ord('\x8e'), "\x8f":ord('\x8f'),
               "\x90":ord('\x90'), "\x91":ord('\x91'), "\x92":ord('\x92'), "\x93":ord('\x93'), "\x94":ord('\x94'), "\x95":ord('\x95'), "\x96":ord('\x96'), "\x97":ord('\x97'), "\x98":ord('\x98'), "\x99":ord('\x99'), "\x9a":ord('\x9a'), "\x9b":ord('\x9b'), "\x9c":ord('\x9c'), "\x9d":ord('\x9d'), "\x9e":ord('\x9e'), "\x9f":ord('\x9f')}

    def encodeSting(self, String2Encode):
        ##shift patterns##
        ##global my_Cypher
        Shift = 0
        tempStr = ""
        retVal = ""
        m = 0
        for ch in String2Encode:
            m += 1
            Shift = ord(ch) + (len(String2Encode) + m)
            i = chr(Shift)
            tempStr = str(i)
            retVal = retVal + chr(my_Cypher[tempStr])
        return retVal

    def decodeString(self, String2Decode):
        ##shift pattern reversed##
        global my_Cypher
        Shift = 0
        tempStr = ""
        retVal=""
        m=0
        for ch in String2Decode:
            m+=1
            Shift = ord(ch)-(len(String2Decode)+ m)
            i = chr(Shift)
            tempStr = str(i)
            retVal = retVal + chr(my_Cypher[tempStr])
        return retVal

    def validateString(self, String2Validate):
        ##checks for invalid chars in  the test string and returns true or false
        invalChars=['+','\'','\"']                          ## list of 'invalid' chars
        maximumLen = 30                                     ## Maximum number of chars allowed
        validBool = False                                   ## test Boolean
        if len(String2Validate) > maximumLen:               ## checks for next validation value
            validBool = False                               ## if too long return a false rating
            return validBool                                ## should return false if caught here
        if len(String2Validate) <= maximumLen:              ## checks if less than max,
            i = 0                                           ## sets string iterator t0 0
            while i < len(String2Validate):                 ## loop that while i less then len of string continues through
                for x in range(0, len(invalChars)):         ## for loop to iterate through invalid char array
                    char = String2Validate[i]               ## sets index of string i to char
                    if invalChars[x] == chr(ord(char)):     ## looks to see if i and x are the same
                        validBool = False                   ## an invalid char was used and returns false
                        return validBool                    ## returns false to caller as the string is containing an invalid char
                        break                               ## stops loop
                    else:                                   ## Else...
                        if i == len(String2Validate)-1:     ## if at the end of the string and no invalid chars are caught
                            validBool = True                ## set validBool to true
                            return validBool                ## returns validBool if valid.
                            break                           ## stops loop
                        else:                               ## if not long enough return to top to continue processing
                            pass                            ## pass to next statement
                i = i + 1                                   ## increments i for new run though
        else:                                               ## if the two other tests fail then it is valid
            validBool=True                                  ## returns true if True


## Class for Managers ##
## ------------------------------------------------------------
class Managers:

   def Prnt_Empl_Lst(self):
      ## For the use of printing out of the available Employees ##
      global Employee                                       ## set Global to table Employee for use in this code
      for Empl in Employee:                          ## This line needs to be coreected
         print str(Empl) +": ",
         for Empl1 in Employee[Empl]:
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
         print "You must be logged in as Super Admin User before you will be allowed to add managers.",
         print "Log off your user and log in as your Super Administrator to add a manager."
         AdminMenu()
      '''
      This function will require that you have Super Admin User logged in, this was done to help limit the ability
      of unauthorized manager adds.  DEFAULTS: Active=TRUE MgrLoggedIn=FALSE
      '''

   def Prnt_Mngr_Lst(self):
      global Manager
      for Mngr in Manager:
         print str(Mngr) +": ",
         for Mngr1 in Manager[Mngr]:
            print Manager[Mngr][Mngr1],
         print ""

   def ValidateMngr(self, MngrID): ##internal validation to ensure that a valid manager exists
      global Manager
      retVal=False
      if MngrID=="100": ## Super Admin Is ALWAYS Valid :)
         retVal=True
         return retVal
      elif MngrID in Manager:
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
