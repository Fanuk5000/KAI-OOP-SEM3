from student import Student
from binary_tree import BinaryTree


if __name__ == "__main__":
    students_lst = [Student("John", "Doe", "Smith", "01-01-2000", 1, 1),
                         Student("Jane", "Roe", "Johnson", "02-02-2001", 2, 2),
                         Student("Alice", "Green", "Brown", "03-03-2002", 3, 3)]


    # Analog of generic collection on C#
    students_g_collection: list[Student] = []

    # if add an object that is not Student - static type analyzer will show an error
    students_g_collection.append(Student("Bob", "White", "Miller", "30-12-1998", 4, 1))
    students_g_collection.append(Student("Jane", "Roe", "Johnson", "23-05-1999", 3, 2))
    students_g_collection.append(Student("Charlie", "Black", "Wilson", "11-01-2002", 1, 3))

    # Non generic collection analog on C#
    students_collection:list = []

    students_collection.append(Student("Alice", "Green", "Brown", "15-07-2001", 2, 4))
    students_collection.append("Not a student object")  # This will not raise an error until
    students_collection.append(Student("Bruno", "Mars", "A", "08-10-1985", 5, 1))

    # Task 3-4
    bin_tree1 = BinaryTree(Student("Root", "Student", "Parent", "01-01-2000", 1, 1))
    bin_tree1.insert(Student("Left", "Child", "Parent", "02-02-2001", 2, 2))
    bin_tree1.insert(Student("Right", "Child", "Parent", "03-03-2002", 3, 3))
    bin_tree1.insert(Student("Left.Left", "Grandchild", "Parent", "04-04-2003", 4, 4))
    bin_tree1.insert(Student("Left.Right", "Grandchild", "Parent", "05-05-2004", 5, 5))

    bin_tree2 = BinaryTree(Student("Another", "Root", "Parent", "10-10-1999", 1, 1))
    bin_tree2.insert(Student("Another.Left", "Child", "Parent", "11-11-2000", 2, 2))
    bin_tree2.insert(Student("Another.Right", "Child", "Parent", "12-12-2001", 3, 3))

    print(bin_tree1 < bin_tree2)  # Compare based on student_id of root nodes

    for student in bin_tree1:
        print(student.student_info())