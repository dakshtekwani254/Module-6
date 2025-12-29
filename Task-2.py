#Task 2: Demonstrate List Slicing 

List=list(range(1, 11))
extracted = List[:5]
reversed_list = extracted[::-1]
print(f"Original List: {List}")
print(f"Extracted first five elements: {extracted}")
print(f"Reversed extracted elements: {reversed_list}")

#Sample Output
'''
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
'''
