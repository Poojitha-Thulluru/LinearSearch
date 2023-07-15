def get_element_count(num_array: list, value: int) -> int:
    count = 0
    for val in num_array:
        if value == val:
            count += 1
    return count


try:
    nums_array = list(map(int, input("Enter only Integers separated by space : ").split()))
    element = int(input("Enter an element to search in array : "))
    print("The count of an element in array is : ", get_element_count(nums_array, element))
except ValueError:
    print("Invalid input. Enter Only Integers")
