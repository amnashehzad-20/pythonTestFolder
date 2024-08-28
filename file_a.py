# file_a.py

import file_b

def function_a(x):
    print(f"Value received in function_a: {x}")
    result = file_b.function_b(x + 10)
    return result

if __name__ == "__main__":
    value = 5
    final_result = function_a(value)
    print(f"Final result in file_a: {final_result}")
