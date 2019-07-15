number = input('Please enter a nmber : ')
try:
    print(int(number) * 7)
except LookupError:
    print('This should never happen')
except ValueError:
    print('You did not enter a base 10 number! Try again')

print('Hello world')



raise ValueError  # to raise an exceptions

# Creating own exceptions in python
class MissingLabelError(KeyError):
    pass

# Builtin python exception

# Attribute Error, when a class doesn't have the attribute that you are trying to access
# Import Error, thrown when a library doesn't exist
# KeyError when a key doesn't exist in a dict
#