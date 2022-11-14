def main(_list, sorted):
    '''
        Docstring
    '''

    length = len(_list)

    # Base case, return list if it is sorted
    if (sorted):
        return _list
    
    else:
        sorted = True
        for i in range(length):

            # Return if last element
            if i+1 == length:
                return main(_list, sorted)

            else:
                # Swap elements if the first one is smaller
                if _list[i] > _list[i+1]:
                    _list[i], _list[i+1] = _list[i+1], _list[i]
                    sorted = False

if __name__ == '__main__':
    print(main([3,2,1,7,9,10,11,45,-1], False))