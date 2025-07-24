# WAF which accepts a hyphen-separated sequence of colors. The function should return the colors in a hyphen-separated sequence after sorting them alphabetically.
# Constraint: All colors will be completely in either lower case or upper case.
# Sample Input 1: green-red-yellow-black-white
# Sample Output 1: black-green-red-white-yellow

def sort_colors(sequence):
    colors = sequence.split('-')
    sorted_colors = sorted(colors)
    return '-'.join(sorted_colors)

# Example usage:
input_sequence = input("Enter hyphen-separated colors: ")
print(sort_colors(input_sequence))
