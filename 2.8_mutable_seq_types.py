l = [1, 2, 3, 4, 5]

def get_list_information(some_list):
    # use id() to get the list id
    print(f"the list has id: {id(some_list)}")
    # use l[0] to get the first element.
    print(f"the first element of the list is: {some_list[0]}")
    return "done"


def post_new_element(some_list, el, new_el):
    """
    param: some_list: the list to be altered
    param: el: the element in some_list to be changed
    param: new_el: the new value in el
    """
    some_list[el] = new_el
    return some_list


def del_list(some_list):
    """ function clears the list, while
    showing that the memory address does
    not change"""
    print(f"the list has id: {id(some_list)}")
    print("----------clearing list----------")
    some_list.clear()
    print(f"the list has id: {id(some_list)}")
    return "done"


def append_new_object(some_list):
    """ using the + operator will change the object we are 
    working with, and append to it.
    This is a concatination and does not mutate the list."""

    new_list = some_list + [9]
    print("We make a new list, CATing onto the old list: new_list = some_list + [9]")
    print(f"new_list = {new_list}")
    print(f"some_list = {some_list}")
    print(f"id of new_list = {id(new_list)}")
    print(f"id of some_list = {id(some_list)}")
    return "done"


def append_same_object(some_list):
    """ using append() will change the state of  the object, mutating it."""
    print(f"Memory address of our list: {id(some_list)}")
    new_list = some_list.append(9) 
    print("We only append to our old list: new_list = some_list.append(9)")
    print(f"Our new_list is null: new_list = {new_list}")
    print(f"To really see, let's check the type of new_list: type(new_list) = {type(new_list)}")
    print(f"some_list = {some_list}")
    print(f"id of new_list = {id(new_list)}")
    print(f"id of some_list = {id(some_list)}")
    return "done"
    

def extend_list(some_list):
    """ we cannot append multiple elements to our list, so we use extend()
    If we append an iterable, then it appends the whole object to the end.
    extend() actually unpacks and appends all elements"""
    print(f"This is our list: {some_list}")
    one_el = [9]
    tre_el = [9, 8, 7]
    some_list.append(one_el)
    print(f"Appending some_list with a single element iterable: {some_list}")
    some_list.append(tre_el)
    print(f"Appending some_list with a multi-element iterable: {some_list}")
    some_list.extend(one_el)
    print(f"extending some_list with a single element iterable: {some_list}")
    some_list.extend(tre_el)
    print(f"extending some_list with a multi-element iterable: {some_list}")
    return "done"

