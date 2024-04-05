# The built-in sum() and len() functions is used to determine the sum of the numbers within a list and...
#  the number of elements in the list, respectively.
# This is done by dividing the sum by the length of the list, to get the average.

# Calculating average using Len() and Sum()

test1 = float(input('Enter the score from the first test: '))
test2 = float(input('Enter the score from the second test: '))
test3 = float(input('Enter the score from the third test: '))
average = (test1 + test2 + test3)/3.0
print('the average score is', average)
print()

bisi_exam_score = float(input('Enter the score for bisi exams: '))
bisi_test_score = float(input('Enter the score for bisi tests: '))
ayo_exam_score = float(input('Enter the score for ayo exams: '))
ayo_test_score = float(input('Enter the score for ayo tests: '))
average_score_for_bisi = (bisi_exam_score + bisi_test_score)/2.0
average_score_for_ayo = (ayo_exam_score + ayo_test_score)/2.0
total_average_score_for_students = (average_score_for_ayo + average_score_for_bisi)
print('total_average_score_for_students', total_average_score_for_students)
print('average_score_for_ayo', average_score_for_ayo)
print('average_score_for_bisi', average_score_for_bisi)
print()

study_time_per_hours = [2,5,9,7,4]
sum = 0
for number in study_time_per_hours:
    sum += number
average = sum/len(study_time_per_hours)
print('Average time spent studying per week:', average, 'hours')
print()

business_year = [2021, 2022, 2023]
profit_made = [1000, 2000, 1500]
sum = 0
for number in profit_made:
    sum += number
average = sum/len(profit_made)
print('Average profit made for three business years:', average, 'dollars')
print()

def average (numbers):
    if len (numbers):
        return None
    else:
        return sum (numbers)/len(numbers)
list = [1, 2, 3, 6]
print ("The average of list is", round(average(list), 2))
# Ask for clarification for the above illustration


