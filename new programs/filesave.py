import json

# 1️⃣ Save data to a text file
def save_to_file():
    name = input("Enter name: ")
    age = input("Enter age: ")

    with open("data.txt", "w") as file:
        file.write("Name: " + name + "\n")
        file.write("Age: " + age + "\n")

    print("Data saved to text file")


# 2️⃣ Read data from a text file
def read_from_file():
    try:
        with open("data.txt", "r") as file:
            content = file.read()
            print("\nFile Content:")
            print(content)

    except FileNotFoundError:
        print("File not found")


# 3️⃣ Save data in JSON format
def save_to_json():
    student = {
        "name": input("Enter student name: "),
        "marks": int(input("Enter marks: ")),
        "course": input("Enter course: ")
    }

    with open("student.json", "w") as file:
        json.dump(student, file, indent=4)

    print("Data saved in JSON file")


# Main execution
save_to_file()
read_from_file()
save_to_json()