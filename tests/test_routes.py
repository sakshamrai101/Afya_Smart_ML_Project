import pytest
from flask import session
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_view_boneFracture_file(client):
    response = client.get('/view_boneFracture_file')
    print(response.status_code, response.headers)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'

def test_view_oralSurgery_file(client):
    response = client.get('/view_oralSurgery_file')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'

def test_view_pneumonia_file(client):
    response = client.get('/view_pneumonia_file')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/plain; charset=utf-8'

# Add more tests for other routes as needed
