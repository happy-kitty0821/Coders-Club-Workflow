---

### Real-World Database Design Questions (6-9 tables each):
#### 1. **E-Commerce System**
**Scenario:** You are tasked with designing a database for an e-commerce platform that sells products online. The platform needs to track customers, orders, payments, and the inventory of products.

- **Tables:** 
   1. `Customers (customer_id, name, email, address, phone)`
   2. `Orders (order_id, order_date, customer_id, total_amount)`
   3. `OrderItems (order_item_id, order_id, product_id, quantity, price)`
   4. `Products (product_id, product_name, product_description, price, stock_quantity)`
   5. `Categories (category_id, category_name)`
   6. `Payments (payment_id, order_id, payment_date, payment_method, payment_status)`
   7. `Shippers (shipper_id, shipper_name, shipping_date, shipping_cost)`
   8. `Suppliers (supplier_id, supplier_name, contact_name, phone)`
   9. `ProductSuppliers (product_id, supplier_id, supply_date, quantity)`

**Question:**
Design the schema for the e-commerce system and write queries to:
- Retrieve all orders along with the total amount and the customer’s details.
- Get the total quantity of products sold by category.
- Identify which products are low in stock (stock quantity < 10).
- Calculate the total revenue generated from each payment method.

---

#### 2. **University Management System**
**Scenario:** Design a database for a university to manage students, courses, faculty, and enrollment details.

- **Tables:** 
   1. `Students (student_id, student_name, email, date_of_birth, address)`
   2. `Courses (course_id, course_name, credits, department_id)`
   3. `Departments (department_id, department_name)`
   4. `Faculty (faculty_id, faculty_name, email, department_id, hire_date)`
   5. `Enrollments (enrollment_id, student_id, course_id, semester, grade)`
   6. `Classrooms (classroom_id, building, room_number, capacity)`
   7. `CourseSchedules (schedule_id, course_id, faculty_id, classroom_id, semester, start_time, end_time)`
   8. `Assignments (assignment_id, course_id, assignment_description, due_date)`
   9. `StudentAssignments (student_id, assignment_id, submission_date, grade)`

**Question:**
Design the schema for the university system and write queries to:
- Retrieve a list of students enrolled in a specific course for a given semester.
- List all faculty members and the courses they are teaching in the current semester.
- Get the classroom schedule for a specific course and faculty.
- Identify students who have not submitted a particular assignment by the due date.

---

#### 3. **Hospital Management System**
**Scenario:** Design a database for a hospital to manage patients, doctors, treatments, and appointments.

- **Tables:** 
   1. `Patients (patient_id, patient_name, date_of_birth, contact_info, address)`
   2. `Doctors (doctor_id, doctor_name, specialization, contact_info)`
   3. `Appointments (appointment_id, patient_id, doctor_id, appointment_date, status)`
   4. `Treatments (treatment_id, treatment_name, treatment_type, cost)`
   5. `Prescriptions (prescription_id, patient_id, doctor_id, treatment_id, dosage, start_date, end_date)`
   6. `Bills (bill_id, appointment_id, total_amount, payment_status, billing_date)`
   7. `Departments (department_id, department_name, department_head)`
   8. `Rooms (room_id, room_type, room_number, cost_per_day)`
   9. `Admissions (admission_id, patient_id, room_id, admission_date, discharge_date)`

**Question:**
Design the schema for the hospital system and write queries to:
- Retrieve a list of all appointments for a specific doctor on a given date.
- Get the total cost of treatments for a patient during a hospital admission.
- Find doctors with the most appointments in a given month.
- Generate a bill for a patient's appointment, including treatments and prescriptions.

---

#### 4. **Travel Booking System**
**Scenario:** You are tasked with designing a database for a travel booking platform where users can book flights, hotels, and car rentals.

- **Tables:** 
   1. `Users (user_id, user_name, email, contact_info)`
   2. `Flights (flight_id, airline, departure_city, destination_city, departure_time, arrival_time, cost)`
   3. `Bookings (booking_id, user_id, booking_date, total_amount)`
   4. `FlightBookings (flight_booking_id, booking_id, flight_id, seat_number)`
   5. `Hotels (hotel_id, hotel_name, city, room_type, cost_per_night)`
   6. `HotelBookings (hotel_booking_id, booking_id, hotel_id, check_in_date, check_out_date, room_number)`
   7. `Cars (car_id, car_model, car_type, cost_per_day)`
   8. `CarRentals (rental_id, booking_id, car_id, rental_start_date, rental_end_date)`
   9. `Payments (payment_id, booking_id, payment_method, payment_date, payment_status)`

**Question:**
Design the schema for the travel booking system and write queries to:
- Retrieve all flights booked by a user along with the corresponding hotel and car rental information.
- Get the total number of hotel nights booked by users in a particular city.
- Identify the most popular flight routes based on the number of bookings.
- Calculate the total amount spent by a user across all their bookings.

---
