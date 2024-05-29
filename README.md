

Flask Application for Student Records
This Flask application provides a simple API to manage student records, programs, blocks, and years. The API includes endpoints for creating, reading, updating, and deleting records, with basic authentication implemented to secure the routes.

Features
Basic Authentication: Secure access to endpoints with a username and password.
Data Retrieval: Fetch records in JSON or XML format.
CRUD Operations: Create, read, update, and delete student records.
Join Operations: Retrieve related records through joins between different tables.

Endpoints
Authentication
/protected (GET): Access a protected resource to confirm authentication.
Records Retrieval
/block_record (GET): Retrieve all block records.
/program_record (GET): Retrieve all program records.
/year_record (GET): Retrieve all year records.
/student_block (GET): Retrieve all student block records.
/student_program (GET): Retrieve all student program records.
/student_year (GET): Retrieve all student year records.
/student_record (GET): Retrieve all student records.
/student_record/int:student_id (GET): Retrieve a specific student record by ID.
/student_program/int:student_id (GET): Retrieve programs for a specific student.
/student_block/int:student_id (GET): Retrieve blocks for a specific student.
/student_year/int:student_id (GET): Retrieve years for a specific student.
/year_students/int:year_id (GET): Retrieve students under a specific year.
CRUD Operations
/student_record (POST): Add a new student record.
/student_record/int:id (PUT): Update an existing student record.
/student_record/int:id (DELETE): Delete a student record.

Usage
Access endpoints using an HTTP client (e.g., Postman, curl) with the following credentials:
Username: rena
Password: 1892

Security
The application uses HTTP Basic Authentication to protect the routes. Replace the authentication logic with your actual user authentication mechanism as needed.
