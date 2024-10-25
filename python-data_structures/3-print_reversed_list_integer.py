#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Iterate over the list in reverse order
    for i in range(len(my_list) - 1, -1, -1):
        # Print each integer using str.format()
        print("{}".format(my_list[i]))

# Example usage
if __name__ == "__main__":
    print_reversed_list_integer([1, 2, 3, 4, 5])
