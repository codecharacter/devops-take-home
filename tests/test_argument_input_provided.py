"""tests if required parameter input provided"""

from subprocess import getstatusoutput

prg = "./ip-checker.py"


def test_no_argument_input_provided():
    """program parameter no input provided"""

    arg = ""
    exitcode, output = getstatusoutput(f"{prg} {arg}")
    assert exitcode != 0


def test_one_argument_input_provided():
    """program parameter with one input provided"""

    arg = "2.56.8.1"
    exitcode, output = getstatusoutput(f"{prg} {arg}")
    assert exitcode == 0


def test_multi_argument_inputs_provided():
    """program parameter with multiple inputs provided"""

    arg1 = "2.56.8.1"
    arg2 = "172.25.3.100"
    exitcode, output = getstatusoutput(f"{prg} {arg1} {arg2}")
    assert exitcode != 0
