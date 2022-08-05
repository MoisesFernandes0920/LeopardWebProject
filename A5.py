from site import addsitepackages
import sqlite3
database = sqlite3.connect("A5db.db")
cursor = database.cursor()

blank_str = ' '

class User: 
# Constructor
    def __init__(self,first,last,IDnum,password):
        self.first = first
        self.last = last
        self.IDnum = IDnum
        self.password = password

class Student(User):
    def __init__(self,first,last,IDnum,password, courses):
        super().__init__(first,last,IDnum,password)

class Admin(User):
    def __init__(self,first,last,IDnum,password):
        super().__init__(first,last,IDnum,password)



class Instructor(User):
    def __init__(self,first,last,IDnum,password):
        super().__init__(first,last,IDnum,password)


def populate_courses(n):
    for i in range(n):
        insert_course()

    database.commit()

#moises
def insert_admin():
        print('Inserting admin:  \n')
        userid = input('ID:')
        pass_validation_flag = False
        while(pass_validation_flag == False):
            password = input('Password:  ')
            pass_confirm = input('Confirm Password:  ')
            if (password == pass_confirm):
                pass_validation_flag = True
            else:
                print('\nPasswords do not match, please try again:  \n')

        fname = input("First Name:")
        lname = input("Last Name:")
        title = input("Title:")
        office = input("Office:")
        email = input("Email:")
        cursor.execute("""INSERT INTO ADMIN VALUES ('%s','%s','%s','%s','%s','%s','%s')""" %(userid,password,fname,lname,title,office,email))
        admin1 = Admin(fname, lname, userid, password)
        print('\n')

#
def insert_student():
        print('Inserting student:  \n')
        userid = input('ID:')
        pass_validation_flag = False
        while(pass_validation_flag == False):
            password = input('Password:  ')
            pass_confirm = input('Confirm Password:  ')
            if (password == pass_confirm):
                pass_validation_flag = True
            else:
                print('\nPasswords do not match, please try again:  \n')
        fname  = input("First Name:")
        lname = input("Last Name:")
        gradyear = input("Graduation year:")
        major = input("Major:")
        email = input("Email:")
        cursor.execute("""INSERT INTO STUDENT VALUES('%s','%s','%s','%s','%s','%s','%s');""" %(userid,password,fname,lname,gradyear,major,email))
        print('\n')
        database.commit()


#moises
def insert_instructor():
        print('Inserting instructor:  \n')
        userid = input('ID:')
        pass_validation_flag = False
        while(pass_validation_flag == False):
            password = input('Password:  ')
            pass_confirm = input('Confirm Password:  ')
            if (password == pass_confirm):
                pass_validation_flag = True
            else:
                print('\nPasswords do not match, please try again:  \n')
        fname = input("First Name:")
        lname= input("Last Name:")
        title = input("Title:")
        hireyr = input("Year of Hire:")
        dept = input ("Department:")
        email = input("Email:")
        cursor.execute("""INSERT INTO INSTRUCTOR VALUES('%s','%s','%s','%s','%s','%s','%s','%s')""" %(userid,password,fname,lname,title,hireyr,dept,email))
        print('\n')
        database.commit()

#moises
def insert_course():
        crn = input('CRN: ')
        title = input("Course Title: ")
        instructor = input("Instructor Last Name:  ")
        dept = input("Department: ")
        time = input("Meeting Time: ")
        days = input('Meeting Days: ')
        semester = input('Semester: ')
        year = input("Year:")
        credits = input("Credits:")
        cursor.execute("""INSERT INTO COURSE VALUES ('%s', '%s','%s','%s','%s','%s','%s','%s','%s');""" % (crn,title, instructor, dept,time,days,semester,year,credits))
        database.commit()

#moises
def remove_course():
        crn = input("Enter the CRN code of the course you wish to remove: ")
        cursor.execute("""DELETE FROM COURSE WHERE CRN = '%s';""" %(crn))
        database.commit()

