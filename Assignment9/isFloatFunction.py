def is_float(stringArgument):
    try:
        float(stringArgument)
        return True
    except ValueError:
        return False
# is_float function definition goes here

# Do not change the lines below
print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))