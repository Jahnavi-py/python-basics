def function_a():
    from Script_Mdoule.Module_b import function_b  # Deferred import
    print("Function A called.")
    function_b()