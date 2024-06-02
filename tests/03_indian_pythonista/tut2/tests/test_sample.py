"""docstring"""

import pytest
from tut2.myapp.sample import validate_age


def test_0096_validate_age_valid_age() -> ValueError:
    """docstring"""
    validate_age(10)


def test_0097_validate_age_invalid_age() -> ValueError:
    """docstring"""
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)
