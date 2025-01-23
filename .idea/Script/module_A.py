def function_a():
    from module_B import function_b  # Deferred import
    print("Function A called.")
    function_b()
