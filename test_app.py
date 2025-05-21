from app import app  # import the Flask app

def test_home_route():
    tester = app.test_client()  # Flask's built-in test client
    response = tester.get('/')  # Simulate GET request to "/"
    
    assert response.status_code == 200  # Check if the route is reachable
    assert response.data == b"Hello from Docker!"  # Check if response matches