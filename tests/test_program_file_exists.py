"""tests if ip-checker.py program file exists"""

import os

prg = "./ip-checker.py"


def test_program_file_exists():
    """test if program file exists"""

    assert os.path.isfile(prg)
