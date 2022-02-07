"""
Divide-and-conquer technique using Quicksort
"""

"""
Divide-and-conquer
 - Figure out a base case
 - Divide/decrease your problem until it becomes the base case
"""


def sum_with_loop(array):
    total = 0
    for i in array:
        total += i
    return total


def sum_with_divide_and_conquer(array):
    """
    The total sum is the first number of the list, plus the sum of the rest of the list
    Recursion is applied to the rest of the list
    This is done until the length of the list is empty

    Base case: When array[0] + return 0
    """
    if len(array) == 0:
        return 0
    return array[0] + sum_with_divide_and_conquer(array[1:])


"""
Quicksort

 - Look at an array
 - If the array is less than 2 elements, there is no need to sort. Just return the array

 [1,5,4]
 - Pick a pivot (eg. 4)
 - Cast all numbers smaller and bigger than the pivot into {left_array} and {right_array} respectively
 - If {left_array} and {right_array} length is more than 2, call the function again to sort
"""


def quicksort(array):
    if len(array) < 2:  # No need to sort array if length is < 2
        return array

    pivot = array[0]  # Pick a pivot
    # Get an array of numbers less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # Get an array of numbers more than the pivot
    greater = [i for i in array[1:] if i >= pivot]

    # Add the arrays together
    return quicksort(less) + [pivot] + quicksort(greater)


"""
Notes about quicksort
 - Speed is dependent on the pivot chosen

 Array of 8 numbers (let n = 8, the length of the array)
 - If your pivot is the largest/smallest number, you will take n function calls. That is the height of the stack.
 - Each function call takes n operations to complete since you need to touch the entire array. That is the time taken to clear the entire stack.
 - Your entire function therefore takes O(n**2 to run)

 - If your pivot is the middle number, you will take log(n) function calls. This is the height of the stack
 - Each function call takes (n) operations to complete since you need to touch the entire array. That is the time taken to clear the entire stack.
 - Your entire function therefore takes O(n log n) to run


 - Best case scenario: x/2, Worst case scenario: x
"""

"""
Notes about Big O:
 - The time it takes for an algorithm to run is fixed time plus variable time
 - Algorithms take some fixed time to run (c)
 - Once run, it will execute some operations (n) that takes (x) time to run per operation. The variable time is therefore xn.
 - Therefore, the time taken for an algorithm to run is = c + xn
 - When you recursively call an algorithm, you will now need to take into account for (c)
"""

"""
Average case vs Worst case
 - 


"""