#benson & kevin
def login(user_type_int):
       
       if user_type_int == 1:
           user_pass_flag = False
           
           while user_pass_flag == False:
                user_id = input("Enter your ID:  ")
                user_password = input("Enter your Password:  ")
                cursor.execute("""SELECT NAME FROM STUDENT WHERE ID = '%s';""" % (user_id))
                id_result = cursor.fetchone()
                cursor.execute("""SELECT PASSWORD FROM STUDENT WHERE ID = '%s';""" % (user_id))
                password_result = cursor.fetchone()
                if user_password == str(password_result)[2:-3]:
                    user_pass_flag = True
                else:
                    print("Incorrect User ID or Password, try again.")
           print('\n Welcome,' + str(id_result)[2:-3] + '\n')

       elif user_type_int == 2:
           user_pass_flag = False
           
           while user_pass_flag == False:
                user_id = input("Enter your ID:  ")
                user_password = input("Enter your Password:  ")
                cursor.execute("""SELECT NAME FROM INSTRUCTOR WHERE ID = '%s';""" % (user_id))
                id_result = cursor.fetchone()
                cursor.execute("""SELECT PASSWORD FROM INSTRUCTOR WHERE ID = '%s';""" % (user_id))
                password_result = cursor.fetchone()
                if user_password == str(password_result)[2:-3]:
                    user_pass_flag = True
                else:
                    print("Incorrect User ID or Password, try again.")
           print('\n Welcome,' + str(id_result)[2:-3] + '\n')

       elif user_type_int == 3:
           user_pass_flag = False
           
           while user_pass_flag == False:
                user_id = input("Enter your ID:  ")
                user_password = input("Enter your Password:  ")
                cursor.execute("""SELECT NAME FROM ADMIN WHERE ID = '%s';""" % (user_id))
                id_result = cursor.fetchone()
                cursor.execute("""SELECT PASSWORD FROM ADMIN WHERE ID = '%s';""" % (user_id))
                password_result = cursor.fetchone()
                if user_password == str(password_result)[2:-3]:
                    user_pass_flag = True
                else:
                    print("Incorrect User ID or Password, try again.")
       
           print('\n Welcome, ' + str(id_result)[2:-3] + '\n')

#kevin
def Course_Search_By_Param():
        print("You can search based on the following parameters:  ")
        print("CRN")
        print("Title")
        print("Instructor")
        print("Department")
        print("Time - format: xx:xx xm")
        print("Days held")
        print("Semester and year")
        param = input("What parameter would you like to search based on? (Enter parameter):  ").upper()
        
        if param == 'CRN':
            value = input("Enter CRN:  ")
            cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s';""" % value)
            result = cursor.fetchall()

        elif param =='TITLE':
            value = input("Enter Title:  ")
            cursor.execute("""SELECT * FROM COURSE WHERE TITLE = '%s';""" % value)
            result = cursor.fetchall()

        elif param == 'INSTRUCTOR':
            value = input("Enter Instructor last name:  ")
            cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTOR = '%s';""" % value)
            result = cursor.fetchall()

        elif param == 'DEPARTMENT':
            value = input("Enter Department:  ")
            cursor.execute("""SELECT * FROM COURSE WHERE DEPARTMENT = '%s';""" % value)
            result = cursor.fetchall()

        elif param == 'TIME':
            value = input("Enter Time:  ")
            cursor.execute("""SELECT * FROM COURSE WHERE TIME = '%s';""" % value)
            result = cursor.fetchall()

        elif param == 'DAYS HELD':
            value = input("Enter days held:  ")
            cursor.execute("""SELECT * FROM COURSE WHERE DAYS = '%s';""" % value)
            result = cursor.fetchall()

        elif param == 'SEMESTER AND YEAR':
            value1 = input("Enter Semester held:  ")
            value2 = input("Enter Year held:  ")
            cursor.execute("""SELECT * FROM COURSE WHERE SEMESTER = '%s' & YEAR = '%s';""" % (value1, value2))
            result = cursor.fetchall()


        for i in result:
            print(i)
        
#kevin
def Search_Course_CRN(crn):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s';""" % crn)
        result = cursor.fetchall()

        for i in result:
            print(i)

#kevin
def print_instructor_roster(last_name):
    cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTOR = '%s';""" % last_name)
    result = cursor.fetchall()
    for i in result:
        print(i)

#kevin
def add_to_roster(crn, name):
    cursor.execute("""UPDATE COURSE SET INSTRUCTOR = '%s' WHERE CRN = '%s';""" % (name, crn))
    database.commit()

#kevin
def remove_from_course(crn):
    cursor.execute("""UPDATE COURSE SET INSTRUCTOR = '%s' WHERE CRN  = '%s';""" % (blank_str, crn))
    database.commit()

#kevin
def get_course(crn):
    cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s';""" % crn)
    return(cursor.fetchone())



        




