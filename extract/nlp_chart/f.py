"""Generic dummy file to pass reference for  the coding standards."""


def add_two_number(x: int, y: int) -> int:
    """Add two whole  number.
    
    Parameters
    ----------
    x : int
        any whole number between 0 to 2147483647
    y : int
        any whole number between 0 to 2147483647

    Returns
    -------
    int
        added result of two whole number.

    Raises
    ------
    ValueError
        Number out of bound exception.
    """
    result = x + y
    if result > 2147483647:
        raise ValueError(
            "Number out of bound , The result is out of the range of the python int data type.For resolution please checkout python bigint , PLease have a look on few implemention here https://www.codementor.io/@arpitbhayani/how-python-implements-super-long-integers-12icwon5vk"
        )
    return x + y
    