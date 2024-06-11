def limit_calls(max_calls):
    def decorator(func):
        
        # Initialize call count variable
        func._call_count = 0  # Call count variable

        # Wrapper function
        def wrapper(*args, **kwargs):
            if func._call_count >= max_calls:
                print(f"Function {func.__name__} has reached its call limit.")
                return None
            func._call_count += 1
            return func(*args, **kwargs)
        
        # Reset call count function
        def reset():
            func._call_count = 0  # Reset call count

        wrapper.reset = reset  # Add reset function to the wrapper
        return wrapper

    return decorator

@limit_calls(3)
def example_function():
    print("Function is called.")

# Calling the decorated function multiple times
example_function()
example_function()
example_function()
example_function()  # This call should not execute the function

# Resetting the call count
example_function.reset()

# Calling the decorated function again
example_function()
example_function()
example_function()
example_function()  # This call should not execute the function