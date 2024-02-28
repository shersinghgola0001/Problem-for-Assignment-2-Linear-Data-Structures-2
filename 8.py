#Q8. Reverse a string using a stack data structure.

def reverse_string(input_string):
    stack = []
    
    for char in input_string:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

input_str = "Data Science!"
reversed_str = reverse_string(input_str)
print(reversed_str)
