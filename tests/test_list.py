import pytest

test_data = [([1, 2, 3], [1, 2], 3),
             (["a", "b", "c"], ["a", "b"], "c"),
             ([None, None], [None], None)]

test_data_2 = [([1, 2, 3], [3, 2, 1]),
               (["abc"], ["abc"]),
               (["a", 1, None], [None, 1, "a"])]

test_data_3 = [([1, 2, 3], [1, 2], [1, 2, 3, 1, 2]),
             (["a", "b", "c"], ["a", "b"], ["a", "b", "c", "a", "b"]),
             ([None, None], [None], [None, None, None])]

test_data_4 = [([1, 2, 3], [1, 2], [1, 2, 3, [1, 2]]),
             (["a", "b", "c"], ["a", "b"], ["a", "b", "c", ["a", "b"]]),
             ([None, None], [None], [None, None, [None]])]


def test_list_count_method():
    assert [1, 2, 3, 4, 4, 4].count(4) == 3


@pytest.mark.parametrize("original_list, desired_list, desired_item", test_data)
def test_list_pop_method(original_list, desired_list, desired_item):
    assert original_list.pop() == desired_item
    assert original_list == desired_list


@pytest.mark.parametrize("original_list, desired_list", test_data_2)
def test_list_reverse_method(original_list, desired_list):
    original_list.reverse()
    assert original_list == desired_list


@pytest.mark.parametrize("original_list, list_to_extend, desired_list", test_data_3)
def test_list_extend_method(original_list, list_to_extend, desired_list):
    original_list.extend(list_to_extend)
    assert original_list == desired_list


@pytest.mark.parametrize("original_list, list_to_append, desired_list", test_data_4)
def test_list_append_method(original_list, list_to_append, desired_list):
    original_list.append(list_to_append)
    assert original_list == desired_list
