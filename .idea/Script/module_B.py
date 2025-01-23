def function_b():
    from module_A import function_a  # Deferred import
    print("Function B called.")
    function_a()