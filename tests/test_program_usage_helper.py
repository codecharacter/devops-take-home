"""Tests if program usage helper present indicating required parameter input"""

from subprocess import getstatusoutput

prg = "./ip-checker.py"


def test_program_usage_helper():
    """Program usage helper for parameter"""

    for flag in ["-h", "--help"]:
        exitcode, output = getstatusoutput(f"{prg} {flag}")
        assert exitcode == 0
        assert output.lower().startswith("usage:")
