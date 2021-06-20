import mysql.connector as co

class stud_func:

    
    def add_student(self):
        mydb = co.connect(host = "localhost", user = "root", password = "Vyssql#07", database = "ss")
        cursor = mydb.cursor()
        
        name = input("Student name :")
        id = input("Student id :")
        colg = input("College :")
        dept = input("Enter dept:")
        mark1 = int(input("Enter marks of subject 1:"))
        mark2 = int(input("Enter marks of subject 2:"))
        mark3 = int(input("Enter marks of subject 3:"))
        mark4 = int(input("Enter marks of subject 4:"))
        mark5 = int(input("Enter marks of subject 5:"))
        tot_marks = mark1 + mark2 + mark3 + mark4 + mark5
        avg = (tot_marks) /5
        if avg > 75:
            grade = "A"
        elif avg > 50 and avg < 75:
            grade = "B"
        else :
            grade = "F"
        w = ("insert into st (id,sname, colg, dept, m1, m2, m3, m4, m5, tot_marks, perc, grade) values (%s,%s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s)")
        v = (id, name, colg, dept, mark1, mark2, mark3, mark4, mark5, tot_marks, avg, grade)
        cursor.execute(w,v)
        mydb.commit()
        print("Record added of student :" + name)
    
    def search(self):
        
        c =input("Enter student ID :")
        try:
            mydb = co.connect(host = "localhost", user = "root", password = "Vyssql#07", database = "ss")
            cursor = mydb.cursor()
            q = ("SELECT * FROM st WHERE id = " +c ) 
            cursor.execute(q)
            res = cursor.fetchall()
            print("The record of the student is :") 
            for i in res:
                print(i)
        except :
            print("Invalid ID.")
    
    
          

    
    def update(self):
        
        print("Enter your choice : ")
        b = input("1. Update name \n2. Update college name \n3. Update Department ")
        if b== '1':
            try:
                mydb = co.connect(host = "localhost", user = "root", password = "Vyssql#07", database = "ss")
                cursor = mydb.cursor()
                c = input("Enter student ID for Name update : ")
                nn = input("Enter new name :")
                q = ("UPDATE st SET sname = %s WHERE id =  %s")
                val = (nn,c)
                cursor.execute(q,val)
                mydb.commit()
                print("Name updated!!")
            except :
                print("Invalid ID")

    
        elif b == '2':
            try :
                mydb = co.connect(host = "localhost", user = "root", password = "Vyssql#07", database = "ss")
                cursor = mydb.cursor()
                c = input("Enter student ID for College name update : ")
                nn = input("Enter new college name : ")
                q = ("UPDATE st SET colg = %s WHERE id =  %s")
                val = (nn, c)
                cursor.execute(q,val)
                mydb.commit()
                print("College Name updated!!") 
            except :
                print("Invalid ID")
        
        elif b == '3':
            try :
                mydb = co.connect(host = "localhost", user = "root", password = "Vyssql#07", database = "ss")
                cursor = mydb.cursor()
                c = input("Enter student ID for Dept name update : ")
                nn = input("Enter new dept name : ")
                q = ("UPDATE st SET dept = %s WHERE id =  %s")
                val = (nn, c)
                cursor.execute(q,val)
                mydb.commit()
                print("Dept Name updated!!") 
                
            except :
                print("Invalid ID")
                
            
        else :
            print("Invalid choice !")
            
 
    def getall(self):
        mydb = co.connect(host = "localhost", user = "root", password = "Vyssql#07", database = "ss")
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROm st ")
        res = cursor.fetchall()
        for x in res:
            print (x) 
    
    def delete(self):
        try :
            mydb = co.connect(host = "localhost", user = "root", password = "Vyssql#07", database = "ss")
            cursor = mydb.cursor()
            c = input("Enter ID to delete")
            q = ("DELETE FROM st WHERE id = "+c) 
            cursor.execute(q)
            mydb.commit()
        except :
            print("invalid ID!")
    
        

     

    
def main():
    s1 = stud_func()
    while True:

        print ("\n Enter your choice :")
        print ("1. Add student \n2. Search \n3. Update \n4. Show all students \n5. Delete  \n6.Exit :")
        ch = int(input())
        if ch == 1 :
            s1.add_student()
        elif ch==2 :
            s1.search()
        elif ch == 3:
            s1.update()
        elif ch == 4 :
            s1.getall()
        elif ch == 5 :
            s1.delete()
        elif ch == 6 :
            print("Thank you!")
        
main()