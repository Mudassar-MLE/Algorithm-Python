def getNthFib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return getNthFib(n-1)+getNthFib(n-2)
################################################################################

def getNthFib(n, memorize={1:0,2:1}):
    if n in memorize:
        return memorize[n]
    else:
        memorize[n]=getNthFib(n-1, memorize) + getNthFib(n-2, memorize)
        return memorize[n]