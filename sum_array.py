def sum_array(arr):
    """Sums an array of integers
    Returns integer"""
    sum = 0
    for num in arr:
        sum += num
    return sum


arr1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]

print "Sum of all integers in array "+ str(arr1) + " is: " + str(sum_array(arr1))
print "Sum of all integers in array "+ str(arr2) + " is: " + str(sum_array(arr2))