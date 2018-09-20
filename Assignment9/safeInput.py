# Here is the definition of safe_input. It should contain this exception:
except ValueError:
    print("Error: please enter a value of ", a_type)

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))