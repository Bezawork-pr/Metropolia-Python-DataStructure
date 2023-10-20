"""Write a function to combine two lists"""
def combine_lists(list_one, list_two):
    joined_list = list_one + list_two
    joined_list.sort()
    return joined_list
