import sys
sys.path.append("/home/e78368jw/Documents/OCTOPUS/")

from src.example_code import main


def test_example_returns_ten():
    assert main() == 10