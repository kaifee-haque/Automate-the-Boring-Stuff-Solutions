#! python3
"""Determines whether a given password is strong or weak."""

import re
import sys

def is_strong_password(password):
    """Determines whether a string is a strong password or a weak password.

    Args:
        password: The string to be tested for password strength.

    Returns:
        A boolean value indicating whether the password is strong or weak.
    """
    
    char_length = re.compile(r"\w{8,}")
    upper = re.compile(r"[A-Z]")
    lower = re.compile(r"[a-z]")
    digit = re.compile(r"[0-9]")
    
    if char_length.search(password) == None:
        return False
    if upper.search(password) == None:
        return False
    if lower.search(password) == None:
        return False
    if digit.search(password) == None:
        return False
    else:
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python strong_password_detection <password>")
        sys.exit()
    if is_strong_password(sys.argv[1]):
        print("Password is strong.")
    else:
        print("Password is weak.")
