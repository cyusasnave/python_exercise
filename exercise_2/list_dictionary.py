list_of_items = ['my', 'list', 'of', 'items']

def list_to_dictionary(items):
    my_dictinary = {}
    for item in items:
        my_dictinary[item] = len(item)

    return my_dictinary

print(list_to_dictionary(list_of_items))