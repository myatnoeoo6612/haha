score = 85

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"


print(f"The grade for a score of {score} is: {grade}")


test_scores = [95, 85, 75, 65, 55]
for ts in test_scores:
    if 90 <= ts <= 100:
        grade = "A"
    elif 80 <= ts < 90:
        grade = "B"
    elif 70 <= ts < 80:
        grade = "C"
    elif 60 <= ts < 70:
        grade = "D"
    else:
        grade = "F"
    print(f"The grade for a score of {ts} is: {grade}")
