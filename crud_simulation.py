students = {}

def create_student(student_id, name, mark):
    if student_id in students:
        print("Student already exists")
        return

    students[student_id] = {
        "name": name,
        "mark": mark
    }
    print("Student created successfully")


def read_students():
    for student_id, details in students.items():
        print(student_id, details)


def update_student(student_id, name, mark):
    if student_id not in students:
        print("Student not found")
        return

    students[student_id]["name"] = name
    students[student_id]["mark"] = mark
    print("Student updated successfully")


def delete_student(student_id):
    if student_id not in students:
        print("Student not found")
        return

    del students[student_id]
    print("Student deleted successfully")


create_student(1, "Arun", 85)
create_student(2, "Meera", 92)

print("\nAll students:")
read_students()

print("\nUpdating student:")
update_student(1, "Arun Kumar", 90)

print("\nAfter update:")
read_students()

print("\nDeleting student:")
delete_student(2)

print("\nFinal records:")
read_students()