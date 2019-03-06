thearchive = {
    "List1": ["Bob","Comes","After","You"],
    "List2": [100,"Hello"]
}

# function takes a dict, a list name and the element
def add_to_list_in_dict(thearchive, listname, element):
    try:
        thearchive[listname].append(element)
        print("Added %s to %s." % (element, listname))
    except KeyError:
        print("The archive doesn't have the following key: %s" % (listname))

add_to_list_in_dict(thearchive, "List1", "Hello")
add_to_list_in_dict(thearchive, "Book", "Page1")
