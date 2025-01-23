def function_b():
    from Script_Mdoule.Module_a import function_a  # Deferred import
    print("Function B called.")
    function_a()