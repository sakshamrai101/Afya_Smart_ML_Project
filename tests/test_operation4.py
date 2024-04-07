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

def test_operation4_page(client):
    response = client.get('/operation4')
    assert response.status_code == 200
    assert b'Operations Page' in response.data

def test_operation4_buttons(client):
    response = client.get('/operation4')
    print(response)
    assert b'Display missing information' in response.data
    assert b'Display targeted questions' in response.data
    assert b'Display recommendations' in response.data
    assert b'Go to Dashboard' in response.data
    
    assert b'id="button1" disabled' in response.data
    assert b'id="button2" disabled' in response.data
    assert b'id="button3" disabled' in response.data

# Add more tests as needed to validate specific functionality or elements on the page
