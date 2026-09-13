from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, incidents

app = FastAPI(title="CloudTrace Incident Hub")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers under /api/v1
app.include_router(auth.router, prefix="/api/v1")
app.include_router(incidents.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "CloudTrace Hub API"}
