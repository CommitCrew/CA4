create database studentsInfo;
use studentsInfo;

create table stduentsInfo(

		StudentID int,
        FirstName varchar(50),
        LastName varchar(50),
        Primary key(StudentID)
        
);
Insert INTO stduentsInfo(StudentID,FirstName,LastName)
Values(1,"Fatima","Abdul Wahid"),(2,"Zuha","Umar"),(3,"Hadiya","Farooq");