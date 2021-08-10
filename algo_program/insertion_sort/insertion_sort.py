import pytest

# insertion sort implementation
def insertion_sort(list):
    if len(list)<=1:
        return
    else:
        for j in range(1, len(list)):
            key=list[j]
            i=j-1
            while i>=0 and list[i] > key:
                list[i+1]=list[i]
                i=i-1
                list[i+1]=key

# tests a list that includes only one element
def test_base():
    a_list=[1]
    insertion_sort(a_list)
    assert a_list==[1]

# tests the best case, in which the list is already sorted
def test_best():
    a_list=[1,2,3,4,5]
    insertion_sort(a_list)
    assert a_list==[1,2,3,4,5]

# tests the worst case, in which all elements in the list are completely in reversed order
def test_worst():
    a_list=[5,4,3,2,1]
    insertion_sort(a_list)
    assert a_list==[1,2,3,4,5]

# tests a list includes same elements
def test_same_list():
    a_list=[1,1,1,1,1,1]
    insertion_sort(a_list)
    assert a_list==[1,1,1,1,1,1]

# tests a list, in which some elements are in right position, but some are not
def test_average_list():
    a_list=[1,1,5,3,6,2]
    insertion_sort(a_list)
    assert a_list==[1,1,2,3,5,6]

