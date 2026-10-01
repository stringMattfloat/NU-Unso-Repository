salary = {"E104": {
    "Employee Name": "Ada Lovelace",
    "Daily Hours": [40, 41.2, 42.3, 40]
    },
    "E601": {
    "Employee Name": "Charles Babbage",
    "Daily Hours": [39.40, 42, 38, 40]
            }
    }

print("=======================")
id = input("Employee ID: ")
print("=======================")

if id not in salary:
    print("Employee Not Found")
else:
    employee = salary[id]
    name = employee["Employee Name"]
    workHours = employee["Daily Hours"]

    # 9000 weekly basic
    weeklyBasic = 9000
    ratePH = weeklyBasic / 40
    weeklyH = sum(workHours)

    overtimeHours = 0

    for hours in workHours:
        if hours > 8:
            overtimeHours += hours - 8

    overtime = overtimeHours * ratePH * 1.5

    gross = (40 * ratePH) + overtime

print("========================")
print("Employee Name", name)
print("Employee ID", id)
print("Excess Hours", overtimeHours)
print("Rate Per Hour", ratePH)
print("Overtime", overtime)
print("Gross Pay", gross)
print("========================")
