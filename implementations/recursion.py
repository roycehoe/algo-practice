from re import L


def while_loop_countdown(i):
    while i > 0:
        print(i)
        i -= 1


def recursive_countdown(i):
    print(i)
    if i <= 0:  # base case
        return
    recursive_countdown(i - 1)  # recursive case


"""
The stack
 - Like a stack of plates, you can add plates to the top, and take plates away from the top. You cannot access "middle" or "end" plates
   - Add plates = push
   - Remove plates = pop
 - 
"""


def emphasise_name(name):
    print("Remember to vote", name, "in the coming elections")


def bye():
    print("Got to go now. Bye!")


def campaign_speech(name):
    """
    How this works:

     - Computer allocates memory for {campaign_speech} function call. Stack 1.
     - Save {name} vairable to memory. Done in stack 1.
     - Print "hello, I am {name}"
     - Suspend {campaign_speech} in a partially completed state

     - Computer allocates memory for {emphasise_name} function call. Stack 2.
     - Save {name} vairable to memory. Done in stack 2.
     - Executes {emphasise_name}. Returns from function call. Pops {emphasise_name} from stack

     - Resume {campaign_speech}. Note that {name} in {campaign_speech} is still saved in memory
     - Executes {bye}
     - Return from {campaign_speech} function call
    """
    print("hello, I am", name)
    emphasise_name(name)
    bye()

#####


def factorial(i):
    """
    When i == 1, 1 is returned. {factorial} is not returned. This breaks the recurssion

    Things to note:
     - Each {factorial} function call has its own value of {i} that you cannot access
     - Drawback: This makes recurssion memory intensive since all values of {i} is saved within half-completed function calls
     - Solution: Use a loop, or use tail recursion


    """
    if i == 1:  # base case
        return 1
    return i * factorial(i - 1)  # recursive case


print(factorial(10))
