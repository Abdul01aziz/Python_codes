from int_cast_function import int
print(int("123"))  # Output: 123
print(int(45.67))  # Output: 45
print(int(True))   # Output: 1
print(int(False))  # Output: 0

from General_functions import is_immutable
print(is_immutable(42))          # Output: True (int is immutable)
print(is_immutable("Hello"))     # Output: True (str is immutable)
print(is_immutable([1, 2, 3]))    # Output: False (list is mutable)

from slicing_function import slice_sequence, slice_sequence2
# Using slice_sequence
x1 = slice_sequence([1, 2, 3, 4, 5], start=1, end=4)  # Output: Sliced sequence: [2, 3, 4]
x2 = slice_sequence("Hello, World!", step=2)  # Output: Sliced sequence: Hlo ol! Using slice_sequence
x3 = slice_sequence2([1, 2, 3, 4, 5], start=1, end=4)  # Output: (([1, 2, 3, 4, 5], id), ([2, 3, 4], id))
x4 = slice_sequence2("Hello, World!", start=2, end=10,step=2)  # Output: (("Hello, World!", id), ("lo o", id)))
print(x1)
print(type(x1))
print(x2)
print(type(x2))
print(x3)
print(type(x3))
print(x4)
print(type(x4))