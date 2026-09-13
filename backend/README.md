# CloudTrace Incident Hub - Back-End RESTful API

## Overview
High-performance RESTful API service engineered using Python FastAPI, SQLAlchemy ORM, and PostgreSQL/SQLite.

## API Capabilities
- **OAuth2 & JWT Bearer Authentication:** Stateless user sessions and role mapping.
- **Incident Management:** Full CRUD lifecycle (Triggered -> Acknowledged -> Resolved).
- **Triage Timeline:** Synchronized event logs and responder notes.
- **Interactive API Docs:** Auto-generated Swagger UI at `/docs` and ReDoc at `/redoc`.

## Setup & Execution Instructions
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Run Test Suite
```bash
pytest -v
```
