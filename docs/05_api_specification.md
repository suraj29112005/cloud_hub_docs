# API Specification Catalog

## REST and WebSocket Endpoints

| Method | Endpoint | Authentication | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/v1/auth/login` | Public | Validates credentials and returns JWT bearer tokens. |
| `POST` | `/api/v1/webhooks/alerts` | API Key | Ingests external monitoring alerts into the queue. |
| `GET` | `/api/v1/incidents` | Bearer JWT | Retrieves paginated, filterable incident records. |
| `GET` | `/api/v1/incidents/{id}` | Bearer JWT | Retrieves full incident context and timeline. |
| `PATCH` | `/api/v1/incidents/{id}/state` | Responder+ | Updates incident state (acknowledged, resolved). |
| `POST` | `/api/v1/incidents/{id}/notes` | Responder+ | Adds an investigation note to the War Room timeline. |
| `WSS` | `/ws/v1/incidents/{id}` | Bearer JWT | Real-time WebSocket connection for synchronized collaboration. |
