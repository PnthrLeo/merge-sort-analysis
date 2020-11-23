from algorithm import merge_sort

import pytest
import random


# Set random seed for result reproducibility
random.seed(42)


@pytest.fixture
def input_1000_pos():
    arr = []
    for i in range(1000):
        num = random.uniform(1.0, 2**32)
        arr.append(num)
    return arr


@pytest.fixture
def input_1000_neg():
    arr = []
    for i in range(1000):
        num = random.uniform(-2**32, -1.0)
        arr.append(num)
    return arr


@pytest.fixture
def input_1000_pos_neg():
    arr = []
    for i in range(1000):
        num = random.uniform(-2**31, 2**31)
        arr.append(num)
    return arr


def test_empty_arr():
    assert merge_sort([], 0, 0) == []


def test_one_element_arr():
    assert merge_sort([42], 0, 0) == [42]


def test_two_elements_arr():
    assert merge_sort([42, 5], 0, 1) == [5, 42]


def test_pos_array(input_1000_pos):
    assert merge_sort(input_1000_pos, 0, 999) == sorted(input_1000_pos)


def test_neg_array(input_1000_neg):
    assert merge_sort(input_1000_neg, 0, 999) == sorted(input_1000_neg)


def test_pos_neg_array(input_1000_pos_neg):
    assert merge_sort(input_1000_pos_neg, 0, 999) == sorted(input_1000_pos_neg)
