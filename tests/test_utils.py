"""
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utils import user_query_input


def test_user_query_input(user_input, expected):
    assert user_query_input(user_input.isalpha()) == expected
"""
"""
def test_user_gpt_input(user_input, expected):
    if user_input in ['yes', 'no']:
        assert user_gpt_input("¿Quieres mejorar el texto?") == expected
    else:
        with pytest.raises(ValueError):
            user_gpt_input("¿Quieres mejorar el texto? (yes/no): ")

"""
