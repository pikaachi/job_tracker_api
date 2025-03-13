# job_tracker_api
This API will help users track job applications, store relevant job details, and update the status of their applications.
1. Tech Stack:
•	Backend Framework: FastAPI (lightweight and great for API design)
•	Database: PostgreSQL
•	ORM: SQLAlchemy
•	Authentication: JWT (using pyjwt)
•	Documentation: Swagger/OpenAPI (built-in with FastAPI)
•	Version Control: GitHub
 
2. Feature Definition
The API will have the following core endpoints:
•	User Authentication
1.	POST /register → Register a user
2.	POST /login → Authenticate user and return JWT token
•	Job Applications
1.	POST /jobs/ → Add a new job application
2.	GET /jobs/ → Get all job applications
3.	GET /jobs/{id} → Get a specific job application
4.	PUT /jobs/{id} → Update job application details
<img width="468" alt="image" src="https://github.com/user-attachments/assets/b25dd6dc-2e68-4ff2-a92c-7f7c443e834d" />
