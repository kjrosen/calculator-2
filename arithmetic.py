"""Functions for common math operations."""


def add(nums):
    """Return the sum of the two input integers."""
    sum_nums = 0
    for num in nums:
        sum_nums += num
    return sum_nums


def subtract(nums):
    """Return the second number subtracted from the first."""
    difference = nums[0]
    nums.pop(0)

    for num in nums:
        difference -= num
    return difference


def multiply(nums):
    """Multiply the two inputs together."""
    product = 1
    for num in nums:
        product *= num

    return product


def divide(nums):
    """Divide the first input by the second, returning a floating point."""
    quotient = nums[0]
    nums.pop(0)
    
    for num in nums:
        quotient /= num
    return quotient


def square(num1):
    """Return the square of the input."""

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
