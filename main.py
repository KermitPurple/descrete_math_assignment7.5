#!/usr/bin/env python3

from typing import List, TypeVar
from random import randint

T = TypeVar('T') # allows for typehinting unknown types

def bubble_sort(arr: List[T]) -> List[T]:
    '''
    perform the bubble sort algorithm
    :arr: the list of items
    :returns: a sorted list of items
    '''
    result = arr[:] # shallow copy list
    size = len(arr) # size of list
    for i in range(size): # iterate over numbers 0 thru size - 1
        for j in range(size - i - 1): # iterate over numbers thru size -i - 2
            if result[j] > result[j + 1]: # if the first item is more than the second
                result[j], result[j + 1] = result[j + 1], result[j] # swap them
    return result

def merge(a: List[T], b: List[T]) -> List[T]:
    '''
    merge two sorted lists
    :a: the first list
    :b: the second list
    :returns: a list containing all of the elements of the two arguments sorted
    '''
    result = [] # create empty list
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]: # if top item in first is less than top item in second
            result.append(a.pop(0)) # remove from first list and add to result
        else: # otherwise
            result.append(b.pop(0)) # remove from second list and add to result
    # at this point either a or b is empty
    if len(a) == 0: # a is empty
        while len(b) > 0: # while b is not empty
            result.append(b.pop(0)) # remove from second list and add to result
    else: # b is empty
        while len(a) > 0: # while a is not empty
            result.append(a.pop(0)) # remove from first list and add to result
    return result

def merge_sort(arr: List[T]) -> List[T]:
    '''
    perform the merge sort algorithm
    :arr: the list to sort
    :returns: the sorted list
    '''
    size = len(arr) # size of list
    if size <= 1: # if there is one element in list or empty
        return arr # return the given list
    return merge( # merge following lists
            merge_sort(arr[:size // 2]), # sort first half of list
            merge_sort(arr[size // 2:]) # sort second half
            )

def rand_arr(size: int, min_val: int = 0, max_val: int = 10) -> List[int]:
    '''
    creates a list of random numbers
    :size: size of return list
    :min_val: minimum value for numbers in list
    :max_val: maximum value for numbers in list
    :returns: a list of random numbers
    '''
    return [randint(min_val, max_val) for i in range(size)]


def is_sorted(arr: List[T]) -> bool:
    '''
    print array and check if sorted
    :arr: the list of items
    :returns: True if the list is sorted
    '''
    size = len(arr) # size of array
    if size <= 1: # size is 0 or 1
        return True # with 0 or 1 element there is no order
    print('sorted:', arr) # show array
    for i in range(size - 1): # iterate from 0 to size - 2
        if arr[i + 1] < arr[i]: # if the second term is less than the first term
            return False # the list isnt sorted
    return True # otherwise the list is sorted


def test_sort(sort_func):
    '''
    test to make sure a sort function works
    :sort_func: the function that will return a sorted list
    '''
    print('-' * 10, f'testing {sort_func.__name__}', '-' * 10)
    arr = rand_arr(20) # get random array
    print('before:', arr) # show list
    assert is_sorted(sort_func(arr)) # sort print and check list

def main():
    '''driver code'''
    test_sort(bubble_sort)
    test_sort(merge_sort)

if __name__ == '__main__':
    main() # run the main method
