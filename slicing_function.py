def slice_sequence(sequence, start=None, end=None, step=None):
    """
    Slices a sequence (like a list or string) based on the provided start, end, and step values.

    Parameters:
    - sequence: The sequence to be sliced (list, string, etc.).
    - start: The starting index of the slice (inclusive). Defaults to None (start from the beginning).
    - end: The ending index of the slice (exclusive). Defaults to None (go until the end).
    - step: The step size for slicing. Defaults to None (step of 1).

    Returns:
    - A new sliced sequence based on the provided parameters.
    """
    sliced = sequence[start:end:step]
    return  f'''Original sequence: {sequence} ({id(sequence)})\nSliced sequence: {sliced} ({id(sliced)})'''

def slice_sequence2(sequence, start:int | None = None, end:int | None = None, step:int | None = None):
    """
    Slices a sequence (like a list or string) based on the provided start, end, and step values.

    Parameters:
    - sequence: The sequence to be sliced (list, string, etc.).
    - start: The starting index of the slice (inclusive). Defaults to None (start from the beginning).
    - end: The ending index of the slice (exclusive). Defaults to None (go until the end).
    - step: The step size for slicing. Defaults to None (step of 1).

    Returns:
    - A new sliced sequence based on the provided parameters.
    """
    sliced = sequence[start:end:step]
    return  (sequence,id(sequence)),(sliced,id(sliced))
