"""docstring"""

import pytest
from .sample import validate_age


def test_1096_validate_age_valid_age() -> ValueError:
    """docstring"""
    validate_age(10)


def test_1097_validate_age_invalid_age() -> ValueError:
    """docstring"""
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)
