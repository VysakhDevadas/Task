import re
import mysql.connector as co
mydb=co.connect(host = "localhost", user ="root", password = "Vyssql#07", database = "ss")

def signup():
    flag = 1
    cursor = mydb.cursor()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    id = input("Enter email ID of the format johndoe@example.com :")
    
    if not (re.search(regex,id)):
        print("Email ID INVALID FORMAT") 
        flag = -1
    else :
        print("Valid Email ID")
        flag = 1
    while flag == 1:  
        ps = input("Enter a valid password ")
        if len(ps)<5 or len(ps)>16 :
            print("Password length should be between 5 and 16 characters!")
            flag = 1
        elif not re.search ("[a-z]",ps) :
            print(" Password should contain atleast one small letter ")
            flag = 1
        elif not re.search("[A-Z]", ps) :
            print(' There should be one capital letter!')
            flag = 1
        elif not re.search("[0-9]", ps):
            print("Password should contain atleast one digit")
            flag = 1
        elif not re.search("[!@#$%^&*()_=)]", ps):
            print("Password should contain a special character")
            flag = 1
        else :
            print("Password is valid")
            flag = -1
            
    val = (id,ps)
    query = "Insert into id( emid, pass) values(%s,%s)"
    cursor.execute(query,val)
    mydb.commit()
    print("Entry added!")
    
def login():
    idl = input("Please enter email id for login :")
    ps = input("Please enter the correct password")
    cursor = mydb.cursor()
    val = (idl,ps)
    try :
        q = ("Select emid, pass from id Where (emid = %s and pass = %s)")
        cursor.execute(q,val)
        

        
def main():
    while 1:
        print("!!  Welcome !! ")
        ch = int(input("Select your choice: \n 1. Sign up (Register for new user) ) \n 2. Login (For registered users) \n 3. Exit."))
        if ch == 1 :
            signup()
        elif ch == 2 :
            login()
        elif ch ==3 :
            print("Visit again  !!")
        else :
            print("You have entered an invalid choice !!!")   

main()
    
 
        

 

