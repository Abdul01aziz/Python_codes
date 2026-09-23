def is_immutable(obj):
    """
    Check if an object is immutable.
    Parameters:
    obj: The object to check.
    Returns:
    bool: True if the object is immutable, False otherwise.
    """
    try:
        hash(obj)
        return True
    except TypeError:
        return False