def frequency(lst, search_term):
    """Return frequency of search_term in list (array).
    iPython or terminal entries:
        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """

    return lst.count(search_term)

"""alternative additions to function for passing an example through"""

a = [1, 2, 3, 4, 4]
b = 4

print(f'{b}vis found {frequency(a, b)} times in the list: {a}')
