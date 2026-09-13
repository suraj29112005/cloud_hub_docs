from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth, incidents
Base.metadata.create_all(bind=engine)
app = FastAPI(title="CloudTrace Incident Hub API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(auth.router)
app.include_router(incidents.router)
@app.get("/health")
def health(): return {"status": "healthy"}
