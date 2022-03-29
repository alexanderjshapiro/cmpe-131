import random

from sort import *


def is_sorted(test_list):
    for i in range(len(test_list) - 1):
        if test_list[i] > test_list[i + 1]:
            return False
    return True


def test_sort_list_does_not_crash():
    sort_list([0, 1, 2])


def test_sort_list_small_list():
    unsorted_lists = [[1, 3, 2, 7], [3, 2, 4, 89]]

    sorted_lists = []
    for unsorted_list in unsorted_lists:
        sorted_lists.append(sort_list(unsorted_list))

    for sorted_list in sorted_lists:
        assert is_sorted(sorted_list)


def test_sort_list_large_list():
    unsorted_list = []
    for n in range(1000):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = sort_list(unsorted_list)

    assert (is_sorted(sorted_list))


def test_sort_list_duplicates():
    unsorted_list = []
    for n in range(100):
        unsorted_list.append(random.randint(0, 1000) % 10)

    sorted_list = sort_list(unsorted_list)

    assert (is_sorted(sorted_list))


def test_sort_list_ordered():
    unsorted_list = []
    for n in range(10):
        unsorted_list.append(n)

    sorted_list = sort_list(unsorted_list)

    assert (is_sorted(sorted_list))


def test_sort_list_reversed():
    unsorted_list = []
    for n in range(9, -1, -1):
        unsorted_list.append(n)

    sorted_list = sort_list(unsorted_list)

    assert (is_sorted(sorted_list))


def test_sort_list_one_element():
    unsorted_lists = [[0], [3], [1000000]]

    sorted_lists = []
    for unsorted_list in unsorted_lists:
        sorted_lists.append(sort_list(unsorted_list))

    for sorted_list in sorted_lists:
        assert is_sorted(sorted_list)


def test_sort_list_same_element():
    unsorted_list = []
    for n in range(10):
        unsorted_list.append(3)

    sorted_list = sort_list(unsorted_list)

    assert (is_sorted(sorted_list))


def test_sort_list_empty_list():
    unsorted_list = []

    sorted_list = sort_list(unsorted_list)

    assert (is_sorted(sorted_list))
