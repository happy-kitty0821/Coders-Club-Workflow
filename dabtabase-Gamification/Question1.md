# This SALES table leads to modification anomalies.

#  **`SALES Table`**

| CustomerID | Products | Price |
|----------|----------|----------|
| 1001 | Toothpaste | 50 |
| 1020 | Clorine Bleach | 450 |
| 3121 | ToothBrush | 45 |
| 1012 | Laundry Detergent | 100 |
| 1011 | Detol Soap Bar | 80 |
| 1021 | Nail Polish | 25 |


---

## **we are given the table named `SALES` the table has three columns named CustomerID, Products and the Price of the Products, now lets us suppose the following:**

**our company sells household cleaning and
personal-care products, and you charge all customers the same price for
each product. The SALES table keeps track of everything for you. Now
assume that customer 1001 moves out of the area and no longer is a
customer. You don’t care what he’s bought in the past, because he’s not
going to buy anything from your company again. You want to delete his
row from the table. If you do so, however, you don’t just lose the fact
that customer 1001 has bought  Toothpaste; you also lose the fact
that laundry detergent costs Rss. 50. This situation is called a deletion
anomaly. In deleting one fact (that customer 1001 bought Toothpaste), you inadvertently delete another fact (that the toothpaste
costs Rs 50).
You can use the same table to illustrate an insertion anomaly. For
example, suppose you want to add stick deodorant to your product line
at a price of Rs 200. You can’t add this data to the SALES table until a
customer buys stick deodorant.
The problem with the SALES table in the figure is that this table deals
with more than one thing: It covers not just which products customers
buy, but also what the products cost.**

---

### **`To create the SALES table the following query was used`**
```sql

CREATE TABLE SALES (
    CustomerID INT,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2),
    PRIMARY KEY (CustomerID, ProductName)
);

```

---
## **your task is to solve this issue and design a new talble which do not face this same issue**
## **you are free to make as many table as you like, but when creating your solution use the following values:**
```sql 
varchar = 255
Decimal = 10,2
```


#**All the Possible Solutions**

## **By creating three tables**
---
``` SQL
--product table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

```

---

``` SQL

create table products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

create table Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255)
);

create table Sales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
