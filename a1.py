from typing import List, TypeVar
import math


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.
    

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    #solution 1:
    # if n < 0:
    #     return n * -1
    # else:
    #     return n
    
    #solution 2:
    n = n ** 2
    n = math.sqrt(n)
    return n


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    if n < 0:
        print("Number cannot be negative")
    elif n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n - 1) ## yay recursion


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    newList = List[T]
    for i in range(0, len(lst), 2):
        newList.append(lst[i])
    return newList


def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    total = 0
    for i in range(0, len(lst)):
        total = total + lst[i]
    return total


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    total = 0
    for i in range(0, len(lst)):
        total = total + lst[i]
    return total / len(lst)


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    lst.sort()
    if len(lst) % 2 == 0:
        mid1 = len(lst) // 2
        mid2 = mid1 - 1
        median = (lst[mid1] + lst[mid2]) / 2.0
    else:
        mid = len(lst) // 2
        median = lst[mid]

    return median



def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
    knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
    'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    index = 0
    count = 0

    while len(lst) > 2:
        count += 1
        if index >= len(lst):
            index = 0
        if count == 3:
            lst.pop(index)
            count = 0
        else:
            index += 1

    return lst



# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")