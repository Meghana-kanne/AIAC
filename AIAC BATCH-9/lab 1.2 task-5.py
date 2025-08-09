def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

# Example usage:
num_lines = read_file('ashwitha.txt')
print(f"Number of lines: {num_lines}")