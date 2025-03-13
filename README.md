# Job Tracker API

The **Job Tracker API** helps users **track job applications**, store relevant job details, and update their application statuses.

## **1️⃣ Tech Stack**
- **Backend Framework:** FastAPI (lightweight and optimized for APIs)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (using PyJWT)
- **Documentation:** Swagger/OpenAPI (built-in with FastAPI)
- **Version Control:** GitHub

## **2️⃣ Features & Endpoints**
The API provides the following core functionalities:

### **🔹 User Authentication**
- `POST /register` → Register a new user
- `POST /login` → Authenticate user and return a JWT token

### **🔹 Job Applications**
- `POST /jobs/` → **Create** a new job application
- `GET /jobs/` → **Retrieve** all job applications (for the logged-in user)
- `GET /jobs/{id}` → **Retrieve** a specific job application (only if owned by the user)
- `PUT /jobs/{id}` → **Update** job application details
- `DELETE /jobs/{id}` → **Delete** a job application

## **3️⃣ API Documentation**
- **Swagger UI:** Available at `http://127.0.0.1:8000/docs`
- **ReDoc:** Available at `http://127.0.0.1:8000/redoc`

## **4️⃣ How to Run Locally**
### **🔹 Prerequisites**
- Python 3.10+
- PostgreSQL installed and running
- Virtual environment (`venv`)

### **🔹 Setup Instructions**
```bash
# Clone the repository
git clone https://github.com/your-username/job_tracker_api.git
cd job_tracker_api

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --reload
