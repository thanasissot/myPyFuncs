# cached fibonacci

cache = dict()
def memFib(n):
    """Stores result in cache dictionary to be used at function
    definition time, making it faster than first caching then
    using it again for faster results
    """
    if n in cache:
        return cache[n]
    
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = memFib(n - 1) + memFib(n -2)
            cache[n] = result
            return result