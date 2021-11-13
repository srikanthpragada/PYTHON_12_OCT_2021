# Read marks from student_marks.txt and display average for each student

f = open("student_marks.txt", "rt")  # Write Text

for line in f.readlines():
    smarks = filter(str.isdigit, line.split(","))  # select only numbers
    marks = list(map(int, smarks))
    avg = sum(marks) / len(marks)
    print(f"{avg:.2f}")

f.close()
