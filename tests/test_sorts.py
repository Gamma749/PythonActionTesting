from sorting.sorts import quick_sort, insertion_sort, selection_sort

testing_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 9, 2, 8, 3, 7, 4, 6, 5],
    [4, 2, 6, 1, 3, 7, 8, 9, 5]
]


def test_insertion_sort():
    for list in testing_lists:
        assert insertion_sort(list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_selection_sort():
    for list in testing_lists:
        assert selection_sort(list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_quick_sort():
    for list in testing_lists:
        assert quick_sort(list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
