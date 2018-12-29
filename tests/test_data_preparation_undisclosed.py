import sys
sys.path.insert(0, './answers')
from answer import data_preparation

def test_data_preparation():
    a = data_preparation("./data/plants.data", "agnorhiza", "nc")
    assert(a == False)
    a = data_preparation("./data/plants.data", "carex globosa", "ca")
    assert(a)
    a = data_preparation("./data/plants.data", "lawsonia", "qc")
    assert(a == False)
