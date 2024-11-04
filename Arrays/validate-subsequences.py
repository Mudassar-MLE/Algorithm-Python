def isValidSubsequence(array, sequence):
    temp = 0
    for i in range(len(array)):
        if temp < len(sequence) and array[i] == sequence[temp]:
            temp += 1
    return temp == len(sequence)