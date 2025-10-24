def linear_search(arr, value):
    """
    Search for 'value' in list 'arr' using linear search.
    Prints the index if found, or reports not found.
    """
    for i, elem in enumerate(arr):
        if elem == value:
            print(f"Value {value} found at index {i}")
            return i
    print(f"Value {value} not found in the list")
    return -1

# Example usage:
if __name__ == "__main__":
    my_list = [5, 3, 8, 4, 2]
    val = 8
    linear_search(my_list, val)
    val = 7
    linear_search(my_list, val)
