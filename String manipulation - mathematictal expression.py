#Parse a string containing mathematical expressions (e.g., 2+3*4) and evaluate it.
expression = "2 + 3 * 4"
result = eval(expression)
print(f"The result of '{expression}' is: {result}")

'''import ast
# Example of safe evaluation for simple expressions
expression = "2 + 3 * 4"
# You can use `ast.literal_eval()` for simple mathematical literals
try:
    result = ast.literal_eval(expression)
    print(f"The result of '{expression}' is: {result}")
except Exception as e:
    print(f"Error: {e}")'''
''' #Throws an error for this code.
import ast
# Example expression
expression = "2 + 3 * 4"
# Parse the expression into an AST
try:
    # Compile the expression into a code object and evaluate it
    parsed_expr = ast.parse(expression, mode='eval')
    result = eval(compile(parsed_expr, filename="<string>", mode="eval"))
    print(f"The result of '{expression}' is: {result}")
except Exception as e:
    print(f"Error: {e}")'''