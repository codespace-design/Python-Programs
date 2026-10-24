import json

students = [
    {"id": 1, "name": "Arun", "mark": 85},
    {"id": 2, "name": "Meera", "mark": 92}
]

# Write Python data into a JSON file
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("JSON file created successfully")

# Read data from the JSON file
with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

print("\nStudent records:")
for student in loaded_students:
    print(student)