import warnings
import pytest


def old_function():
    warnings.warn(
        "old_function() is deprecated; use new_function() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    warnings.warn(
        "The syntax will be removed in version 2.0.0.",
        SyntaxWarning,
        stacklevel=2,
    )


def test_703_myfunction_deprecated():
    with pytest.deprecated_call():
        old_function()
