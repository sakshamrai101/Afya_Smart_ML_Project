import pytest
from openai import OpenAI
import sys
import os

# Add the parent directory of the app package to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you should be able to import ranking2
print(sys.path)
from app import userstory3
# print()
# Define a fixture to initialize the OpenAI client
@pytest.fixture
def openai_client():
    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    client = OpenAI(api_key='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')
    print(client)
    yield client

# Define a test function to test the get_recommendations function
def test_get_recommendations(openai_client):
    # Define user input and guidelines text
    user_input = """
    Patient Name: John Smith
    Date of Visit: 03/25/2023
    Chief Complaint: Shortness of breath and cough
    ...
    """
    guidelines_text = """
    COMMUNITY FIRST HEALTH PLANS PCP MEDICAL RECORD DOCUMENTATION AND CONTINUITY GUIDELINES
    ...
    """

    # Call the get_recommendations function and check if it returns recommendations
    recommendations =userstory3.get_recommendations(user_input, guidelines_text)
    # Assert that recommendations are not empty
    assert recommendations.strip() != ''

# # Add more test functions as needed for other functionalities or edge cases
