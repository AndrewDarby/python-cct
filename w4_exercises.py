"""
    =========== Exercise 1 =============
    Add a docstring to the function below.
    The function takes a list and prints all 
    the items in the list.
    Bonus: Try using type declaration for the argument.
"""


def print_list(list_to_parse: []):
    """
    print out list of items
    """
    for item in list_to_parse:
        print(item)

print_list(["milk","eggs"])
"""
    =========== Exercise 2 =============
    Implement the delete_item() function
    below, all the details to do so should
    be there for you.
    Hint: you can use del(list[index]) to remove
    an item from a list.
"""
def delete_item(list_to_parse, item_index):
    """
    Takes a list, removes an item at the 
    specified index and returns the list
    Parameters
    ----------
    list_to_parse:
        The list to remove the item from
    item_index:
        The index to remove an item from
    Returns
    -------
    The list with the item removed
    """
    # Do stuff here
    list_to_parse.pop(item_index)
    return list_to_parse

shopping_list = ["eggs", "ham", "sausages"] # A test list to remove an item from
shopping_list = delete_item(shopping_list, 2) # Should remove 'ham' from the list
print_list(shopping_list)
