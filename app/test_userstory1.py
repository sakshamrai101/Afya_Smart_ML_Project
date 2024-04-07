from .userstory1 import get_missing_info, format_missing_info

def test_get_missing_info_returns_list():
    # Test if get_missing_info returns a list
    user_input = "..."
    guidelines_text = "..."
    result = get_missing_info(user_input, guidelines_text)
    print(type(result))  # Add this line to see the actual value returned
    assert isinstance(result, str)

def test_format_missing_info_returns_list():
    # Test if format_missing_info returns a list
    missing_info = "..."
    result = format_missing_info(missing_info)
    assert isinstance(result, list)