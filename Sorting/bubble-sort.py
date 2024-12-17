def bubbleSort(array):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(0,len(array)-1):
            if array[i]>array[i+1]:
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
        for i in range(len(array)-2,0,-1):
            if array[i]<array[i-1]:
                temp=array[i]
                array[i]=array[i-1]
                array[i-1]=temp
                sorted=False
    return array
