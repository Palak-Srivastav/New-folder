raw_data = (("Palak", 101, 85), ("Harry", 102, 92), ("Ron", 103, 78))

students_list = []
highest_marks = 0
topper_name = ""
total_marks = 0

for item in raw_data:
    student = {"Name": item[0], "Roll": item[1], "Marks": item[2]}
    
    students_list.append(student)
    
    total_marks += student["Marks"]
    
    if student["Marks"] > highest_marks:
        highest_marks = student["Marks"]
        topper_name = student["Name"]

# Calculate average
average = total_marks / len(students_list)

print("--- Student Records ---")
for student in students_list:
    print(f"Name: {student['Name']} | Roll: {student['Roll']} | Marks: {student['Marks']}")

print("-----------------------")
print(f"Average Marks: {average}")
print(f"Class Topper: {topper_name} with {highest_marks} marks")