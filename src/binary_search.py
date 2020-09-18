def binary_search(numbers_list,number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) //2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index +1

    return -1

if __name__=='__main__':
    numbers_list = [12,16,27,47,59,73,78,89,94,98]
    number_to_find = 781

    index = binary_search(numbers_list,number_to_find)
    print(f"Number found at index {index} using Binary search")

