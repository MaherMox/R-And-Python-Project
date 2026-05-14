🚀 Task Management System

A full-stack Task Management System built using FastAPI with authentication, role-based authorization, Redis caching, monitoring, Docker support, and automated API testing.

📖 Overview

This system is designed to manage:

👤 Users
📁 Projects
📝 Tasks

The system supports secure authentication, task workflow validation, monitoring, caching, and role-based permissions.

✨ Features
🔐 JWT Authentication
🛡️ Role-Based Authorization
⚡ Redis Caching
📊 Monitoring Dashboard
🧾 Logging System
🧪 API Testing with Pytest
🖥️ Frontend Interface
🐳 Docker Support
🧑‍💻 Roles
Role	Permissions
👑 Admin	Full access to manage users, projects, and tasks
🧠 Project Manager	Create, update, assign, and monitor projects/tasks
👨‍💼 Employee	Update assigned tasks only
⚙️ Features Details
📁 Project Management
Create Projects
Update Projects
Delete Projects
View Projects
📝 Task Management
Create Tasks
Update Tasks
Delete Tasks
Assign Tasks to Users
🔄 Task Workflow Validation

Allowed task status transitions:

To Do → In Progress → Done

Invalid transitions are automatically rejected.

🔍 Task Filtering

Tasks can be filtered by:

status
priority
assignee_id

Example:

/tasks/?status=To Do&priority=high&assignee_id=1
🔐 Authentication
Features
User Registration
User Login
JWT Token Generation
Protected Endpoints
Token Validation
Notes
created_by is automatically extracted from the logged-in JWT user.
Employees can only update tasks assigned to them.
⚡ Redis Caching
Cache Strategy

The project uses the Cache-Aside Pattern:

Check cache first
If cache miss → fetch from database
Save result in cache
Return response
Cached Endpoints
GET all projects/tasks
GET project/task by ID
Filtered task queries
Cache Invalidation

Cache is automatically cleared after:

➕ Create
✏️ Update
❌ Delete
📊 Monitoring Dashboard
Endpoints
Method	Endpoint
GET	/monitoring
DELETE	/monitoring/reset
GET	/health
Monitoring Includes
📊 Total API requests
⏱️ Average response time
❌ Error count
📥 Recent requests
🚨 Recent errors
💚 System health status
🧪 API Testing

The project uses Pytest for automated API testing.

Run Tests
pytest
Test Coverage
🔐 Authentication
🛡️ Authorization
🔁 CRUD operations
🔄 Task workflow validation
🔍 Filters
❗ Error handling
⚡ Cache behavior
🖥️ Frontend
Features
🔐 Login / Register
📊 Dashboard
📁 Manage Projects
📝 Manage Tasks
🔄 Update Task Status
🔍 Filter Tasks
📊 Monitoring Dashboard
Run Frontend

Open:

frontend/index.html
🐳 Docker
Run Project
docker compose up --build
Stop Project
docker compose down
Run Tests Inside Docker
docker compose exec app pytest
🌐 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs
💻 Local Setup
Create Virtual Environment
python -m venv .venv
Activate Environment (Windows)
.venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Start Redis
redis-server
Run Server
uvicorn app.main:app --reload
📁 Project Structure
app/
├── core/
├── models/
├── routes/
├── schemas/
├── services/
├── database.py
├── dependencies.py
└── main.py

tests/
frontend/

docker-compose.yml
requirements.txt
README.md
🛠️ Technologies Used
FastAPI
SQLAlchemy
SQLite
Redis
JWT
Pytest
Docker
HTML / CSS / JavaScript
✅ Security Notes
JWT-based authentication is required for protected routes.
Role-based authorization is enforced.
Cache authorization validation is implemented.
Employees cannot access unauthorized tasks/projects.

👥 Team Members
mahmoud shaker 1
mahmoud tarek 2
mohamed maher 3
Member 4
Member 5
✅ Final Notes
The system enforces valid task lifecycle transitions.
Redis improves API performance.
Monitoring tracks system behavior and API health.
The project is fully containerized using Docker.
Automated tests validate core functionality.