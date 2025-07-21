def find_divisors_1(number):
    """
    Create a list of all divisors for a number including 1
    and excluding the number itself.  Modulo will be used
    to test divisibility.
    """


def find_divisors_2(number):
    """
    Same as find_divisors_1 but a list comprehension is used.
    """

# Example usage:
print(find_divisors_1(80)) # [1, 2, 4, 5, 8, 10, 16, 20, 40]
print(find_divisors_2(80)) # [1, 2, 4, 5, 8, 10, 16, 20, 40]
print(find_divisors_1(79)) # [1] ... This is prime
print(find_divisors_2(79)) # [1]
