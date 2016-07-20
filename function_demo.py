def subtractor(a, b): 
   """I subtract b from a and return the result"""  
   print("I'm a function. My name is {}".format(subtractor.__name__))
   print("I'm about to subtract {} and {}\n\n".format(a,b))
   return a - b  # i output a value by using the return statement


if __name__ == '__main__':
	subtractor(3, 2)
	
def print_function():
   """I'm also a function, but I don't take any parameters"""
   print("I'm {}, and I'm printing now".format(print_function.__name__))

if __name__ == '__main__':
   print_function()
   
   
   
def side_effect_test(value):
    # Do something to modify the value
    value[1] = "orange"
    print("Inside the function, the value becomes {}".format(value))

if __name__ == "__main__":
    # Create the value
    value = ["red", "green", "blue"]

    print("Outside the function, the value starts as {}".format(value))

    side_effect_test(value)

    print("Outside the function, the value is now {}".format(value))