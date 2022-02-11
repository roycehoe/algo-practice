"""
Like how we store items in drawers, computers store items in drawers too. These drawers are called memory.

Arrays
 - Stores instructions and items right next to each other in memory.
 - Random access
 - Problem: When there is no more memory to put instructions/items next to each other
 - Solution: Allocate ajacent memory whenever you create an array
 - Problem: Wasted memory, not perfect as you might exceed the allocated ajacent memory
 - Good: No need to iterate through each item. You know the address for every item in your array.

Linked lists
 - Stores instructions anywhere in memory
 - Each item stores the address of the next item in the list
 - Sequential access
 - Good: Can store memory anywhere
 - Problem: You need to iterate through each item of the list to find the next address and so on, till you find the item you are looking for

---
Reading
---

Array
 - No need to iterate through each item. You know the address for every item in your array
 - O(1)

Linked List
 - You need to iterate through each item of the list to find the next address and so on, till you find the item you are looking for
 - O(n)

---
Insertion
---

Array
 - To insert a new element, you need to shift all following elements down 1 memory address
 - O(n)

Linked List
 - To insert a new element, you just need to get 1 element to point to the new element, and the new element to point to the next element
 - O(1)

---
Deletion
---

Array
 - Same concept and runtime as insertion

Linked list
 - Same concept and runtime as insertion

---
Final words
---
These are not mutually exclusive concepts. Companies use both concurrently: Linked list to narrow down search parameters; Array to search for parameter
"""


#####

"""
Selection sort
"""




from random import shuffle
def selection_sort(sort_range):
    """
    Finding the largest value in unsorted_list takes n operations
    There are n items in the unsorted_list
    Therefore, bigO is n^^2
    """

    unsorted_list = [i for i in range(0, sort_range)]
    shuffle(unsorted_list)
    sorted_list = []

    for i in range(0, sort_range):

        max_number = max(unsorted_list)
        sorted_list.append(max_number)
        unsorted_list.remove(max_number)

    print(sorted_list)


selection_sort(30)
