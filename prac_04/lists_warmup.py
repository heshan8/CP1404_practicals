"""WARM UP ACTIVITY"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> numbers = [3, 1, 4, 1, 5, 9] Removes one from the end
# numbers[3:4] -> [1] shows numbers within range including starting number
# 5 in numbers -> True 5 is in the list
# 7 in numbers -> False 7 Not in list
# "3" in numbers -> False Not in list
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] Adds them to the list

print(numbers)

numbers[0] = "ten"
print(numbers)

numbers[6] = 1
print(numbers)

print(numbers[2:7])

print(9 in numbers)
