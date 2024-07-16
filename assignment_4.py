numbers = [1, 2, 3, 4, 5]
modified_numbers = [num + 10 if num % 2 == 0 else num - 1 for num in numbers]
print(modified_numbers)