#Main Method - Coded by Kevin
print('Welcome to Leopardweb!')

user_type = input('Please enter the type of user you you like to login: \n \n \t 1 - Student \n \t 2 - Instructor \n \t 3 - Admin \n')


while (True):
    if user_type == '1':
        print('Welcome, Student!')
        login(1)
        student_choice = 0
        student_schedule = []
        while (True):
            print('What would you like to do? (Type command)')
            student_choice = input('\n \n \t add - Add Course to Schedule \n \t remove - Remove Course from schedule \n \t Schedule - Print schedule \n \t CRN search - Search Courses by CRN \n \t parameter search - Search Course by parameter \n \t logout - Logout and Exit \n').upper()
            #student_choice = input()
            if student_choice == 'ADD':
                #add course to student schedule
                current_crn = input('Type the crn of the course you would like to add:  ')
                student_schedule.append(get_course(current_crn))

            elif student_choice == 'REMOVE':
                #remove course from student schedule
                
                urrent_crn = input('Type the crn of the course you would like to remove:  ')
                student_schedule.remove(get_course(current_crn))

            elif student_choice == 'SCHEDULE':
                print(student_schedule)

            elif student_choice == 'CRN SEARCH':
                crn = input("Enter CRN:  ")
                Search_Course_CRN(crn)

            elif student_choice == 'PARAMETER SEARCH':
                Course_Search_By_Param()

            elif student_choice == 'LOGOUT':
                break

            else:
                print("Command not recognized - please enter another command: \n")


        break
    elif user_type == '2':
        print('Welcome, Instructor!')
        login(2)
        instructor_choice = 0
        while (instructor_choice != 9):
            print('What would you like to do?')
            instructor_choice = input('\n \n \t add - Add Course to Roster \n \t remove - Remove Course from Roster \n \t CRN search - Search Courses by CRN \n \t parameter search - Search Course by parameter  \n \t roster - Print instructor roster\n \t logout - Logout and Exit \n').upper()
            
            
            if instructor_choice == 'ADD':
                #add course to instructor schedule
                
                crn = input('Enter the crn of the course you would like to add:  ')
                name = input('Enter your last name (Instructor name):  ')
                add_to_roster(crn, name)
            elif instructor_choice == 'REMOVE':
                #remove course from instructor schedule
                
                crn = input('Enter the crn you would like to remove from roster:  ')
                remove_from_course(crn)

            elif instructor_choice == 'CRN SEARCH':
                crn = input("Enter CRN:  ")
                Search_Course_CRN(crn)

            elif instructor_choice == 'PARAMETER SEARCH':
                Course_Search_By_Param()

            elif instructor_choice == 'ROSTER':
                
                last = input('Print Last name of roster to be printed:  ')
                print_instructor_roster(last)

            elif instructor_choice == 'LOGOUT':
                break

            else:
                print("Command not recognized - please enter another command: \n")

            
        break
    elif user_type == '3':
        print('Welcome, Admin!')
        login(3)
        admin_choice = 0
        while (admin_choice != 9):
            print('What would you like to do?')
            admin_choice = input('\n \n \t add course - Add Course to System \n \t remove course- Remove Course from System \n \t search crn - Search Courses by CRN \n \t search parameter - Search Course by parameter \n \t add student - Add student to system \n \t add instructor - add instructor to system \n \t logout - Logout and Exit \n').upper()
            
            if admin_choice == 'ADD COURSE':
                #add course to system
                insert_course()
                
            elif admin_choice == 'REMOVE COURSE':
                #remove course from system
                remove_course()

            elif admin_choice == 'SEARCH CRN':
                crn = input("Enter CRN:  ")
                Search_Course_CRN(crn)

            elif admin_choice == 'SEARCH PARAMETER':
                Course_Search_By_Param()

            elif admin_choice == 'ADD STUDENT':
                insert_student()

            elif admin_choice == 'ADD INSTRUCTOR':
                insert_instructor()

            elif admin_choice == 'LOGOUT':
                break

            else:
                print("Command not recognized - please enter another command: \n")
        break
    else:
        print('Please enter a valid user type: ')
        user_type = input()

print("Thank you for choosing LeopardWeb!  Goodbye")




database.commit()
database.close()


