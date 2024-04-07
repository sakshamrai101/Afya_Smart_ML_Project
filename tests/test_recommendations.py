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

def test_recommendations_page(client):
    response = client.post('/Recommendations')
    assert response.status_code == 200
    assert b'Validated Recommendations' in response.data
    assert b'Clinical review of recommendations' in response.data
    assert b'Helpfulness:' in response.data
    assert b'doneButton' in response.data
    # Add more assertions as needed to validate the content of the rendered recommendations.html page

def test_recommendations_content(client):
    response = client.post('/Recommendations')
    assert b'Recommendations' in response.data
    # Add assertions to check if recommendations are present in the response data

# Add more tests as needed to cover different aspects of the /Recommendations route
def test_feedback_form_submission(client):
    # Simulate submitting feedback form
    response = client.post('/Recommendations', data={'criteria1': 'value1', 'criteria2': 'value2', 'criteria3': 'value3', 'criteria4': 'value4', 'criteria5': 'value5', 'feedback': 'Additional feedback'})
    assert response.status_code == 200  # Assuming successful submission returns HTTP status code 200
    # Add assertions for the expected behavior after form submission, such as redirect or success message