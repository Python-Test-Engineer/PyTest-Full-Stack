import warnings


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


def new_function():
    print("This is the new function.")


old_function()
