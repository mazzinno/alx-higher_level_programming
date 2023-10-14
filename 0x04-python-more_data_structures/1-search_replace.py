#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda el: replace if el == search else el, my_list))
