# 1 function for getting marks from the user
def get_marks():
    english = int(input("Your marks in Englihs: "))
    maths = int(input("Your marks in Maths: "))
    physics = int(input("Your marks in Physics: "))
    chemistry = int(input("Your marks in Chemistry: "))
    social = int(input("Your marks in Social: "))
    return english, maths, physics, chemistry, social

# 2 function for calculating total marks
def get_total_marks(english, maths, physics, chemistry, social):
    return english + maths + physics + chemistry + social

# 3 function for finding average
def get_average(total):
    return total / 5

# 4 function to get average
def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"

# 5 function for displaying the result    
def display_result(total, average, grade):
    print("\n ------------ RESULT ------------")
    print("Total Marks: ", total)
    print("Average: ", average)

    if average >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    print("Grade: ", grade)
    print("Result: ", result)


#Main Program
english, maths, physics, chemistry, social = get_marks()
total = get_total_marks(english, maths, physics, chemistry, social)
average = get_average(total)
grade = get_grade(average)

display_result(total, average, grade)