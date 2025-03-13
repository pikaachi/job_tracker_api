# job_tracker_api
This API will help users track job applications, store relevant job details, and update the status of their applications.
Tech Stack:
•	Backend Framework: FastAPI (lightweight and great for API design)
•	Database: PostgreSQL
•	ORM: SQLAlchemy
•	Authentication: JWT (using pyjwt)
•	Documentation: Swagger/OpenAPI (built-in with FastAPI)
•	Deployment: Docker (optional), Render/Heroku/VPS
•	Version Control: GitHub
 
1. Define Features
The API will have the following core endpoints:
•	User Authentication
o	POST /register → Register a user
o	POST /login → Authenticate user and return JWT token
•	Job Applications
o	POST /jobs/ → Add a new job application
o	GET /jobs/ → Get all job applications
o	GET /jobs/{id} → Get a specific job application
o	PUT /jobs/{id} → Update job application details
<img width="468" alt="image" src="https://github.com/user-attachments/assets/b25dd6dc-2e68-4ff2-a92c-7f7c443e834d" />
