import pytest
from unittest.mock import patch, MagicMock
from userstory2 import generate_targeted_questions  # Ensure this matches the name of your Python script

# Sample data for testing
econsult_data = "Patient Name: John Smith..."
guidelines_text = "COMMUNITY FIRST HEALTH PLANS PCP MEDICAL RECORD DOCUMENTATION AND CONTINUITY GUIDELINES..."

# Mock response from OpenAI
mock_response = {
    "choices": [
        {
            "message": {
                "content": "1. Is the patient currently taking any medication? 2. What is the patient's medical history?"
            }
        }
    ]
}

# Test function
def test_generate_targeted_questions():
    with patch('userstory2.client.chat.completions.create') as mock_create:
        # Configure the mock to return a predefined response
        mock_create.return_value = mock_response
        
        # Call the function with the mock object and test data
        result = generate_targeted_questions(econsult_data, guidelines_text)
        
        # Assertions to verify the expected behavior
        assert "Is the patient currently taking any medication?" in result
        assert "What is the patient's medical history?" in result
        
        # Verify that the OpenAI API was called once
        mock_create.assert_called_once()
