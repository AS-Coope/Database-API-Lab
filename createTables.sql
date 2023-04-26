DROP DATABASE IF EXISTS Lab3Work;
CREATE DATABASE Lab3Work;

use lab3Work;

CREATE TABLE Customers(
    CustomerID int NOT NULL,
    Gender varchar(255) NOT NULL,
    Age int NOT NULL,
    AnnualIncome int NOT NULL,
    SpendingScore int NOT NULL,
    Profession varchar(255) NOT NULL,
    WorkExperience int NOT NULL,
    FamilySize int NOT NULL,
    PRIMARY KEY (CustomerID)
);