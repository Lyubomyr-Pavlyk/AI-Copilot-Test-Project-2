from app import app, db
import json

def test_get_destinations():
    # Create a test client
    client = app.test_client()

   
    with app.app_context():
        db.drop_all()
        db.create_all()

    # Test GET request to /destinations
    response = client.get('/destinations')
    assert response.status_code == 200  
    data = json.loads(response.data)
    assert len(data) == 0  

    # Test POST request to create a destination
    destination_data = {
        "name": "Paris",
        "description": "The City of Love",
        "location": "France"
    }
    response = client.post('/destinations', json=destination_data)
    assert response.status_code == 200  

    # Test GET request to /destinations again
    response = client.get('/destinations')
    assert response.status_code == 200  
    data = json.loads(response.data)
    assert len(data) == 1  

if __name__ == '__main__':
    test_get_destinations()
