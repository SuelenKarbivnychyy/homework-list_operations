"""Utilities for manipulating lists."""

def head(input_list):
    """Return the first item of the input list.   
    For example:
      >>> head(['Jan', 'Feb', 'Mar'])
      'Jan'"""  
    
    first = input_list[0]
    return [first]
#print (head(['Jan', 'Feb', 'Mar']))



def tail(input_list):
    """Return a new list of all items, excluding the first item.

    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']
    """
    new_list = input_list[1:]
    return [new_list]
# print(tail(['Jan', 'Feb', 'Mar']))

def last(input_list):
    """Return the last item of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'
    """
    last_item = input_list[-1]
    
    return [last_item]
# print(last(['Jan', 'Feb', 'Mar']))    


def top(input_list):
    """Return all elements of the input list except the last.

    For example:

    >>> top(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']
    """
    except_last = input_list[:-1]
    return [except_last]
# print(top(['Jan', 'Feb', 'Mar']))    


def first_three(input_list):
    """Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """
    first_three_elem = input_list[:3]
    return first_three_elem
#print(first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May']))


def last_five(input_list):
    """Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """
    last_five_elems = input_list[-1:-6]
    #print(last_five_elems)
    return [last_five_elems]
#print (last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
  


# def middle(input_list):
#     """Return all elements of input_list except the first two and the last two.

#     For example:

#     >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
#     [6, 9, 12, 15, 18, 21]

#     """

#     return []


# def inner_four(input_list):
#     """Return the third, fourth, fifth, and sixth elements of input_list.

#     For example:

#     >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
#     [6, 9, 12, 15]

#     """

#     return []


# def inner_four_end(input_list):
#     """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

#     This function should return those elements in a list, in the exact order
#     described above.

#     For example:

#     >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
#     [12, 15, 18, 21]

#     """

#     return []


# def replace_head(input_list):
#     """Replace the head of input_list with the value 42 and return nothing.

#     Input list must be modified in-place, not merely reassigned to a new value.

#     For example:

#     >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
#     >>> replace_head(multiples)
#     >>> multiples
#     [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]

#     """

#     pass


# def replace_third_and_last(input_list):
#     """Replace third and last elements of input_list with 37 and return nothing.

#     Input list must be modified in-place, not merely reassigned to a new value.

#     For example:

#     >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
#     >>> replace_third_and_last(multiples)
#     >>> multiples
#     [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]

#     """

#     pass


# def replace_middle(input_list):
#     """Replace all elements of a list but the first two and last two with 42 and 37.

#     After the replacement, 42 and 37 should appear in that order in input_list.
#     Input list must be modified in-place, not merely reassigned to a new value.

#     Return nothing.

#     For example:

#     >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
#     >>> replace_middle(multiples)
#     >>> multiples
#     [0, 3, 42, 37, 24, 27]

#     """

#     pass


# def delete_third_and_seventh(input_list):
#     """Remove third and seventh elements of input_list and return nothing.

#     Input list must be modified in-place, not merely reassigned to a new value.

#     For example:

#     >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
#     >>> delete_third_and_seventh(notes)
#     >>> notes
#     ['Do', 'Re', 'Fa', 'So', 'La', 'Do']

#     """

#     pass


# def delete_middle(input_list):
#     """Remove all elements from input_list except the first two and last two.

#     Input list must be modified in-place, not merely reassigned to a new value.

#     Return nothing.

#     For example:

#     >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
#     >>> delete_middle(notes)
#     >>> notes
#     ['Do', 'Re', 'Ti', 'Do']

#     """

#     pass
