""""
1491. Average Salary Excluding the Minimum and Maximum Salary

def average(salary):
    sorted_salary = sorted(salary)
    length = len(sorted_salary)
    sorted_salary[0] = 0
    sorted_salary[-1] = 0
    return sum(sorted_salary)/(length -2)
"""


"""
1523. Count Odd Numbers in an Interval Range

def countOdds(low high):
    first_odd_number = low if low % 2 != 0 else low + 1
    return (high - first_odd_number) // 2 + 1
"""