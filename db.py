from tabulate import tabulate
import mysql.connector as sql
 
# Creating connection object
mydb = sql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "<your password>",
    database="<your database name>"
)

#insert function
def insert(sname,age):
    res=mydb.cursor()
    sql="insert into student(sname,age) values(%s,%s)"
    stored=(sname,age)
    res.execute(sql,stored)
    mydb.commit()
    print(" inserted successfully ")

#update function
def update(id,name,age):
    res=mydb.cursor()
    sql="update student set sname=%s,age=%s where id=%s"
    stored=(name,age,id,)
    res.execute(sql,stored)
    mydb.commit()
    print(id,"successfully updated")

#select function
def select():
    res = mydb.cursor()
    sql = "SELECT * from student"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","STUDENT_NAME","AGE"]))

#delete function
def delete(id):
    res=mydb.cursor()
    sql="delete from student where id=%s"
    stored=(id,)
    res.execute(sql,stored)
    mydb.commit()
    print(id,"is succesfully deleted")

#colunmn deleted function
def columndelete(name):
    res=mydb.cursor()
    sql=f"alter table student drop column `{name}`"
    res.execute(sql)
    mydb.commit()
    print(name+"successfully column deleted")


#continuous run
while True:
    
    print("\n1.insert")
    print("2.select")
    print("3.update")
    print("4.delete")
    print("5.column delete")
    
    print("6.exit\n")
    
    
    choice=int(input("enter your choice:"))
    print("\n")

    if choice==1:
        name=str(input("enter a name :"))
        age=int(input("enter age :"))
        insert(name,age)
    
    elif choice==2:
        select()

    elif choice==3:
        id=int(input("enter id :"))
        name=str(input("enter a name :"))
        age=int(input("enter age :"))
        update(id,name,age)

    elif choice==4:
        id=int(input("enter id :"))
        delete(id)

    elif choice==5:
        DelName=str(input("enter a column name :"))
        columndelete(DelName)

    elif choice==6:
        quit()

    else:
        print("the choices is not available,try again")