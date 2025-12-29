#Task 1: Create a Dictionary of Student Marks

students={'Alice':85, 'Ron':39 , 'Harry':65 , 'Moana':93}
key_name=input("Enter the student's name: ")
key_name=key_name.title()

for name in students:
    if name==key_name:
        print(f"{name}'s marks: {students[name]} ")
        break
else:
    print("Student not found.")


#Sample Output (Student found)
'''
Enter the student's name: alice
Alice's marks: 85 
'''

#Sample Output (Student not found)
'''
Enter the student's name: john
Student not found.
'''
