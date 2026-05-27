import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="121896",database="student_database")

db_cursor=conn.cursor()


def show_menu():
    print("===========STUDENT MANAGEMENT SYSTEM==============")
    print('''
        1. Add Student
        2. View Student
        3. Update Student
        4. Delete Student
        5. Display All Students
        6. Exit'''
    )




class Student:
    def __init__(self):
        pass

    @staticmethod
    def search():
        while True:
            show_menu()
            

            try:
                choice=int(input("Enter your choice(1-6): "))
            except ValueError:
                print("Enter a valid number!")
                continue

        

            match choice:
                case 1:
                    while True:
                        std_id=input("Enter your student ID: ")
                        if not (std_id.isdigit() and len(std_id)==4):
                            print("ID must be 4 digit number!")
                            continue
                        break

                    while True:
                        name=input("Enter your name: ")
                        if not name.replace(" ","").isalpha():
                            print("Please enter alphabetical words")
                            continue
                        break
                

                    while True:
                        try:
                            age=int(input("Enter your age: "))
                        except ValueError as e:
                            print(e)
                            continue
                        break

                    while True:
                        department=input("Enter your department: ")
                        if not department.replace(" ","").isalpha():
                            print("Please enter alphabetical words")
                            continue
                        break


                    try:
                        db_cursor.execute('''
                                      INSERT INTO users(Student_id,Name,Age,Department) VALUES
                                      (%s,%s,%s,%s)''',(std_id,name,age,department))
                        conn.commit()

                        print("Student added successfully")
                    except Exception as e:
                        print("Error: ",e)

                case 2:
                    while True:
                        id=input("Enter Student ID to search: ")
                        if not id.isdigit(): 
                            print("Wrong input!")
                            continue

                        try:
                            db_cursor.execute('''select * from users where Student_id=%s''',(id,))
                            data=db_cursor.fetchone()
                        except Exception as e:
                            print("Error: ",e)
                       
                        if data:
                            print("Student Found")
                            print(f"ID: {data[0]}, Name: {data[1]}, Age: {data[2]}, Department: {data[3]} ")
                        else:
                            print("student not found!")
                            continue

                        break


                case 3:
                    while True:
                        id=input("Enter Student ID to search: ")
                        if not id.isdigit(): 
                            print("Wrong input!")
                            continue
                        
                        try:
                            db_cursor.execute('''select Student_id from users where Student_id=%s''',(id,))
                            data=db_cursor.fetchone()
                        except Exception as e:
                            print("Error: ",e)


                        if data: 
                            print('''
                            1.Update your age
                            2.Update your department
                            ''')
                            try:
                                choice1=int(input("Enter your choice(1-2): "))
                            except ValueError:
                                print("Enter a valid number!")
                                continue 


                            match choice1:
                                     case 1:
                                         try:
                                             age1=int(input("Enter your age: "))
                                         except ValueError as e:
                                             print(e)
                                             continue 

                                         try:  
                                            db_cursor.execute('''update users set Age=%s where Student_id=%s''',(age1,id))
                                            conn.commit()
                                            print("Age updated successfully")
                                            break  
                                         except Exception as e:
                                            print("Error: ",e)
                                     case 2:
                                         try:
                                             dept1=input("Enter your department: ")
                                         except ValueError as e:
                                             print(e)
                                             continue
                                         
                                         try:
                                            db_cursor.execute('''update users set Department=%s where Student_id=%s''',(dept1,id))
                                            conn.commit()
                                            print("Department updated successfully")
                                            break
                                         except Exception as e:
                                           print("Error: ",e)
                                     case _:
                                         print("Invalid choice")
                                         continue
                                         
                            
                                
                        else:
                            print("Student not found")
                


                case 4:
                    while True:
                        id=input("Enter Student ID to search: ")
                        if not id.isdigit(): 
                            print("Wrong input!")
                            continue
                        
                        try:
                            db_cursor.execute('''select Student_id from users where Student_id=%s''',(id,))
                            data=db_cursor.fetchone()
                        except Exception as e:
                            print("Error: ",e)

                        if data:
                            try:
                                db_cursor.execute('''delete from users where Student_id=%s''',(id,))
                                conn.commit()
                            except Exception as e:
                                print("Error: ",e)
                            print("Record deleted successfully")
                            break

                        else:
                            print("Student not found")


                case 5:
                        db_cursor.execute('''select * from users''')
                        data=db_cursor.fetchall()
                       
                        if data:
                            print("Student data :")
                            print("-"*55)
                            print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<15}")
                            print("-" * 55)

                            for row in data:
                                print(f"{row[0]:<10}{row[1]:<20}{row[2]:<10}{row[3]:<15} ")

                            print("-"*55)

                        else :
                            print("No record found")
                                                     
        
                case 6:
                    print("Thank you for using Student Management System!\nProgram terminated.")
                    break
                case _:
                    print("Invalid choice")
                    continue



a=Student()
a.search()

