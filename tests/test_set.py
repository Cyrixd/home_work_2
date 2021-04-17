import pytest

test_data = [({1, 2, 3}, {1, 4}, {1, 2, 3, 4}),
             ({"a", "b", "c"}, {"d", "e"}, {"a", "b", "c", "d", "e"})]

test_data_2 = [({1, 2, 3}, {9, 4}),
               ({"a", "b", "c"}, {"d", "e"})]

test_data_3 = [({1, 2, 3}, {1, 2, 3, 4, 99}),
               ({"a", "b", "c"}, {"a", "b", "c", "d", "e"})]

test_data_4 = [({1, 2, 3}, 1, {2, 3}),
               ({"a", "b", "c"}, "e", {"a", "b", "c"})]


@pytest.mark.parametrize("original_set, other_set, desired_set", test_data)
def test_set_union_method(original_set, other_set, desired_set):
    assert original_set.union(other_set) == desired_set


@pytest.mark.parametrize("original_set, other_set", test_data_2)
def test_set_isdisjoint_method(original_set, other_set):
    assert original_set.isdisjoint(other_set)


@pytest.mark.parametrize("sub_set, super_set", test_data_3)
def test_set_issubset_method(sub_set, super_set):
    assert sub_set.issubset(super_set)


@pytest.mark.parametrize("sub_set, super_set", test_data_3)
def test_set_issuperset_method(sub_set, super_set):
    assert super_set.issuperset(sub_set)


@pytest.mark.parametrize("original_set, discard_item, desired_set", test_data_4)
def test_set_discard_method(original_set, discard_item, desired_set):
    original_set.discard(discard_item)
    assert original_set == desired_set
