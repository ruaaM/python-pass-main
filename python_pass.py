"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""

class StringOperations:
    "3"
    def reverse(self, *, to_be_reversed: str = None): 
            for char in reversed(to_be_reversed):
             	return char
    
"1 & 4"
class ReversedString(StringOperations):

            
       def __init__(self, to_be_reversed):
        self.to_be_reversed =to_be_reversed
        pass
"2 & 5"
print(StringOperations.reverse(self="Hello"))