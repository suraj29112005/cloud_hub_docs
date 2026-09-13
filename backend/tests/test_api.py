import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_register_and_login():
    reg_res = client.post('/api/v1/auth/register', json={
        'email': 'lead.sre@cloudtrace.internal',
        'password': 'SecurePassword123!',
        'full_name': 'S. Bhadola'
    })
    assert reg_res.status_code == 201
    assert reg_res.json()['email'] == 'lead.sre@cloudtrace.internal'

    login_res = client.post('/api/v1/auth/token', data={
        'username': 'lead.sre@cloudtrace.internal',
        'password': 'SecurePassword123!'
    })
    assert login_res.status_code == 200
    assert 'access_token' in login_res.json()

def test_unauthorized_incident_creation():
    res = client.post('/api/v1/incidents', json={
        'title': 'PostgreSQL Standby Lag',
        'severity': 'P1',
        'service_name': 'db-primary'
    })
    assert res.status_code == 401
