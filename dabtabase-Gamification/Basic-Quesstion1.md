# basic SQL question
## **we are given the following employee table of a newly established company**
## **The `employee` table has the records of 30 employees:**

| employee_id | first_name | last_name | department | salary   | hire_date   |
|-------------|------------|-----------|------------|----------|-------------|
| 1           | Ram        | Sharma    | HR         | 45000.00 | 2023-01-15  |
| 2           | Sita       | Thapa     | IT         | 55000.00 | 2023-02-10  |
| 3           | Hari       | Magar     | Finance    | 47000.00 | 2023-03-05  |
| 4           | Gita       | Bhandari  | Sales      | 40000.00 | 2023-04-20  |
| 5           | Krishna    | Poudel    | IT         | 60000.00 | 2023-05-15  |
| 6           | Rita       | Khadka    | HR         | 46000.00 | 2023-06-01  |
| 7           | Bikash     | Adhikari  | Marketing  | 52000.00 | 2023-07-10  |
| 8           | Mina       | Rai       | Finance    | 48000.00 | 2023-08-25  |
| 9           | Suraj      | Tamang    | IT         | 62000.00 | 2023-09-12  |
| 10          | Anita      | Gurung    | Sales      | 43000.00 | 2023-10-02  |
| 11          | Prakash    | Basnet    | HR         | 45000.00 | 2023-11-14  |
| 12          | Sunita     | Lama      | Finance    | 50000.00 | 2023-12-01  |
| 13          | Ramesh     | Shrestha  | Marketing  | 52000.00 | 2024-01-03  |
| 14          | Bina       | Shah      | IT         | 61000.00 | 2024-02-12  |
| 15          | Manoj      | Maharjan  | Sales      | 41000.00 | 2024-03-08  |
| 16          | Sarita     | Karki     | HR         | 46000.00 | 2024-04-15  |
| 17          | Dinesh     | Koirala   | Finance    | 48000.00 | 2024-05-22  |
| 18          | Sujata     | Bhattarai | Marketing  | 51000.00 | 2024-06-10  |
| 19          | Rajesh     | KC        | IT         | 63000.00 | 2024-07-05  |
| 20          | Sanjay     | Malla     | Sales      | 42000.00 | 2024-08-18  |
| 21          | Usha       | Pant      | HR         | 45000.00 | 2024-09-27  |
| 22          | Santosh    | Ghimire   | Finance    | 47000.00 | 2024-10-06  |
| 23          | Binita     | Dangol    | Marketing  | 50000.00 | 2024-11-11  |
| 24          | Ashok      | Tiwari    | IT         | 62000.00 | 2024-12-02  |
| 25          | Kalpana    | Acharya   | Sales      | 43000.00 | 2024-12-25  |
| 26          | Dipesh     | Rana      | Finance    | 48000.00 | 2025-01-09  |
| 27          | Jyoti      | Nepali    | HR         | 46000.00 | 2025-02-17  |
| 28          | Niraj      | Panta     | Marketing  | 53000.00 | 2025-03-22  |
| 29          | Meena      | Gautam    | IT         | 62000.00 | 2025-04-05  |
| 30          | Madan      | Luitel    | Finance    | 48000.00 | 2025-05-15  |

### Explanation of Columns:
- `employee_id`: A unique identifier for each employee, auto-incremented.
- `first_name`: The first name of the employee.
- `last_name`: The last name (surname) of the employee.
- `department`: The department where the employee works (e.g., HR, IT, Finance, etc.).
- `salary`: The salary of the employee.
- `hire_date`: The date the employee was hired.

Each row represents an employee with their corresponding details.

### **The query used to create the emoloyee table is given below**

```sql
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);
```
--- 
# `questions` with their splutions

### 1. Retrieve all employee details.
```sql
SELECT * FROM employee;
```

### 2. Get the first name, last name, and salary of all employees in the IT department.
```sql
SELECT first_name, last_name, salary 
FROM employee 
WHERE department = 'IT';
```

### 3. Find the employees hired after '2024-01-01'.
```sql
SELECT first_name, last_name, hire_date 
FROM employee 
WHERE hire_date > '2024-01-01';
```

### 4. List the top 5 highest paid employees.
```sql
SELECT first_name, last_name, salary 
FROM employee 
ORDER BY salary DESC 
LIMIT 5;
```

### 5. Count the number of employees in each department.
```sql
SELECT department, COUNT(*) AS employee_count 
FROM employee 
GROUP BY department;
```

### 6. Calculate the average salary of employees in the Finance department.
```sql
SELECT AVG(salary) AS avg_salary 
FROM employee 
WHERE department = 'Finance';
```

### 7. Find the total salary paid to employees in the Sales department.
```sql
SELECT SUM(salary) AS total_salary 
FROM employee 
WHERE department = 'Sales';
```

### 8. Update the salary of employees in the HR department, giving them a 10% raise.
```sql
UPDATE employee 
SET salary = salary * 1.10 
WHERE department = 'HR';
```

### 9. Delete all employees who were hired before '2023-06-01'.
```sql
DELETE FROM employee 
WHERE hire_date < '2023-06-01';
```

### 10. Find the employee(s) with the highest salary.
```sql
SELECT first_name, last_name, salary 
FROM employee 
WHERE salary = (SELECT MAX(salary) FROM employee);
```

These questions cover common SQL concepts such as `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `JOIN`, `UPDATE`, and `DELETE`, focusing on operations commonly used in querying an `employee` table.
