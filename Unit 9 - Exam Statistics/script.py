REVIEW
1. Let's look at those grades!

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

2. Print those grades

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def print_grades(grades):
    for grade in grades:
        print grade

print_grades(grades)

3. Review

print "Let's compute some stats!"

THE AVERAGE GRADE
4. The sum of scores

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def grades_sum(scores):
    total = 0
    for n in scores:
        total = total + n
        print total
    return total
grades_sum(grades)

5. Computing the Average

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def grades_sum(scores):
    total = 0
    for n in scores:
        total = total + n
        print total
    return total
grades_sum(grades)

6. Review

print "Time to conquer the variance!"

DO THE GRADES VARY ? 
7. The Variance

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2)
    return variance / (len(scores))

print grades_variance(grades)

8. Standard Deviation

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2)
    return variance / (len(scores))

print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print grades_std_deviation(variance)

9. Review

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2)
    return variance / (len(scores))

print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)

