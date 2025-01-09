def insertionSort(array):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                sorted=False
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
                for j in range(i,0,-1):
                    if array[i]<array[i-1]:
                        temp=array[i]
                        array[i]=array[i-1]
                        array[i-1]=temp
    return array
