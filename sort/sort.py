def bubble(_list):
    '''
    Sort a numeric list using bubble sort

    Args:
        _list: list to be sorted

    Returns:
        _list: sorted list

    Raises:
        TypeError: If the list has invalid element(s)
    '''

    length = len(_list)
    sorted = True

    for i in range(length):

        # Return if last element
        if i+1 == length:
            # Return sorted list if no elements were swapped
            if (sorted):
                return _list
            # Call function again for nth passthrough if array elements were swapped
            else:
                return bubble(_list)

        else:
            # Swap elements if the first one is smaller
            if _list[i] > _list[i+1]:
                _list[i], _list[i+1] = _list[i+1], _list[i]
                sorted = False

def quick(_list):
    '''
        Docstring
    '''
    return

def insertion(_list):
    '''
        Docstring
    '''
    return


if __name__ == '__main__':
    print(bubble([3,2,1,7,9,10,11,45,-1, "a"]))
    print(bubble([0]))
    print(bubble([2,0]))