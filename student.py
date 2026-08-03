from db import conn,cursor
def add_student():
    name=input("ENTER NAME:")
    age=int(input("ENTER AGE:"))
    branch=input("ENTER BRANCH:")
    email=input("ENTER EMAIL:")
    query= """
    insert into students(name,age,branch,email)
    values(%s,%s,%s,%s)"""

    values=(name,age,branch,email)
    cursor.execute(query, values) #To execute the sql Queries

    conn.commit()   #to save the changes in databases.

    print("Student Added Successfully!")

# to view the students
def view_students():

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    print("\n------ Student Records ------")

    for student in students:
        print(student)
# to search the students details
def search_student():
    student_id=int(input("enter id:"))
    query="select* from students where id=%s"
    cursor.execute(query,(student_id,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print(f"ID      : {student[0]}")
        print(f"Name    : {student[1]}")
        print(f"Age     : {student[2]}")
        print(f"Branch : {student[3]}")
        print(f"Email   : {student[4]}")
    else:
        print("Student Not Found!")

#to update the student details

def update_student():
    student_id=int(input("enter id:"))
    name=input("ENTER NAME:")
    age=int(input("ENTER AGE:"))
    branch=input("ENTER BRANCH:")
    email=input("ENTER EMAIL:")
    query="""UPDATE students
          SET name=%s, age=%s, branch=%s, email=%s
          WHERE id=%s"""
    values=(name,age,branch,email,student_id)
    cursor.execute(query,values)
    conn.commit()
    print("Student Updated Successfully!")

# delete student details
def delete_student():
    student_id=int(input("enter id:"))
    query="delete from students where id=%s"
    cursor.execute(query,(student_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student ID Not Found!")
   