### **Scenario 1 E-Commerce Store**

**Overview:**  
Design a database system for an online store that sells various products. The store allows customers to make multiple purchases, and suppliers provide the products. Customers can write reviews for the products they buy, and each review can include ratings.

**Questions:**

1. **Customers and Orders**  
   Design a system where customers can place multiple orders. Each order can contain several products. How will you model the relationship between **Customers** and **Orders**?

2. **Products and Suppliers**  
   Suppliers can provide multiple products, and each product can come from multiple suppliers. Create the necessary tables and relationships to handle this many-to-many scenario between **Products** and **Suppliers**.

3. **Customers and Reviews**  
   Customers can write reviews for products they have purchased. A product can have multiple reviews from different customers. Create a schema that links **Customers** with their **Reviews** and **Products**.

---

### **Scenario 2: University Course Enrollment System**

**Overview:**  
Create a database for a university system that tracks students, courses, instructors, and enrollments. Students can enroll in multiple courses, and each course can have more than one instructor.

**Questions:**

1. **Students and Courses**  
   Students can enroll in multiple courses, and each course can have many students. How will you handle this many-to-many relationship between **Students** and **Courses**?

2. **Instructors and Courses**  
   Instructors can teach multiple courses, and each course can have multiple instructors. How will you model this relationship between **Instructors** and **Courses**?

3. **Courses and Semesters**  
   Each course is offered in different semesters, and students can enroll in different semesters. Design a schema that links **Courses** with **Semesters** and manages enrollments accordingly.

---

### **Scenario 3: Hospital Management System**

**Overview:**  
Design a database for a hospital that manages patients, doctors, treatments, and appointments. Doctors treat multiple patients, and patients receive care from multiple doctors.

**Questions:**

1. **Patients and Doctors**  
   A patient can be treated by multiple doctors, and a doctor can treat multiple patients. How will you represent this many-to-many relationship between **Patients** and **Doctors**?

2. **Appointments**  
   Each appointment can involve a patient and one or more doctors. How will you create the database schema to handle this scenario? Ensure you track the date, time, and type of appointment.

3. **Medical Treatments**  
   Patients can receive multiple treatments, and doctors can prescribe multiple treatments to various patients. Design a schema to manage **Treatments** given to patients and prescribed by doctors.

---

### **Scenario 4: Gym Membership Management System**

**Overview:**  
A gym needs a system to manage members, fitness classes, and trainers. Members can enroll in multiple classes, and each class can be led by different trainers. The gym also needs to track equipment usage in these classes.

**Questions:**

1. **Members and Classes**  
   Members can sign up for multiple classes, and each class can have multiple members. How will you handle the many-to-many relationship between **Members** and **Classes** in your ERD?

2. **Trainers and Classes**  
   Trainers can lead multiple classes, and a class can be led by multiple trainers. Design the schema to track which **Trainers** are assigned to each **Class**.

3. **Equipment and Classes**  
   Classes often use different gym equipment. Design a schema to track the **Equipment** used in each class and the duration of its usage.

---

For each scenario, the contestants must design a **comprehensive ERD** that handles all the relationships between the entities and then provide a **database schema** outlining the tables and their relationships. 
