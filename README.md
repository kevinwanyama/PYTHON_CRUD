# PYTHON_CRUD
This is CRUD with Python and MySQL


#DB creation
Here, we will create a simple database as "Test" and will create a simple table as "Employee" as follows. Following is the SQL script for creating a database and table. You can directly execute it. Once it will execute successfully, you can find a Test database along with the Employee table in SQL Server.

CREATE DATABASE Test
GO

USE Test
GO

CREATE TABLE Employee(Id int PRIMARY KEY IDENTITY(1,1),	Names varchar(255) NULL,	Age int NULL)
