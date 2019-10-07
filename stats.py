def variance(data):
    """Returns the population variance of a list (array) of numbers in data.
    
    The variance is the sum of squared differences between data values
    and their mean, divided by the number of items in the list (n).
    This is different from the sample variance, where the sum is divided by (n-1).
    Example: variance([1,5]) is ((1-3)**2 + (5-3)**2)/2 = 4.
    
    Args:
        data -- list of numbers for which variance will be computed. 
           Must contain at least one element.
    Returns:
        population variance of values in data list.
    Throws:
        ValueError if the data parameter is empty.

    Examples: see README.md for examples
    """
    n = len(data)
    if n == 0:
        raise TypeError()
    average = sum(data)/n
    return sum( [(x-average)**2 for x in data] )/n
