import sys
sys.path.append("/home/e78368jw/Documents/OCTOPUS/")

from src.example_code import main


def test_example_does_not_return_one():
    assert main() != 1