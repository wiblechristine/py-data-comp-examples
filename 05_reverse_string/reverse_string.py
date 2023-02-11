def reverse_string(phrase):
    """Have a passed through string (phrase) reverse itself when called in iPython.

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    return phrase[::-1]

"""This [::-1] means start at the end of a string and end at 0 index, with the
increment of -1 in order to work backwards by a single step.

If the string was saved to a variable, the reversal would look like this:

txt = 'awesome'
print(text)
"""