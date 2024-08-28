# file_b.py

import file_a

def function_b(y):
    print(f"Value received in function_b: {y}")
    result = file_a.function_a(y * 2)
    return result

if __name__ == "__main__":
    value = 3
    final_result = function_b(value)
    print(f"Final result in file_b: {final_result}")
