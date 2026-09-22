from app import app, db
import json

def test_get_itineraries():
    # Create a test client
    client = app.test_client()

    # Ensure the database is in a clean state
    with app.app_context():
        db.drop_all()
        db.create_all()

    # Test GET request to /itineraries
    response = client.get('/itineraries')
    assert response.status_code == 200  
    data = json.loads(response.data)
    assert len(data) == 0  

    # Test POST request to create an itinerary
    itinerary_data = {
        "destination_id": 1,
        "activity": "Visit Eiffel Tower"
    }
    response = client.post('/itineraries', json=itinerary_data)
    assert response.status_code == 200  

    # Test GET request to /itineraries again
    response = client.get('/itineraries')
    assert response.status_code == 200  
    data = json.loads(response.data)
    assert len(data) == 1  

if __name__ == '__main__':
    test_get_itineraries()
