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


def insertion(_list, _position=0):
    '''
        Sort a numeric list using insertion sort
        Args:
            _list: list to be sorted
        Returns:
            _list: sorted list
        Raises:
            TypeError: If the list has invalid element(s)
    '''

    length = len(_list)

    for i in range(length)[_position:]:
        
        # Base case, reached end of list
        if i + 1 == length:
            return _list
        
        else:
            # Swap last element of sorted sub list and first element of unsorted sublist if they are not in order
            if _list[i] > _list[i+1]:
                _list[i], _list[i+1] = _list[i+1], _list[i]
                
                # Move new element down sorted sublist until it is in the correct spot
                j = 1
                while _list[i-j+1] < _list[i-j]:
                    if (i-j) < 0:
                        return insertion(_list, i+1)
                    _list[i-j+1], _list[i-j] = _list[i-j], _list[i-j+1]
                    j += 1
                
                return insertion(_list, i+1)  

            # If they are in order, increase size of sorted sublist and go to next passthrough
            else:
                return insertion(_list, i+1)

def quick(_list):
    '''
        Docstring
    '''
    return




if __name__ == '__main__':
    #print(bubble([3,2,1,7,9,10,11,45,-1, "a"]))
    #print(bubble([0]))
    #print(bubble([2,0]))

    print(insertion([10,1,0,8,-1]))