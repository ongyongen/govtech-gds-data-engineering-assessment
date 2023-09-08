"""
Pytest Template Code
"""

def increment(number):
    """
    Function that increases number by 1
    """
    return number + 1


def test_answer():
    """
    Check that number has increased by 1
    """
    assert increment(3) == 4
