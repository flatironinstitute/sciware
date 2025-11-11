### TODO:
# - Test that the midpoint function works correctly.
# - Test that binary_search returns the correct index for a target in the list.
# - Test that binary_search returns -1 for a target not in the list.


def midpoint(low, high):
    return (low + high) // 2


def binary_search(lst, target) -> int:
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = midpoint(low, high)
        guess = lst[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1
