# This statememnt imports
import sqlite3 as sql

# Creating Class Table  Moises Coded 
database.execute("""CREATE TABLE COURSE 
(
CRN INT PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
DEPARTMENT TEXT NOT NULL,
TIME TEXT NOT NULL,
DAYS TEXT NOT NULL,
SEMESTER TEXT NOT NULL,
YEAR INT NOT NULL,
CREDITS INT NOT NULL); """)

# Course Creation Function Moises Coded 
# This function will add courses to the course table 
def insert_course(cursor):
    crn = input('CRN: ')
    title = input("Course Title: ")
    dept = input("Department: ")
    time = input("Meeting Time: ")
    days = input('Meeting Days: ')
    semester = input('Semester: ')
    year = input("Year:")
    credits = input("Credits:")
    cursor.execute("""INSERT INTO COURSE VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',);""" % (crn,title,dept,time,days,semester,year,credits))

# Remove Course Function Moises Coded 
# This function will remove courses from the course table 
def remove_course(cursor):
    crn = input("Enter the CRN code of the course you wish to remove: ")
    cursor.execute("""DELETE FROM COURSE WHERE CRN = '%s';""" %(crn))

# Creating Student Table Moises Coded 
database.execute("""CREATE TABLE STUDENT
(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL,
GRADYEAR INT NOT NULL,
MAJOR CHAR(4) NOT NULL,
EMAIL TEXT NOT NULL,
); """)

# Student Creation Function Moises Coded 
# This function will add students to the student table 

def insert_student(cursor):
    userid = input('ID:')
    fname  = input("First Name:")
    lname = input("Last Name:")
    gradyear = input("Graduation year:")
    major = input("Major:")
    email = input("Email:")
    cursor.execute("""INSERT INTO STUDENT VALUES('%s',%s',%s',%s',%s',%s',);""" %(userid,fname,lname,gradyear,major,email))
     
# Creating Instructor Table Moises Coded 
database.execute("""CREATE TABLE INSTRUCTOR
(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL, 
TITLE TEXT NOT NULL,
HIREYEAR INT NOT NULL,
DEPT CHAR(4) NOT NULL,
EMAIL TEXT NOT NULL,
); """ )

# Instructor Creation Function Moises Coded 
# This Function will add instructors to the instructor table 

def insert_instructor(cursor):
    userid = input('ID:')
    fname = input("First Name:")
    lname= input("Last Name:")
    title = input("Title:")
    hireyr = input("Year of Hire:")
    dept = input ("Department:")
    email = input("Email:")
    cursor.execute("""INSERT INTO INSTRUCTOR VALUES('%s','%s','%s','%s','%s','%s','%s',)""" %(userid,fname,lname,title,hireyr,dept,email))

# Creating Admin Table Moises Coded 
database.execute("""CREATE TABLE ADMIN
(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL,
TITLE TEXT NOT NULL,
OFFICE TEXT NOT NULL,
EMAIL TEXT NOT NULL,
);""" )

# Admin Creation Function Moises Coded 
# This Function will add admins to the admin table 
def insert_admin(cursor):
    userid = input('ID:')
    fname = input("First Name:")
    lname = input("Last Name:")
    title = input("Title:")
    office = input("Office:")
    email = input("Email:")
    cursor.execute("""INSERT INTO ADMIN VALUES ('%s','%s','%s','%s','%s','%s')""" %(userid,fname,lname,title,office,email))

