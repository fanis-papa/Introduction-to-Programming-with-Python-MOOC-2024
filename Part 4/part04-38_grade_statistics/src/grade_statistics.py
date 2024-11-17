import math

def main() -> list:
    fails = 0
    grades_tracker = [0, 0, 0, 0, 0, 0]
    grades_themselves_for_avg = []

    # during the loop and for each input, a function must be called to:
    # calculate and update the grades tracker. Will prob use an array for grades:
    #[0] will be grade 0 (fail), [1] grade 1, [2] grade 2 etc *UPD* grade_calculator will take care of that, grades are stored on the grade_tracker

    # increase the fails track var *UPD*  fails_tracker will take care of that. 

    # funcs will get the 2 array items nicely converted for arguments

    while True:
        input1 = input('Exam points and exercises completed: ')

    # When user enters an empty string, statistics will be called: Takes fails, the grades array grades_them... for averge as arg, calculates and prints everything

        if input1 == '':
            statistics(fails, grades_tracker, grades_themselves_for_avg)
            break

        exercise_points = math.floor(int(input1.split()[1]) / 10)
        exam_points = int(input1.split()[0])
    
        if fails_tracker(exercise_points, exam_points):
            fails += 1
            grades_tracker[0] += 1
    

        grade_updater = grade_calculator(exercise_points, exam_points)
        grades_themselves_for_avg.append(grade_updater[0])

        # print(f'Grade updater returns: {grade_updater[1]}')

        # here we dont really care about the exact points themselves (eg 23, 30, 10 etc). We care if the grade is 0 to 5. So we increase the grade_tracker at the appropriate index by 1 
        if grade_updater[1] != 0:
            grades_tracker[grade_updater[1]] += 1
        
        # print(f'Fail tracker returned {fails_tracker(exercise_points, exam_points)}')

        

# Returns a bool which will be used both in the loop to increase the fails var, necessary for calculations and printing later. Also is used on the calculator as a guard claw. 
def fails_tracker(exercise_points: int, exam_points: int) -> bool:
    if exam_points < 10 or exercise_points + exam_points < 15:
        return True
    else:
        return False

def grade_calculator(exercise_points: int, exam_points: int) -> list:

    total = exercise_points + exam_points
    return_value = [total, 0]

    # The function will simply return firstly the total. Will use it for averages. Also returns an int on the index 1 of the list. Will use that integer as the index of the grades tracker back on the loop, to increase the value of the num on that index by one. Later that value will be used for printing the statistics


    # print(f'exercise points are {exercise_points} -- exams points are {exam_points} -- total = {total}')
    

    if not fails_tracker(exercise_points, exam_points):
        if total > 14 and total < 18:
            return_value[1] = 1
        elif total >=18 and total < 21:
            return_value[1] = 2
        elif total >= 21 and total < 24:
            return_value[1] = 3
        elif total >= 24 and total < 28:
            return_value[1] = 4
        elif total >= 28:
            return_value[1] = 5

    return return_value
    
def statistics(fails: int, grades: list, average: list):


    # helper to print statistic for each grade. In essence its the index for each grade on the loop later 
    counter = 5

    pass_percentage = 100.0
    # print(f'Array of students grades for finding the average is: {average}')
    average_grade = sum(average)/ len(average)

    # to avoid errors when dividing by 0
    if fails > 0:
        pass_percentage = round(100 - (fails/ sum(grades)*100), 1)

    print('Statistics: ')
    print(f'Points average: {average_grade}')
    print(f'Pass percentage: {pass_percentage}')
    print('Grade distribution: ')
    for grade in grades[::-1]:
        print(f'  {counter}: {'*' * grade}') 
        counter -= 1




main()