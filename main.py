def get_student_data():
    """
    Function to get student data input from the user.
    Returns a list of dictionaries, each containing student's name and marks.
    """
    students = []
    try:
        num_students = int(input("Enter the number of students: "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return get_student_data()

    for i in range(num_students):
        print(f"\nEnter details for Student {i+1}:")
        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            return get_student_data()

        try:
            math = float(input("Math marks: "))
            science = float(input("Science marks: "))
            english = float(input("English marks: "))
            if not (0 <= math <= 100 and 0 <= science <= 100 and 0 <= english <= 100):
                print("Marks should be between 0 and 100.")
                return get_student_data()
        except ValueError:
            print("Invalid marks input. Please enter numeric values.")
            return get_student_data()

        student = {
            "Name": name,
            "Math": math,
            "Science": science,
            "English": english
        }
        students.append(student)
    return students

def calculate_scores(students):
    """
    Function to calculate total marks, average and assign grade for each student.
    Modifies the students list in place by adding 'Total', 'Average', and 'Grade'.
    """
    for student in students:
        total = student['Math'] + student['Science'] + student['English']
        average = total / 3
        student['Total'] = total
        student['Average'] = average
        student['Grade'] = assign_grade(average)

def assign_grade(average):
    """
    Function to assign grade based on average mark.
    """
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_class_average(students):
    """
    Calculate class average from all students' averages.
    """
    if not students:
        return 0
    total_avg = sum(student['Average'] for student in students)
    return total_avg / len(students)

def find_topper(students):
    """
    Find the student with highest total marks.
    """
    if not students:
        return None
    topper = max(students, key=lambda x: x['Total'])
    return topper

def display_results(students):
    """
    Displays the results in a tabular format,
    along with class average and topper info.
    """
    print("\nStudent Performance Summary:")
    print("="*70)
    header = f"{'Name':<15}{'Math':<10}{'Science':<10}{'English':<10}{'Total':<10}{'Average':<10}{'Grade':<10}"
    print(header)
    print("-"*70)
    for student in students:
        print(f"{student['Name']:<15}{student['Math']:<10.2f}{student['Science']:<10.2f}{student['English']:<10.2f}"
              f"{student['Total']:<10.2f}{student['Average']:<10.2f}{student['Grade']:<10}")

    class_avg = calculate_class_average(students)
    topper = find_topper(students)

    print("\n" + "="*70)
    print(f"Class Average: {class_avg:.2f}")
    if topper:
        print(f"Topper: {topper['Name']} with Total Marks = {topper['Total']:.2f}")
    print("="*70)

def main():
    print("Welcome to the Student Marks and Grades Summary Program\n")
    students = get_student_data()
    calculate_scores(students)
    display_results(students)

if __name__ == "__main__":
    main()
