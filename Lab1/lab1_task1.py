numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_of_numbers = 0
for value in numbers:
    if value:
        sum_of_numbers += value

count_of_numbers = len(numbers)
average_of_numbers = round(sum_of_numbers/count_of_numbers, 2)
numbers_modified = []

for i in numbers:
    if i is None:
        numbers_modified.append(average_of_numbers)
    else:
        numbers_modified.append(i)

numbers = numbers_modified


#TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
