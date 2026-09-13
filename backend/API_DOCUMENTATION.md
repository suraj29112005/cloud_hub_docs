# CloudTrace Incident Hub - REST API Documentation

## Base URL: http://localhost:8000

## 1. Authentication Endpoints
### POST /auth/register
- **Description**: Register a new platform administrator or operator.
- **Request Body**:
  ```json
  { "email": "admin@cloudtrace.internal", "password": "SecurePassword123" }
  ```
- **Response 201 Created**:
  ```json
  { "id": 1, "email": "admin@cloudtrace.internal", "is_active": true }
  ```

### POST /auth/token
- **Description**: Authenticate user and obtain OAuth2 JWT bearer token.
- **Content-Type**: application/x-www-form-urlencoded
- **Parameters**: username, password
- **Response 200 OK**:
  ```json
  { "access_token": "eyJhbGciOi...", "token_type": "bearer" }
  ```

## 2. Incident CRUD Endpoints
### GET /incidents
- **Description**: Retrieve list of incidents with optional severity filtering.
- **Headers**: Authorization: Bearer <token>
- **Query Params**: severity (optional: Critical, High, Medium, Low)
- **Response 200 OK**: Array of incident objects.

### POST /incidents
- **Description**: Create a new operational incident alert.
- **Headers**: Authorization: Bearer <token>
- **Request Body**:
  ```json
  { "title": "Database pool exhausted", "severity": "Critical", "service": "PostgreSQL-Cluster", "description": "High latency" }
  ```
- **Response 201 Created**: Created incident record.

### PUT /incidents/{id}
- **Description**: Update incident status or resolution notes.
- **Response 200 OK**: Updated incident details.

### DELETE /incidents/{id}
- **Description**: Remove or archive an incident record.
- **Response 204 No Content**
