"""Tests if ip-checker.py program file exists"""

import os

prg = "./ip-checker.py"


def test_program_file_exists():
    """Test if program file exists"""

    assert os.path.isfile(prg)
