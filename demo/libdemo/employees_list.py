# Read employees.txt and display dept followed by employees

f = open("employees.txt", "rt")  # Write Text

departments = {}
for line in f.readlines():
    line = line.strip()
    parts = line.split(",")
    if len(parts) < 2:
        continue

    dept, emp = parts
    if dept in departments:
        departments[dept].append(emp)  # Add employee to dept
    else:
        departments[dept] = [emp]    # Create new entry


for dept, employees in departments.items():
    print(f"{dept:5} {','.join(employees)}")

f.close()
