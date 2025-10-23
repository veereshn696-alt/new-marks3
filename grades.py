marks=int(input("enter the marks :"))
i=0
if marks>90 :
    grade="a"
elif marks>80 :
    grade="b"
elif marks>70 :
    grade ="c"
elif marks>60 :
    grade="d"
else :
    grade="fail"
marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / 5

# Determine grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Average Marks: {average:.0f}")
print("Grade:",grade)