DROP DATABASE IF EXISTS lab3BulkTest;
CREATE DATABASE lab3BulkTest;

use lab3BulkTest;

CREATE TABLE Customers(
    CustomerID int NOT NULL,
    Gender varchar(255) NOT NULL,
    Age int NOT NULL,
    AnnualIncome int NOT NULL,
    SpendingScore int NOT NULL,
    Profession varchar(255) NOT NULL,
    WorkExperience int NOT NULL,
    FamilySize int NOT NULL
);