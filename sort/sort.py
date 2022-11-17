def bubble(_list):
    """
    Sort a numeric list using bubble sort
    Args:
        _list: list to be sorted
    Returns:
        _list: sorted list
    Raises:
        TypeError: If the list has invalid element(s)
    """

    length = len(_list)
    sorted = True

    for i in range(length):

        # Return if last element
        if i + 1 == length:
            # Return sorted list if no elements were swapped
            if sorted:
                return _list
            # Call function again for nth passthrough if array elements were swapped
            else:
                return bubble(_list)

        else:
            # Swap elements if the first one is smaller
            if _list[i] > _list[i + 1]:
                _list[i], _list[i + 1] = _list[i + 1], _list[i]
                sorted = False


def insertion(_list, _position=0):
    """
    Sort a numeric list using insertion sort
    Args:
        _list: list to be sorted
    Returns:
        _list: sorted list
    Raises:
        TypeError: If the list has invalid element(s)
    """

    length = len(_list)

    for i in range(length)[_position:]:

        # Base case, reached end of list
        if i + 1 == length:
            return _list

        else:
            # Swap last element of sorted sub list and first element of unsorted sublist if they are not in order
            if _list[i] > _list[i + 1]:
                _list[i], _list[i + 1] = _list[i + 1], _list[i]

                # Move new element down sorted sublist until it is in the correct spot
                j = 1
                while _list[i - j + 1] < _list[i - j]:

                    # break out of loop if it reaches first element
                    if (i - j) < 0:
                        break

                    # Move element down one spot in sorted sublist
                    _list[i - j + 1], _list[i - j] = _list[i - j], _list[i - j + 1]
                    j += 1

                # Increase size of sorted sublist and go to next passtrhough
                return insertion(_list, i + 1)

            # If they are in order, increase size of sorted sublist and go to next passthrough
            else:
                return insertion(_list, i + 1)


def quick(_list, low=0, high=-1):
    """
    Sort a numeric list using quick sort
    Args:
        _list: list to be sorted
        low: low index of list
        high: high index of list
    Returns:
        _list: sorted list
    Raises:
        TypeError: If the list has invalid element(s)
    """

    # Set high index if it is the initial call
    if (high == -1):
        high = len(_list) - 1
    
    if (low < high):
        p = part(_list, low, high)
        quick(_list, low, p - 1)
        quick(_list, p + 1, high)

    return _list

def part(_list, low, high):
    """
    Sub function of quick()
    Args:
        _list: list to be sorted
        low: low index of list
        high: high index of list
    Returns:
        i+1: index of list partition
    Raises:
        TypeError: If the list has invalid element(s)
    """
    
    length = len(_list)
    pivot = _list[high]
    i = low - 1

    # Loop through list partition
    for j in range(length)[low:high]:
        if (_list[j] <= pivot):
            i += 1
            _list[i], _list[j] = _list[j], _list[i]
    
    _list[i+1], _list[high] = _list[high], _list[i+1]

    # Return partition index
    return (i+1)