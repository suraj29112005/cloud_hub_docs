# CloudTrace Incident Hub - Project Reflection Report

## 1. Architectural Successes
- Complete decoupling of FastAPI backend and React/TypeScript frontend.
- Test isolation using temporary SQLite fixtures in Pytest with drop_all teardown.

## 2. Engineering Challenges
- Resolved passlib/bcrypt incompatibility by pinning bcrypt==4.0.1.
- Addressed Pydantic V2 email validation errors via email-validator.
- Fixed Pytest collection paths using pythonpath = . in pytest.ini.

## 3. Lessons Learned
- Future iterations will use Docker multi-stage builds for uniform local and production runtimes.
- Scaling to PostgreSQL with Alembic migrations for concurrent production writes.
