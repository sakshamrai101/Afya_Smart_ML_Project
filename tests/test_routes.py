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


# Test the index route
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'PCP Login' in response.data

# Test the login route with valid credentials
def test_login_valid(client):
    response = client.post('/PCP_login', data={'username': 'valid_user', 'password': 'valid_password'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Import Page' in response.data

# Test the login route with invalid credentials
def test_login_invalid(client):
    response = client.post('/PCP_login', data={'username': 'invalid_user', 'password': 'invalid_password'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

# Test the logout route
def test_logout(client):
    with client:
        client.post('/PCP_login', data={'username': 'valid_user', 'password': 'valid_password'})
        response = client.get('/logout', follow_redirects=True)
        assert b'PCP Login' in response.data

# Test other routes and functionalities as needed, such as:
# - Route to view files
# - Route to display operation pages
# - Route to handle operations like missing_info, targeted_questions, recommendations, etc.

# Example test for viewing a file

# Example test for operation page
def test_operation3(client):
    with client:
        client.post('/PCP_login', data={'username': 'valid_user', 'password': 'valid_password'})
        response = client.get('/operation3')
        assert response.status_code == 200
        assert b'Operations Page' in response.data

