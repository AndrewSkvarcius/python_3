def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # counter for nums frequency 
    count = {}
   
    for num in nums:
        count[num] = count.get(num, 0) + 1
     
     # finds the most frequent number
    
    max_val = max(count.values())
     
     # finds which index has the most frequent 
    
    for(num, freq) in count.items():
        if freq == max_val:
            return num