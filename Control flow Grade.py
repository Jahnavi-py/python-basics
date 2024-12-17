#Use elif statements to print a grade based on a score: A, B, C, or Fail.
def grade_based_on_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'Fail'
score = int(input("Enter the score: "))
grade = grade_based_on_score(score)
print(f"The grade is: {grade}")
