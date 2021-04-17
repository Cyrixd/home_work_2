import pytest

test_data = [({'a': 1, 'b': 2}, [('a', 1), ('b', 2)]),
             ({1: 'a', 2: 'b'}, [(1, 'a'), (2, 'b')])]

test_data_2 = [({'a': 1, 'b': 2}, ('b', 2), {'a': 1}),
               ({1: 'a', 2: 'b'}, (1, 'a'), {2: 'b'})]

test_data_3 = [({'a': 1, 'b': 2}, [1, 2]),
               ({1: 'a', 2: 'b'}, ['a', 'b'])]

test_data_4 = [({'a': 1, 'b': 2}, ['a', 'b']),
               ({1: 'a', 2: 'b'}, [1, 2])]


@pytest.mark.parametrize("original_dict, desired_list", test_data)
def test_dict_items_method(original_dict, desired_list):
    assert list(original_dict.items()) == desired_list


@pytest.mark.parametrize("original_dict, pop_items, desired_dict", test_data_2)
def test_dict_pop_method(original_dict, pop_items, desired_dict):
    assert original_dict.pop(pop_items[0]) == pop_items[1]
    assert original_dict == desired_dict


@pytest.mark.parametrize("original_dict, values_list", test_data_3)
def test_dict_values_method(original_dict, values_list):
    assert list(original_dict.values()) == values_list


@pytest.mark.parametrize("original_dict, keys_list", test_data_4)
def test_dict_values_method(original_dict, keys_list):
    assert list(original_dict.keys()) == keys_list


def test_dict_get_method():
    d = {'a': 1, 'b': 2}
    assert d.get('b') == 2
