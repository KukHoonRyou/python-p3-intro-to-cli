#!/usr/bin/env python3

# def create_grade_report(student_grades):
#     with open('./reports/grade_report.txt', 'w') as gr:
#         for grade in student_grades:
#             # add '\n' to write grades on separate lines
#             gr.write(grade + '\n')

# if __name__ == '__main__':
#     student_grades = []

#     grade = input("Student name, grade: ")
#     while grade:
#         student_grades.append(grade)
#         # end when no grade is entered
#         grade = input("Student name, grade: ")

#     create_grade_report(student_grades)

# class MyClass:
#     def __init__(self, user_input):
#         self.value = user_input

# def my_function(my_object):
#     # CLI 워크플로에서 최종 값을 반환합니다
#     return my_object.value

# if __name__ == '__main__':
#     user_input = input("여기에 입력하세요: ")
#     my_object = MyClass(user_input)
#     print(my_function(my_object))

# number = 10
# result = isinstance(number, str)
# print(result)

import re

def validate_grade_input(input_string):
    # 숫자와 문자가 포함되어야 하며 쉼표로 구분된 형식을 검사하는 정규 표현식
    pattern = re.compile(r"^[A-Za-z]+,\s*[A-F]$")
    if not pattern.match(input_string):
        return False
    return True

user_input = input("학생 이름, 성적을 입력하세요 (예: John, A): ")
if validate_grade_input(user_input):
    print("올바른 입력입니다.")
else:
    print("잘못된 입력입니다. 형식에 맞춰 다시 입력해 주세요.")