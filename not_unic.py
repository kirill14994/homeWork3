


list_of_numbers = [6, 1, 2, 7, 3, 5, 2, 1, 5]
result = list(set([i for i in list_of_numbers if list_of_numbers.count(i) > 1]))
print(result)