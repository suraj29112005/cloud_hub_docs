# CloudTrace Incident Hub - Production Deployment Guide

## 1. Production Configuration
Set the following in backend/.env:
ENVIRONMENT=production
PORT=8000
SECRET_KEY=e83a9f01c34a2e6f9821d3e8b0a39f1c7d24e81a9f01c34a2e6f9821d3e8b0a3
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./incident_hub.db
ALLOWED_ORIGINS=https://cloudtrace-hub.vercel.app

## 2. Public Platform Deployment
- Backend: Render Web Service pointing to backend folder. Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
- Frontend: Vercel Static deployment pointing to frontend folder. Environment variable: VITE_API_BASE_URL

## 3. Common Troubleshooting
- Bcrypt 72-byte limit: Pin bcrypt==4.0.1 in requirements.txt.
- Missing dependencies: Ensure email-validator is installed for Pydantic V2.
- CORS: Verify allowed origins match the production domain.
