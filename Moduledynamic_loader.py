#Write a script to dynamically load and execute a function from a module using the importlib library.
import importlib
def load_and_execute(module_name, function_name, *args, **kwargs):
    try:
        module = importlib.import_module(module_name)
        print(f"Module '{module_name}' loaded successfully.")
        func = getattr(module, function_name, None)
        if not func:
            raise AttributeError(f"Function '{function_name}' not found in module '{module_name}'.")
        print(f"Executing function '{function_name}' with arguments {args} and {kwargs}.")
        result = func(*args, **kwargs)
        return result
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    module_name = "math"
    function_name = "pow"
    args = (2, 3)
    result = load_and_execute(module_name, function_name, *args)
    if result is not None:
        print(f"Result: {result}")
