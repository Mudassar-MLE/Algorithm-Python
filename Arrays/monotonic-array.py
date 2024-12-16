def isMonotonic(array):
    increament = True
    decreament = True
    for i in range(len(array)-1):
        increament = increament and array[i]<=array[i+1]
        decreament = decreament and array[i]>=array[i+1]
    return increament or decreament
