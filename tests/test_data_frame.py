import os

from answers.answer import data_frame


def test_data_frame():
    a = data_frame(os.path.join(".", "data", "plants.data"), 11)
    assert a == open(os.path.join(".", "tests", "data_frame.txt"), "r").read()

    # assert(a==open("tests/data_frame.txt","r").read())
