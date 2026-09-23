from int_cast_function import int
print(int("123"))  # Output: 123
print(int(45.67))  # Output: 45
print(int(True))   # Output: 1
print(int(False))  # Output: 0

from General_functions import is_immutable
print(is_immutable(42))          # Output: True (int is immutable)
print(is_immutable("Hello"))     # Output: True (str is immutable)
print(is_immutable([1, 2, 3]))    # Output: False (list is mutable)