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

    
def test_login_form(client):
    # Send a POST request with valid login credentials
    response = client.post('/PCP_login', data={'username': 'example', 'password': 'example'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'PCP Login' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data
# Add more tests as needed to validate specific functionality or elements on the page
