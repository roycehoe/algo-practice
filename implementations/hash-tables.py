"""
Let's say you want to find the price of an item in the Ikea catalogue. 
Wouldn't it be nice to have someone who memorized the entire catalogue, and can tell you the exact price of the item in an instant?

Hash function
 - Takes in a string input (name of ikea item); returns a number (price of ikea item)
 - Feature: must be consistent. Same input returns same output.
 - Feature: must map different words to different numbers. Different inputs give different results

How to use a hash function
 - I have an array and a hash function

 - Input the name of the item into hash function
 - Hash function outputs a number
 - The number corresponds to an index in the array. This index in the array holds the price of the item

 - Feature: Hash function does not return invalid indexes

 - Note: Python has hash tables; they are called dictionaries
 - Note: Hash function + Array = Hash table

Hash tables and caching
 - People make the same requests to certain pages. Eg. Google home page
 - Instead of the server calculating the data each time someone visits the page, they just cache the data
 - This is done by checking if the URL is in the hash
 - If it is, it would send the cache data
 - If it isn't, the server would do some work

Hash tables and collisions
 - Hash tables cannot have collisions
 - In order to prevent collisions, you can do 2 things: Create a better hash function, or create a linked list
 - Linked list: When a collision happens, put items in a linked list. You will now need to do 2 searches, one for the hash table, and one for the linked list
 - Better hash function: Try to map keys evenly all over the hash

Big O:
 - Hash tables take constant time to run, no matter how large (n) is
 - O(1)

Load factor:
 - Load factor = Items in hash table * Total number of slots
 - 1 slot, 100 items, load factor = 100
 - To decrease load factor, simply increase the number of slots. People typically double the number of slots

"""
