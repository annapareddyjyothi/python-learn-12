# 2D List (list of lists)
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("2D List:", list_2d)

# 2D Tuple (tuple of tuples)
tuple_2d = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("2D Tuple:", tuple_2d)

# 2D Dictionary (dict of dicts)
dict_2d = {
    'row1': {'a': 1, 'b': 2, 'c': 3},
    'row2': {'a': 4, 'b': 5, 'c': 6},
    'row3': {'a': 7, 'b': 8, 'c': 9}
}
print("2D Dictionary:", dict_2d)

# 2D Set (set of frozensets, since sets themselves can't contain other sets)
set_2d = {frozenset([1, 2, 3]), frozenset([4, 5, 6]), frozenset([7, 8, 9])}
print("2D Set:", set_2d)
