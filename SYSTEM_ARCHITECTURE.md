# CloudTrace Incident Hub - System Architecture & Planning

## 1. Project Brief
CloudTrace Hub is an enterprise full-stack incident response and cloud observability platform designed to track microservice health alerts, database latency spikes, and system outages in real time.

## 2. Core Functional Requirements
- **Authentication**: Secure OAuth2 JWT bearer token issuance and password hashing via Passlib/Bcrypt.
- **Incident Management**: Complete CRUD operations for incident lifecycle (Open, Investigating, Resolved).
- **Filtering & Querying**: Filter incidents by severity (Critical, High, Medium, Low).
- **User Interface**: Three interconnected views (Landing Page, Operational Dashboard, Incident Detail View).

## 3. Technical Architecture
- **Front-End Layer**: React 18, TypeScript, responsive modular component structure (Navbar, Dashboard, DetailView).
- **Back-End Layer**: FastAPI RESTful API, Pydantic data validation schemas, SQLAlchemy ORM engine.
- **Data Storage Layer**: Relational database schema with primary keys, indexes, foreign key references, and timestamps.

## 4. Database Schema (ER Model)
- **User Model**: id (PK), email (Unique, Indexed), hashed_password (String), is_active (Boolean).
- **Incident Model**: id (PK), title (String), severity (Enum), status (Enum), service (String), description (Text), created_at (DateTime), updated_at (DateTime).
