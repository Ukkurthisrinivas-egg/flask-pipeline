from app import app

def test_home():
    # Create a test client
    client = app.test_client()
    response = client.get("/")
    
    # Assertions
    assert response.status_code == 200
    assert b"Hello, CI/CD Pipeline!" in response.data

