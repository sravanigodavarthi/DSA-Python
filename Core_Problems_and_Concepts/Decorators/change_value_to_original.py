# Create a method that takes an input x and subtract 2 from it and returns the result. 
# Now using decorator change the value of x to original value


def my_decorator(subtract_2):
    def original(x):
        print("hello wrapper")
        return subtract_2(x+2)
    return original
    
@ my_decorator
def subtract_2(x):
    return x - 2


print(subtract_2(5))

# Step 1: Applying the Decorator
# @my_decorator
# def subtract_2(x):
#     return x - 2
# This decorator line is equivalent to:
# subtract_2 = my_decorator(subtract_2)Step 1: Applying the Decorator
# Calling subtract_2(5)
# Since subtract_2 is now original(x) (after the decorator), 
# this actually calls original(5), not the original function.