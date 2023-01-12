# Python has no command for declaring a variable.

x = 10
y = "Naoto"

print(x)    # 10
print(y)    # Naoto

# Variables do not need to be declared with any particular type, 
# and can even change type after they have been set.
x = 10          # x is of type integer
x = "Naoto"     # x is now of type string

print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(10)     # x will be '10'
y = int(10)     # y will be 10
z = float(10)   # z will be 10.0


# When you want to check a data type of variable, you can use type().
x = 10

print(type(x))  # <class 'int'>

# The rules of variable names
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
myname      = "Naoto"
my_name     = "Naoto"
_my_name    = "Naoto"
myName      = "Naoto"
MYNAME      = "Naoto"
myname2     = "Naoto"

# Many values to multiple variables
x, y, z = "Toyota", "BMW", "Nissan"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "Toyota"
print(x)
print(y)
print(z)

# Unpack a collection
cars = ["Toyota", "BMW", "Nissan"]
x, y, z = cars
print(x)
print(y)
print(z)

# Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


