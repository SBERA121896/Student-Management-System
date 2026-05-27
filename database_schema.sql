CREATE DATABASE student_database;
use student_database;
create table users(
	Student_id varchar(100) primary key,
	Name varchar(100) not null,
	Age int not null,
	Department varchar(100) not null
);
