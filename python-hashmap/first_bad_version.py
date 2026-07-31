def first_bad_version(versions: list[bool] | None) -> int:
    """
    versions[i] is False -> good version
    versions[i] is True  -> bad version

    All good versions appear before all bad versions.

    Return the index of the first bad version.
    Return -1 if there is no bad version.

    Examples:
    [False, False, True, True] -> 2
    [True, True, True]         -> 0
    [False, False]             -> -1
    []                         -> -1
    None                       -> -1
    """
    if versions is None:
        return -1
    left = 0
    right = len(versions) -1
    ans = -1
    while left <=right:
        mid = left + (right - left) // 2
        if versions[mid] == True:
            ans = mid
            right = mid -1
        else:
            left = mid +1
    return ans


list = [False, False, True, True]
list1 = [True, True, True]
list2 =  [False, False]
list3 = None
print(first_bad_version(list))
print(first_bad_version(list1))
print(first_bad_version(list3))
print(first_bad_version(list2))
print(first_bad_version([]))

