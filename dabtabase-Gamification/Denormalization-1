### **Denormalization Exercise**

In this exercise, we will further explore the concept of denormalization by merging data from multiple normalized tables, combining information about employees and the projects they are working on.

### Scenario:

You are managing a company's database, where employee and project information is stored in separate normalized tables:

#### **`employee` table:**

| employee_id | first_name | last_name | salary   | department_id |
|-------------|------------|-----------|----------|---------------|
| 1           | Ram        | Sharma    | 45000.00 | 1             |
| 2           | Sita       | Thapa     | 55000.00 | 2             |
| 3           | Hari       | Magar     | 47000.00 | 3             |

#### **`project` table:**

| project_id  | project_name    |
|-------------|-----------------|
| 101         | Alpha           |
| 102         | Beta            |
| 103         | Gamma           |

#### **`employee_project` table:**

| employee_id | project_id |
|-------------|------------|
| 1           | 101        |
| 1           | 102        |
| 2           | 103        |
| 3           | 101        |

### Task:

**Question:**
Write a query to **denormalize** the data by combining the `employee`, `project`, and `employee_project` tables into a single table, showing the employee's first name, last name, department, and the projects they are working on.

**Expected Result:**

| first_name | last_name | department_id | project_name |
|------------|-----------|---------------|--------------|
| Ram        | Sharma    | 1             | Alpha        |
| Ram        | Sharma    | 1             | Beta         |
| Sita       | Thapa     | 2             | Gamma        |
| Hari       | Magar     | 3             | Alpha        |

**Solution:**

```sql
SELECT e.first_name, e.last_name, e.department_id, p.project_name
FROM employee e
JOIN employee_project ep ON e.employee_id = ep.employee_id
JOIN project p ON ep.project_id = p.project_id;
```

### Explanation:

- The `employee_project` table acts as a bridge between the `employee` and `project` tables, representing which employees are working on which projects.
- We use two `JOIN` operations: one to connect the `employee` and `employee_project` tables via `employee_id`, and another to connect the `employee_project` and `project` tables via `project_id`.
- The result combines information about employees and their associated projects, effectively denormalizing the data.

This kind of denormalization helps when you need to generate reports that combine data from multiple entities, such as employee details and project assignments, for better performance in read-heavy environments.
