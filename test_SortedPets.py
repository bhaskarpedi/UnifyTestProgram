from sortedlibrary import *

def test_sort():
    test_array = [5,4,3,2,1]
    sorted_test_array = [1,2,3,4,5]
    assert(sort(test_array) == sorted_test_array)