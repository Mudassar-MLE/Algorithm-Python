def smallestDifference(arrayOne, arrayTwo):
    smaller=float("inf")
    result=[]
    for x in arrayOne:
        for y in arrayTwo:
            diff=abs(x-y)
            if diff<smaller:
                smaller= diff
                result=[x,y]
    return result
