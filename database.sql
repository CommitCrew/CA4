create database studenInfo;
use studentInfo;

create table students(

		StudentID int,
        FirstName varchar(50),
        LastName varchar(50),
        Primary key(StudentID)   
);
Insert INTO students(StudentID,FirstName,LastName)
Values(1,"Fatima","Abdul Wahid"),(2,"Zuha","Umar"),(3,"Hadiya","Farooq");