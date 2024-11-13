numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
miss_index = numbers.index(None)
sum_numbers = sum(numbers[:miss_index] + numbers[miss_index+1:])
count_numbers = len(numbers)
average = sum_numbers / count_numbers
numbers[miss_index] = average
print("Измененный список:", numbers)
