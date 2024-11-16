def moveElementToEnd(array, toMove):
    if array == []:
        return array
    for i in range(len(array) + 1):
        if array[-i] == toMove:
            move = array.pop(-i)
            array.append(move)
    return array
