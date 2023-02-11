def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter

"""alternative example:
we start with an empty dictionary (array) inside function.
line 28 is how we access our empty dictionary, counts.
zero is default for quantity, not index."""

def letter_counter(phrase):

    counts = {}

    for letter in phrase:
        counts [letter] = counts.get(letter, 0) + 1

    return counts

print(letter_counter('hello'))
