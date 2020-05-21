"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print Each item in a given list
    Example:
    >>> output_all_items([1,'hello',True])
    1
    hello
    True
    """

    for item in items:
        print(item)


def get_all_evens(nums):
    """Given a list of numbers, return a list of all even numbers

    >>> get_all_evens([7,8,10,1,2,2])
    [8, 10, 2, 2]
    """

    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    """Given a list, return all elements at odd numbered indices.

    >>> get_odd_indices([1,'hello',True,500])
    ['hello', 500]
    """

    result = []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])

    return resultprint


def print_as_numbered_list(items):
    """Return a list of numbers in a certain range
    >>> print_as_numbered_list([1, "hello", True])
    1. 1
    2. hello
    3. True
    """

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i +=1

def get_range(start, stop):
    """Return a list of numbers in a certain range"""
    
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums

def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with "*"."""

    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        chars.append(letter)

    return "".join(vowels)


def snake_to_camel(string):
    """ Given a string in snake case, return a string in upper camel case."""
    
    camel_case = []

    for word in string.split("_"):
        camel_case.append(word.title())

    "".join(camel_case)

def longest_word_length(words):
    """Return the length of the longest word in the given list of words"""

    longest = len(word[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest



def truncate(string):
    """Truncate repeating characters into one character"""

    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result)-1]:
            result.append(char)


def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced"""

    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

        if parens < 0:
            return False

    return parens == 0


def compress(string):
    """Return a compressed version of a given string"""

    compressed = []

    curr_char = ""
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0

        char_count += 1 

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)

