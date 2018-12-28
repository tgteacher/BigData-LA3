import sys
sys.path.insert(0, './answers')
from answer import data_frame

def test_data_frame_undisclosed():
    a = data_frame("./data/plants.data", 14)
    assert(a==open("tests/data_frame_undisclosed.txt","r").read())
