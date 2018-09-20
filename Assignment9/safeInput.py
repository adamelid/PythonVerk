# Here is the definition of safe_input. It should contain this exception:
def safe_input(prompt, a_type):

    while True:
        safe_str = input(prompt)
        try:
            safe_str = a_type(safe_str)
            return safe_str
        except ValueError:
            print("Error: please enter a value of ", a_type)    

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))