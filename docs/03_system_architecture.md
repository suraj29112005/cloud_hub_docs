# Technical Architecture & Rationale

## Tier Breakdown
1. **Client Tier:** React 19, TypeScript, Tailwind CSS, Zustand state management.
2. **Gateway Tier:** Nginx reverse proxy providing TLS 1.3 termination and rate limiting.
3. **Application Tier:** Python FastAPI REST and WebSocket services with Celery asynchronous task workers.
4. **Data Store Tier:** PostgreSQL 16 for ACID relational persistence and JSONB telemetry storage.
5. **Caching & Messaging Tier:** Redis 7 for sliding-window deduplication and Pub/Sub WebSocket event fan-out.

## Architectural Trade-Offs
- **Modular Monolith over Microservices:** Avoids network serialization latency and distributed transaction overhead while maintaining clean package separation.
- **WebSockets over SSE:** Enables full-duplex communication required for collaborative typing indicators, lock acquisition, and live notes.
- **PostgreSQL + Redis Hybrid:** Combines ACID relational reliability for compliance audits with in-memory throughput for volatile deduplication checks.
