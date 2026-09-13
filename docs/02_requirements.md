# Requirements Specification

## Functional Requirements (FR)
- **FR-01:** Responders must authenticate via OAuth2/JWT and retain authenticated sessions.
- **FR-02:** The system must ingest raw JSON alert payloads over an HMAC-authenticated REST endpoint.
- **FR-03:** Alerts sharing the same service and cluster within 10 minutes must aggregate into a single incident.
- **FR-04:** Incident status updates must broadcast to connected clients via WebSockets with sub-250ms latency.
- **FR-05:** Responders must be able to export timeline event logs as post-mortem artifacts.

## Non-Functional Requirements (NFR)
- **Ingestion Latency:** p95 < 100 ms via asynchronous Redis queues.
- **WebSocket Broadcast:** < 250 ms propagation across all active War Room sessions.
- **Availability:** 99.9%% service uptime with stateless application workers.
- **Security:** TLS 1.3 encryption in transit, AES-256 at rest, bcrypt password hashing.
